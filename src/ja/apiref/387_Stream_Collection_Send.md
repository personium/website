# Stream Collection送信
## 概要
Stream Collectionのqueueやtopicにデータを送信する

### 必要な権限
stream-send

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{CollectionName}/queue/{QueueName}
```
```
{CellURL}{BoxName}/{CollectionName}/topic/{TopicName}
```

### メソッド
POST<br>
PUT

### リクエストクエリ
クエリは無視する

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### リクエストボディ
JSON

Formatに規定はありません。

### queueとtopic
Stream Collectionの[設定](386_Configure_Stream_Collection.md)にてQueue名やTopic名を登録しておく必要があります。
登録されていない場合は、404エラーとなります。

queueに送信したデータは、Stream Collectionの[受信](388_Stream_Collection_Receive.md)により取得可能です。
ただし、queueは一度しか取得できないため、誰かが受信した場合は、取得できません。

topicに送信したデータは、Stream Collectionの[WebSocket接続](389_Stream_Collection_Connect.md)により取得可能です。
ただし、送信前に接続をしておく必要があります。接続後に送信したデータのみ取得可能です。

## レスポンス
### ステータスコード
200

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル
```sh
curl "https://cell1.unit1.example/box1/steram-colleciton1/queue/name" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-d '{"hoge":false,"piyo":"test"}'
```
