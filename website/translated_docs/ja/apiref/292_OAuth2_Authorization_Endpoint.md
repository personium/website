---
id: 292_OAuth2_Authorization_Endpoint
title: OAuth 2.0 認可エンドポイント
sidebar_label: OAuth 2.0 認可エンドポイント
---

## 概要
Cell の OAuth 2.0 認可エンドポイント。通常ブラウザで表示するための HTML を返します。しかし Cookie の状態等によってエンドユーザの認可が自動的になされると判断される場合は、認可コードやアクセストークン・IDトークンなどを返すための指定されたURLに直接リダイレクトすることもあります。

### 制限事項
OpenID Connect の ID token の発行は、以下指定のみサポート

* scope=openid
* response_type=id_token または code

## リクエスト
### リクエストURL
```
{CellURL}/__authz
```

### メソッド

GET

### リクエストクエリ
|項目名|概要|書式|必須|有効値|
|:--|:--|:--|:--|:--|
|response_type|応答タイプ|String|○|token, code, id_token(scope=openid必須)|
|client_id|アプリセル URL|String|○|スキーマ認証元のアプリセルURL|
|redirect_uri|クライアントのリダイレクトエンドポイントURL|String|○|アプリセルのデフォルトBOX配下に登録されたリダイレクトスクリプトのURL<br>application/x-www-form-urlencodedでフォーマットされたクエリパラメータを含める事ができる<br>フラグメントを含める事はできない<br>有効桁長:512byte|
|state|リクエストとコールバックの間で状態を維持するために使用するランダムな値|String|×|ランダムな値<br>有効桁長:512byte|
|scope|要求するアクセス範囲|String|×|Personiumでは"openid"等の値をスペース区切りで指定|
|expires_in|アクセストークンの有効期限（秒）|Int<br>1～3600|×|発行されるアクセストークンの有効期限を指定<br>デフォルトは3600（1時間）<br>※response_typeがtoken以外の場合は、本パラメタの指定は無視する|

### リクエストヘッダ
なし

## レスポンス
認証フォームまたはパスワード変更フォーム表示のためのHTMLを返却します。  
ただし、リクエストパラメータが不正な場合や、送信Cookieの値によってはリダイレクトエンドポイントにリダイレクトします。

### HTMLレスポンス
セルやユニットに設定された認証フォームまたはパスワード変更フォーム表示のためのHTMLを返却します。 設定がない場合はデフォルトhtmlが返ります。  

#### HTML設定方法
[Unitの設定](../server-operator/unit_config_list.md)または[対象Cellのプロパティ設定](./291_Cell_Change_Property.md)が必要。2つを同時に設定した場合、対象Cellのプロパティ設定が優先される。  

Unitの設定  
```
io.personium.core.cell.authorizationhtmlurl.default={htmlが取得可能なURL}
io.personium.core.cell.authorizationpasswordchangehtmlurl.default={htmlが取得可能なURL}
```

対象Cellのプロパティ設定  
```xml
<p:authorizationhtmlurl>{htmlが取得可能なURL}</p:authorizationhtmlurl>
<p:authorizationpasswordchangehtmlurl>{htmlが取得可能なURL}</p:authorizationpasswordchangehtmlurl>
```
URLに指定可能なスキームは"http","https","personium-localunit","personium-localcell"。

#### HTML 要求仕様
設定するHTMLから送信されるフォームリクエスト電文を受け取るため、本エンドポイントは POST メソッドも受け付けます。HTMLを実装するときは、 [こちら](./292p_OAuth2_Authorization_Endpoint.md) のドキュメントを参照してください。


#### ステータスコード
200  
#### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|text/html; charset=UTF-8||

#### レスポンスボディ
認証フォームまたはパスワード変更フォーム(HTML)を返却する。  
リクエスト時に設定したpassword_change_requiredがtrueの場合、パスワード変更フォームを返却する。  
それ以外の場合、認証フォームを返却する。


### パラメータチェックエラー（client_id、redirect_uri）
「client_id、redirect_uriが未指定」「client_id、redirect_uriがURL形式ではない」「client_idとredirect_uriのセルが異なる」の場合
#### ステータスコード
303  
ブラウザはシステムのエラーページにリダイレクトされる。
```
{error_page_uri}?code={code}
```

#### URLパラメータ
|項目名|概要|備考|
|:--|:--|:--|
|error_page_uri|Redirect URL|システムのエラーページ「セルのURL + __html/error」|
|code|[Personiumのメッセージコード](004_Error_Messages.md)||

### パラメータチェックエラー（上記以外）
client_id、redirect_uri、username、password以外のリクエストパラメータで、必須項目が未設定もしくは設定値が不正な形式の場合<br>
または、cancel_flgにtrueが設定されている（ユーザによりキャンセルされた）場合
#### ステータスコード
303  
ブラウザはクライアントのリダイレクトエンドポイントURL（リクエストの「redirect_uri」の値）にリダイレクトされる。  
redirect_uriに、「URLパラメータ」で示すフラグメントまたはクエリが格納される。  
（response_type=codeの場合はクエリが格納され、それ以外の場合はフラグメントが格納される）
```
{redirect_uri}?error={error}&error_description={error_description}&state={state}&code={code}
{redirect_uri}#error={error}&error_description={error_description}&state={state}&code={code}
```
#### URLパラメータ
|項目名|概要|備考|
|:--|:--|:--|
|redirect_uri|Redirect URL|リクエストの「redirect_uri」で指定された、<br>クライアントのリダイレクトスプリクトのURL|
|error|エラー内容を示すコード|「error」を参照|
|error_description|エラーの追加情報|例外メッセージなどを設定する|
|error_uri|エラーの追加情報のWebページのURI|空文字を返す<br>※今後のエンハンスに備えて設定|
|state|リクエスト時に設定したstateの値||
|code|[Personiumのメッセージコード](004_Error_Messages.md)||
##### error
|コード値|概要|備考|
|:--|:--|:--|
|invalid_request|リクエストで必須パラメータが指定されていない<br>リクエストパラメータの形式が不正||
|unauthorized_client|ユーザによってキャンセルされた||
|unsupported_response_type|response_typeの値が不正||
|server_error|サーバエラー||

## 認可処理成功レスポンス
認可処理を行う。処理結果によってリダイレクト先やURLパラメータが異なる。  
処理結果のパターンは以下の通り。
- 認可処理成功（Implicit 認可）
- 認可処理成功（認可コード）
- 認可処理成功（IDトークン発行）
- 認証失敗
- パラメータチェックエラー（client_id、redirect_uri）
- パラメータチェックエラー（上記以外）

### 認可処理成功（Implicit 認可）
認可処理に成功 かつ リクエストのresponse_typeにtokenを指定した場合

#### ステータスコード
303  
ブラウザはクライアントのリダイレクトエンドポイントURL（リクエストの「redirect_uri」の値）にリダイレクトされる。<br>
redirect_uriに、「URLパラメータ」で示すフラグメントが格納される。
```
{redirect_uri}#access_token={access_token}&token_type=Bearer&expires_in={expires_in}&state={state}&last_authenticated={last_authenticated}
&failed_count={failed_count}
※実際には改行されず一行で返却される
```

#### URLパラメータ
|項目名|概要|備考|
|:--|:--|:--|
|redirect_uri|クライアントのリダイレクトエンドポイントURL|リクエストの「redirect_uri」の値|
|access_token|取得されたアクセストークン|セルローカルトークンもしくは、トランスセルトークンを返却する|
|token_type|Bearer||
|expires_in|アクセストークンの有効期限（秒）|リクエスト時に設定した有効期限<br>デフォルトは3600（1時間）|
|state|リクエスト時に設定したstateの値|リクエストとコールバックの間で状態を維持するために使用するランダムな値|
|last_authenticated|前回認証日時|前回の認証日時（long型のUNIX時間）<br>初回認証時はnull<br>※パスワード認証の場合のみ返却する|
|failed_count|認証失敗回数|前回認証時からのパスワード認証に連続で失敗した回数<br>※パスワード認証の場合のみ返却する|
|box_not_installed|Box未インストールフラグ|アプリセルURLをスキーマに持つBoxが作成されていない場合のみtrueを返却する|

### 認可処理成功（認可コード）
認可処理に成功 かつ リクエストのresponse_typeにcodeを指定した場合
#### ステータスコード
303  
ブラウザはクライアントのリダイレクトエンドポイント（リクエストの「redirect_uri」の値）にリダイレクトされる。<br>
redirect_uriに、「URLパラメータ」で示すクエリが格納される。
```
{redirect_uri}?code={code}&state={state}&last_authenticated={last_authenticated}&failed_count={failed_count}
```
#### URLパラメータ
|項目名|概要|備考|
|:--|:--|:--|
|redirect_uri|クライアントのリダイレクトエンドポイントURL|リクエストの「redirect_uri」の値|
|code|取得されたCode|grant_type:authorization_codeで認可可能なCode|
|state|リクエスト時に設定したstateの値|リクエストとコールバックの間で状態を維持するために使用するランダムな値|
|last_authenticated|前回認証日時|前回の認証日時（long型のUNIX時間）<br>初回認証時はnull<br>※パスワード認証の場合のみ返却する|
|failed_count|認証失敗回数|前回認証時からのパスワード認証に連続で失敗した回数<br>※パスワード認証の場合のみ返却する|
|box_not_installed|Box未インストールフラグ|アプリセルURLをスキーマに持つBoxが作成されていない場合のみtrueを返却する|

### 認可処理成功（IDトークン発行）
認可処理に成功 かつ リクエストのresponse_typeにid_tokenを指定した場合

#### ステータスコード
303  
ブラウザはクライアントのリダイレクトエンドポイントURL（リクエストの「redirect_uri」の値）にリダイレクトされる。<br>
redirect_uriに、「URLパラメータ」で示すフラグメントが格納される。
```
{redirect_uri}#id_token={id_token}&state={state}&last_authenticated={last_authenticated}&failed_count={failed_count}
```

#### URLパラメータ
|項目名|概要|備考|
|:--|:--|:--|
|redirect_uri|クライアントのリダイレクトエンドポイントURL|リクエストの「redirect_uri」の値|
|id_token|取得されたid_token|OpenID Connectで利用可能なid_token|
|state|リクエスト時に設定したstateの値|リクエストとコールバックの間で状態を維持するために使用するランダムな値|
|last_authenticated|前回認証日時|前回の認証日時（long型のUNIX時間）<br>初回認証時はnull<br>※パスワード認証の場合のみ返却する|
|failed_count|認証失敗回数|前回認証時からのパスワード認証に連続で失敗した回数<br>※パスワード認証の場合のみ返却する|
|box_not_installed|Box未インストールフラグ|アプリセルURLをスキーマに持つBoxが作成されていない場合のみtrueを返却する|

### 認証失敗
認証に失敗した場合（パスワード不一致、アカウントロック中など）

#### ステータスコード
303  
ブラウザは認可エンドポイント（セルのURL + \_\_authz）に再度リダイレクトされる。  
認可エンドポイントに、「URLパラメータ」で示すクエリが格納される。
```
{authorization_endpoint_url}?response_type={response_type}&redirect_uri={redirect_uri}&client_id={client_id}&state={state}&scope={scope}
&expires_in={expires_in}&error={error}&error_description={error_description}&error_uri={error_uri}&code={code}
&password_change_required={password_change_required}&access_token={access_token}
※実際には改行されず一行で返却される
```
#### URLパラメータ
|項目名|概要|備考|
|:--|:--|:--|
|authorization_endpoint_url|認可エンドポイントのURL（セルのURL + __authz）||
|response_type|リクエスト時に設定したresponse_typeの値||
|client_id|リクエスト時に設定したclient_idの値||
|redirect_uri|リクエスト時に設定したredirect_uriの値||
|state|リクエスト時に設定したstateの値||
|scope|リクエスト時に設定したscopeの値||
|expires_in|リクエスト時に設定したexpires_inの値||
|error|エラー内容を示すコード|「error」を参照|
|error_description|エラーの追加情報|例外メッセージなどを設定する|
|error_uri|エラーの追加情報のWebページのURI|空文字を返す<br>※今後のエンハンスに備えて設定|
|code|[Personiumのメッセージコード](004_Error_Messages.md)||
|password_change_required|認証したアカウントがパスワード変更必須かを示すフラグ|認証できるがパスワード変更が必須の場合にのみtrueを返却する|
|access_token|認証したアカウントのアクセストークン|password_change_requiredがtrueの場合のみパスワード変更のみ可能なアクセストークンを返却|

##### error
|コード値|概要|備考|
|:--|:--|:--|
|invalid_request|認証に必須なパラメータ（username、password）が指定されていない||
|invalid_grant|認証失敗<br>アカウントロック中||
|unauthorized_client|クライアントが認可されていない<br>パスワード変更が必要||
|server_error|サーバエラー||

### パラメータチェックエラー（client_id、redirect_uri）
「client_id、redirect_uriが未指定」「client_id、redirect_uriがURL形式ではない」「client_idとredirect_uriのセルが異なる」の場合  
「レスポンス（認証フォームリクエスト）」の「パラメータチェックエラー（client_id、redirect_uri）」と同様。

### パラメータチェックエラー（上記以外）
client_id、redirect_uri、username、password以外のリクエストパラメータで、必須項目が未設定もしくは設定値が不正な形式の場合  
「レスポンス（認証フォームリクエスト）」の「パラメータチェックエラー（上記以外）」と同様。

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__authz?\
response_type=token&\
client_id=https://app-cell1.unit1.example&
redirect_uri=https://app-cell1.unit1.example/__/redirect.md&\
state=0000000111" -X GET -i
```
