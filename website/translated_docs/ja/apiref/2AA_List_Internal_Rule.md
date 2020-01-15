---
id: 2AA_List_Internal_Rule
title: Rule内部情報一覧取得
sidebar_label: Rule内部情報一覧取得
---
## 概要
システム内部のRule情報の一覧を取得する

### 必要な権限
rule-read

## リクエスト
### リクエストURL
```
{CellURL}__rule
```
### メソッド
GET

### リクエストクエリ
以下のクエリパラメタが利用可能です。

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### リクエストボディ
なし

## レスポンス
### ステータスコード
200

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### ODataレスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||

### レスポンスボディ
レスポンスはJSONオブジェクトです。

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__rule" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```
