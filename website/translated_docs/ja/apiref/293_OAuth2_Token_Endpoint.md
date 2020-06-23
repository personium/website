---
id: 293_OAuth2_Token_Endpoint
title: OAuth 2.0 トークンエンドポイント
sidebar_label: OAuth 2.0 トークンエンドポイント
---
## 概要

セルの様々なAPIにアクセスするためのアクセストークンを発行するAPIのエンドポイントです。 OAuth 2.0仕様に準拠しており、様々な方法でユーザやアプリを認証してアクセストークンやリフレッシュトークン等を発行します。

### ユーザ認証のバリエーション

#### パスワードによるアカウント所有者認証

* OAuth 2.0 の ROPC (Resource Owner Password Credential) フローです。
* 登録したアカウントの名前とパスワードに基づきアカウントの所有者を認証してアクセストークン発行を受けることができます。
* 総当たり攻撃に対する防御策として、認証に失敗後1秒間はそのアカウントについてはパスワードが正当であっても認証エラーとなります。
* このフローはセルGUIをはじめとして、セル所有者が高いレベルの信用を置く前提であるセル管理アプリのみが使うべきものです。
* OAuth 2.0の仕様に記述されているとおり、このフローを一般のPersoniumアプリは使うべきではありません。

#### トランスセルアクセストークンによる他セルユーザの認証

* OAuth 2.0 拡張の SAML2 assertion フローに対応する認証方法です。
* このセル宛のトランスセルアクセストークンを送信することで、他セルユーザを認証してアクセストークン発行を受けることができます。
* 送信するトランスセルアクセストークンの発行を受けたときにアプリ認証を経ていた場合も、ここでアプリの再認証が必要となります。

#### リフレッシュトークン送信によるユーザ認証状態継続

* リフレッシュトークンを送信することでそのリフレッシュトークン発行時にうけたユーザ認証状態を引き継いだ新たなアクセストークン発行を受けることができます。
* 送信するリフレッシュトークンの発行を受けたときにアプリ認証を経ていた場合も、ここでアプリの再認証が必要となります。
* トークンリフレッシュ時に別アプリのclient_id, client_secretを送信することで、アプリの切り替えをすることはできません。
* セルアプリから一般アプリへのシングルサインオンなどアプリ間で認証状態を引き継ぎたい場合は、必要に応じてOpenID Connectの IDトークンを使ってください。アクセストークンやリフレッシュトークンをアプリ間で共有・やり取りはすべきではありません。

### アプリ認証のための情報送信

* PersoniumではOAuthのclient認証の枠組を使ってアプリの認証を行います。
* Personiumではclient_idとして、アプリのスキーマURIを用います。多くの場合スキーマURIはアプリセルのURLです。
* Personiumではclient_secretとしてアプリ認証トークンを用います。
* アプリ認証のための情報送信は必須ではありません。

### 発行トークン指定のバリエーション

#### アクセストークンの発行

p_target というパラメタの指定がないときはこのセルで有効なアクセストークン（セルローカルアクセストークン）を発行します。

#### トランスセルアクセストークンの発行

p_target というパラメタで他のセルのURLを指定することで、他のセルにアクセスするためのトランスセルアクセストークンを発行します。


### その他のバリエーション

#### クッキーの発行

* p_cookie というパラメタをtrue値で指定することでこのセルでのみ有効なクッキーを発行します。
* このクッキーは単体ではアクセストークンの代わりになりませんが、同時に発行されるcookie_peerという文字列と共に用いることでアクセストークン同等の効果を持ちます。
* このセル上のリソースをGETするさいにURLにcookie_peerというクエリパラメタでこの値をつけてアクセスすることで、同時に送られるクッキーと対応が取れているときのみ、アクセストークン送信と同様の扱います。
* これにより例えばHTMLの img video audio等のタグで非公開のメディアを許可されたユーザにのみ表示することなどが可能です。
* 発行されるクッキーはこのセルでのみ有効なものであるため、他セルアクセスのためのトークン取得用パラメタであるp_target と併用することはできません。

### 認証履歴の記録

パスワード認証（認可タイプにpasswordをリクエスト時に設定した場合）の際、認証履歴として前回の認証日時と認証失敗回数を記録します。<br>
認証履歴を記録しないアカウントを[対象Cellのプロパティ設定](./291_Cell_Change_Property.md)で設定可能です。

対象Cellのプロパティ設定
```xml
<p:accountsnotrecordingauthhistory>{アカウント名（カンマ区切りで複数指定可）}</p:accountsnotrecordingauthhistory>
```

## リクエスト
### リクエストURL
```
{CellURL}/__token
```
### メソッド
POST

### リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ

|項目名|概要|書式|必須|有効値|
|:--|:--|:--|:--|:--|
|Authorization|OAuth 2.0でClient認証に用いる|Basic {String}|×|OAuth 2.0 に定められたとおり、本ヘッダを使いBasic認証の形式でClient認証を行うことができます。Basic に続いて{{アプリのスキーマURI}:{アプリ認証トークン}}をBase64Encodeした値を送信してください。<br>リクエストボディにclient_assertion_typeやclient_assertionパラメタの指定がある場合それを優先します。client_idとclient_secretの設定があっても本ヘッダの指定を優先します。|
|Content-Type|リクエストボディの形式を指定|application/x-www-form-urlencodedのみ有効|×|省略時は[application/x-www-form-urlencoded]として扱う|

### リクエストボディ


|項目名|概要|書式|必須|有効値|
|:--|:--|:--|:--|:--|
|grant_type|認可タイプ|String|○|password<br>urn&#58;x-personium:oidc:google<br>urn&#58;ietf:params:oauth:grant-type:saml2-bearer<br>authorization_code<br>refresh_token|
|username|ユーザ名|String|(grant_type=passwordの場合必須)|登録済のユーザ名|
|password|パスワード|String|(grant_type=passwordの場合必須)|登録済のパスワード|
|assertion|トランスセルアクセストークン|String|(grant_type=urn&#58;ietf:params:oauth:grant-type:saml2-bearerの場合)|有効なトランスセルアクセストークン|
|code|認可コード|String|(grant_type=authorization_codeの場合必須)|有効な認可コード|
|refresh_token|リフレッシュトークン|String|(grant_type=refresh_tokenの場合必須)|有効なリフレッシュトークン|
|id_token|IDトークン|JSON Web Token|(grant_type=urn&#58;x-personium:oidc:googleの場合必須)|有効なIDトークン|
|p_target|発行ターゲット|String|×|任意の他者セルURL<br>指定した場合そのセル宛のトランスセルアクセストークンを発行|
|client_assertion_type|client_assertionのタイプ|String|×|RFC7522の定義値"urn:ietf:params:oauth:grant-type:saml2-bearer"のみ有効。このパラメタやclient_assertionの設定があるときはRFC7522の動作を優先的に行い、Authorizationヘッダの内容やclient_sercretの内容は参照せずにClient認証を行う。|
|client_assertion|アプリ認証トークン|String|×|アプリセル等から発行されるアプリ認証トークン<br>client_assertion_typeとともに指定した場合アプリ認証済トークンを発行<br>このパラメタやclient_assertion_typeの設定があるときはRFC7522の動作を優先的に行う。（Authorizationヘッダの内容やclient_sercretの内容は参照しない。）|
|client_id|アプリのスキーマURI|String|(grant_type=authorization_codeの場合必須)|多くの場合アプリセルURL<br>client_assertion, client_secretとともに有効値を指定した場合アプリ認証済トークンを発行。|
|client_secret|アプリ認証トークン|String|×|アプリセル等から発行されるアプリ認証トークン<br>client_idとともに指定した場合アプリ認証済トークンを発行<br>同時にAuthorizationヘッダで同様情報が送信された場合、Authorizationヘッダの設定が優先される|
|scope|要求scope|String|×|アプリが求めるscope情報をスペース区切りで指定|
|p_owner|Unitユーザ昇格指定|String|×|trueのみ有効|
|p_cookie|認証クッキー発行オプション<br>指定された場合は認証クッキーを発行する<br>p_targetが指定された場合は、本パラメタの指定は無視する|String|×|trueのみ有効|
|expires_in|アクセストークンの有効期限（秒）|Int<br>1～3600|×|発行されるアクセストークンの有効期限を指定<br>デフォルトは3600（1時間）|
|refresh_token_expires_in|リフレッシュトークンの有効期限（秒）|Int<br>1～86400|×|発行されるリフレッシュトークンの有効期限を指定<br>デフォルトは86400（24時間）<br>p_ownerが指定された場合は、本パラメタの指定は無視する|


### リクエストサンプル

パスワードによるアカウント所有者認証
```
grant_type=password&username=username&password=pass
```


パスワードによるアカウント所有者認証でトランスセルアクセストークン発行
```
grant_type=password&username=username&password=pass&p_target=https://cell1.unit1.example/
```

パスワードによるアカウント所有者認証とアプリ認証トークン送付によるアプリ認証済アクセストークン発行
```
grant_type=password&username=username&password=pass&client_id=https://app-cell1.unit1.example/
&client_secret=WjzDmvJ...(省略)...4nHgo

```

Google発行のOpen ID Connect Id Tokenによるアカウント所有者認証
```
grant_type=urn:x-personium:oidc:google&id_token=IDTOKEN
```

トランスセルアクセストークンによる他セルユーザ認証
```
grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion=WjzDmvJ...(省略)...4nHgo
```

リフレッシュトークンによるトークンのリフレッシュ
```
grant_type=refresh_token&refresh_token=RA~uELM...(省略)...yWMoQ
```

パスワードによるアカウント所有者認証でクッキーも発行
```
grant_type=password&username=username&password=pass&p_cookie=true
```



## レスポンス
### ステータスコード
200

### レスポンスヘッダ

|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|application/json||
|Set-Cookie|クッキー認証情報（p_cookie）|クッキー発行オプション（p_cookie）をリクエスト時に設定した場合のみ|

### レスポンスボディ

|項目名|概要|備考|
|:--|:--|:--|
|access_token|アクセストークン||
|refresh_token|リフレッシュトークン|※p_ownerをリクエスト時に設定した場合、返却されない|
|token_type|Bearer||
|scope|要求に応じて発行されたトークンに認められたscope|複数のスコープが返る場合は、スペース区切り文字列で返却|
|expires_in|アクセストークンの有効期限（秒）|リクエスト時に設定した有効期限<br>デフォルトは3600（1時間）|
|refresh_token_expires_in|リフレッシュトークンの有効期限（秒）|リクエスト時に設定した有効期限<br>デフォルトは86400（24時間）<br>※p_ownerをリクエスト時に設定した場合、返却されない|
|id_token|OpenID Connectで利用可能なid_token|grant_type=authorization_code かつ<br>codeのscopeがopenidである<br>場合のみ返却する|
|p_cookie_peer|クッキー認証値|クッキー認証時に指定する認証値<br>※クッキー発行オプション（p_cookie）をリクエスト時に設定した場合のみ返却する|
|last_authenticated|前回認証日時|前回の認証日時（long型のUNIX時間）<br>初回認証時はnull<br>※認可タイプ（grant_type）にpasswordをリクエスト時に設定した場合のみ返却する|
|failed_count|認証失敗回数|前回認証時からのパスワード認証に連続で失敗した回数<br>※認可タイプ（grant_type）にpasswordをリクエスト時に設定した場合のみ返却する|

### レスポンスサンプル
```JSON
{
  "access_token": "AA~PBDc...(省略)...FrTjA",
  "refresh_token_expires_in": 86400,
  "refresh_token": "RA~uELM...(省略)...yWMoQ",
  "token_type": "Bearer",
  "scope": "root",
  "expires_in": 3600,
  "last_authenticated": 1486462510467,
  "failed_count": 2
}
```
### 認証失敗時
エラーのレスポンスを返す。[エラーメッセージ一覧](004_Error_Messages.md)の認証系APIを参照<br>
レスポンスボディは以下の通り。

|項目名|概要|備考|
|:--|:--|:--|
|error|OAUTH エラーコード||
|error_description|[{メッセージコード}] - {メッセージ}|メッセージコードとメッセージを結合した文字列を返却|
|access_token|アクセストークン|メッセージコードが"PR401-AN-0001"の場合にのみ返却する<br>パスワード変更のみ可能なアクセストークンを返却|
|url|URL|メッセージコードが"PR401-AN-0001"の場合にのみ返却する<br>パスワード変更APIのURLを返却|
|last_authenticated|前回認証日時|メッセージコードが"PR401-AN-0001"の場合にのみ返却する|
|failed_count|認証失敗回数|メッセージコードが"PR401-AN-0001"の場合にのみ返却する|

## cURLサンプル
#### アカウント所有者認証
```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=password&username=user1&password=pass'
```
#### 他セルユーザ認証
```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion=WjzDmvJ...(省略)...4nHgo'
```
#### トークンリフレッシュ
```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=refresh_token&refresh_token=RA~uELM...(省略)...yWMoQ'
```
#### アカウント所有者 + アプリ認証
```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=password&username=name1&password=pass&client_id=\
https://app-cell1.unit1.example/&client_secret=WjzDmvJ...(省略)...4nHgo'
```
#### 他セルユーザ認証 による他セル向けトランスセルアクセストークン発行
```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion=\
WjzDmvJ...(省略)...4nHgo&p_target=https://cell1.unit1.example/'
```
