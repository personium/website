---
id: version-1.7.18-297_OAtuh2_Token_Introspection_Endpoint
title: OAuth 2.0 Token Introspection Endpoint
sidebar_label: OAuth 2.0 Token Introspection Endpoint
---
## 概要
トークンの内容を取得するAPIのエンドポイントです。 RFC7662を実装しています。

トークンのIssuerかAudienceがCellURLと等しい場合のみ結果を返します。

### 必要な権限
なし

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/x-www-form-urlencodedとして扱う
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする

## リクエスト
### リクエストURL
```
{CellURL}/__introspect
```
### メソッド
POST

### リクエストヘッダ

|項目名|概要|書式|必須|有効値|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {Token}<br>Basic {Base64String}|○|Bearerの場合、認証トークンは認証トークン取得APIで取得したアクセストークン。ユニットマスタートークンかユニットユーザトークン、もしくは、トークンのSchemaがリクエストボディで指定するtokenのSchemaと一致する場合のみtokenの情報を取得可能。<br>Basicの場合、ユーザ名とパスワードは、Unitの設定でIntrospection用に設定されたもの、もしくは、CellURLとトークンを指定。CellURLとトークンの場合は、クライアント認証がOKかつCellURLがtokenのSchemaと一致する場合のみtokenの情報を取得可能|
|Content-Type|リクエストボディの形式を指定する|application/x-www-form-urlencoded|×|省略時は[application/x-www-form-urlencoded]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### リクエストボディ

|項目名|概要|書式|必須|有効値|
|:--|:--|:--|:--|:--|
|token|トークン|String|○|認証トークン取得APIで取得したアクセストークンかリフレッシュトークン|

### リクエストサンプル

```
token=AA~(省略)

```

## レスポンス
### ステータスコード
200

### レスポンスヘッダ

|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|application/json||

### レスポンスボディ

|項目名|概要|型|備考|
|:--|:--|:--|:--|
|active|トークンが有効かどうか|boolean||
|client_id|クライアントID|string|personiumではトークンのschema|
|exp|有効期限|integer|January 1 1970 UTCからの秒数|
|iat|発行時刻|integer|January 1 1970 UTCからの秒数|
|sub|トークンの主体|string|personiumではトークンのsubject|
|aud|トークンのオーディエンス|string|personiumではトランスセルトークンにおけるtarget|
|iss|トークンの発行者|string|トークンを発行したCellのURL|
|p_roles|トークンに含まれるロールのリスト|list of string|personium独自仕様|

### レスポンスサンプル
有効なトークンの場合
```JSON
{
  "active": true,
  "exp": 1544059820,
  "iat": 1543973420,
  "sub": "https://cell1.unit1.example/#account",
  "aud": "https://cell2.unit1.example/",
  "iss": "https://cell1.unit1.example/",
  "p_roles": ["https://cell1.unit1.example/__role/__/role1","https://cell1.unit1.example/__role/__/role2"]
}
```
無効なトークンの場合
```JSON
{
  "active": false,
}
```

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル
```sh
curl "https://cell1.unit1.example/__introspect" -X POST -i \
-H 'Authorization:Basic username:password' \
-H 'Content-Type:application/x-www-form-urlencoded' \
-H 'Accept:application/json' \
-d 'token=RA~(省略)'
```
