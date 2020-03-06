---
id: version-1.7.21-292p_OAuth2_Authorization_Endpoint
title: OAuth2.0 認可エンドポイントにおける POST の受け入れ
sidebar_label: OAuth2.0 認可エンドポイントにおける POST の受け入れ
---

## 概要
OAuth 2.0 認可エンドポイントでは、POSTメソッドを受け付けます。
これは、OAuth 2.0 認可エンドポイントへのGETで返されるHTMLから送信されるフォーム電文を受け取るためのものです。

### 制限事項
OpenID ConnectのID tokenの発行は、以下指定のみサポート

* scope=openid
* response_type=id_token または code

## リクエスト
### リクエストURL
```
{CellURL}/__authz
```

### メソッド

POST

### リクエストボディ
|項目名|概要|書式|必須|有効値|
|:--|:--|:--|:--|:--|
|response_type|応答タイプ|String|○|token, code, id_token(scope=openid必須)|
|client_id|アプリセル URL|String|○|スキーマ認証元のアプリセルURL|
|redirect_uri|クライアントのリダイレクトエンドポイントURL|String|○|アプリセルのデフォルトBOX配下に登録されたリダイレクトスクリプトのURL<br>application/x-www-form-urlencodedでフォーマットされたクエリパラメータを含める事ができる<br>フラグメントを含める事はできない<br>有効桁長:512byte|
|state|リクエストとコールバックの間で状態を維持するために使用するランダムな値|String|×|ランダムな値<br>有効桁長:512byte|
|scope|要求するアクセス範囲|String|×|Personiumでは"openid"を指定可能|
|username|ユーザ名|String|×|登録済のユーザ名<br>※認証フォームリクエスト時、本パラメタの指定は無視する|
|password|パスワード|String|×|登録済のパスワード<br>※認証フォームリクエスト時、本パラメタの指定は無視する|
|expires_in|アクセストークンの有効期限（秒）|Int<br>1～3600|×|発行されるアクセストークンの有効期限を指定<br>デフォルトは3600（1時間）<br>※response_typeがtoken以外の場合は、本パラメタの指定は無視する|
|cancel_flg|キャンセルフラグ|Boolean|×|認可処理のユーザキャンセルフラグ<br>trueが設定された場合、ユーザによりキャンセルされたものとする|
|password_change_required|パスワード変更必須フラグ|Boolean|×|認証したアカウントがパスワード変更必須であったかを示すフラグ<br>※認可リクエストのレスポンスで返却されたpassword_change_required|
|access_token|アクセストークン|String|×|認証したアカウントのアクセストークンを指定<br>※認可リクエストのレスポンスで返却されたaccess_token|

### リクエストヘッダ
なし

### リクエストクエリ
リクエストクエリと同じ



## レスポンス（認可処理リクエスト）
認可処理を行う。処理結果によってリダイレクト先やURLパラメータが異なる。  
処理結果のパターンは以下の通り。
- 認可処理成功（トークン認証）
- 認可処理成功（コード認証）
- 認可処理成功（IDトークン認証）
- 認証失敗
- パラメータチェックエラー（client_id、redirect_uri）
- パラメータチェックエラー（上記以外）

### 認可処理成功（トークン認証）
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

### 認可処理成功（コード認証）
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

### 認可処理成功（IDトークン認証）
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


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__authz" -X POST -i \
-d 'response_type=token&client_id=https://app-cell1.unit1.example/&\
redirect_uri=https://app-cell1.unit1.example/__/redirect.md&\
state=0000000111&username=account1&password=pass'
```
