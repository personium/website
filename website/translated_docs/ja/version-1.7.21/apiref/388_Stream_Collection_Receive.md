---
id: version-1.7.21-388_Stream_Collection_Receive
title: Stream Collection受信
sidebar_label: Stream Collection受信
---
## 概要
Stream Collectionのqueueからデータを受信する

### 必要な権限
stream-receive

### 制限事項
* リクエストヘッダのAcceptは無視される
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{CollectionName}/queue/{QueueName}
```

### メソッド
GET

### リクエストクエリ
クエリは無視する

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### queueの設定
Stream Collectionの[設定変更](386_Configure_Stream_Collection.md)にてQueue名を登録しておく必要があります。
登録されていない場合は、404エラーとなります。

## レスポンス
### ステータスコード
200

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Content-Type|返却されるデータの形式||

### レスポンスボディ
JSON配列

メッセージキューにより、取得されるデータが複数の場合があるため、配列でレスポンスを返します。
送信されたデータがない場合は空の配列が返ります。

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル
```sh
curl "https://cell1.unit1.example/box1/steram-colleciton1/queue/name" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```
