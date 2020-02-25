---
id: version-1.7.18-390_Options_Stream_Collection
title: Streamコレクションの操作可能メソッド取得
sidebar_label: Streamコレクションの操作可能メソッド取得
---
## 概要
Streamコレクションで操作可能なメソッドをトークンの権限に応じて返却する。

### 必要な権限
なし

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{CollectionName}/queue/{QueueName}
```
```
{CellURL}{BoxName}/{CollectionName}/topic/{TopicName}
```

### メソッド
OPTIONS

### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|

※認証情報は必須です。認証情報がない場合、OPTIONSメソッドのレスポンスは、すべてのメソッドをAllowヘッダに設定したものとなります。

## レスポンス
### ステータスコード
200

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Access-Control-Allow-Methods|CORS用ヘッダ|[CORS対応](002_CORS_Support.md)参照|
|Allow|操作可能なメソッド|送信可能であればOPTIONSとPOSTとPUT、受信可能であればOPTIONSとGET、どちらも可能であればOPTIONSとPOSTとPUTとGET、どちらも不可であればOPTIONSが設定される|

### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/stream-collection1/queue/name" -X OPTIONS -i -H \
"Authorization:Bearer AA~PBDc...(省略)...FrTjA"
```
