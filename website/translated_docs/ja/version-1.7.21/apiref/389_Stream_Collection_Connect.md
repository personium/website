---
id: version-1.7.21-389_Stream_Collection_Connect
title: Stream Collection への Web Socket 接続
sidebar_label: Stream Collection への Web Socket 接続
---

## 概要
Stream Collectionのtopicへ送信されたデータをリアルタイムに受信することができます。  
本APIは最初にアクセストークンの送信を要求します。該当トークンがtopicの受信権限をもつときのみ接続を許可します。

### 必要な権限
* read : topicの存在確認のため
* stream-receive : topicからデータを受信するため

## 接続とセッション開始

### 接続エンドポイントURL
```
    wss://{CellName}.{UnitFQDN}/__topic/{BoxName}/{Path}
```
か
```
    wss://{UnitFQDN}/{CellName}/__topic/{BoxName}/{Path}
```

{Path}は、Stream Collectionの送信時のパスから{CellName}と{BoxName}を除いて、"/"を"."に変更したものを指定します。  
例えば、送信時のURLが
```
    https://cell1.unit1.example/box1/stream-collection1/topic/name
```
のときは、WebSocket接続は、
```
    wss://cell1.unit1.example/__topic/box1/stream-collection1.topic.name
```
になります。

まず上記URLにWebSocketでの接続を行ってください。アクセストークンを受け付ける状態となります。この状態ではアクセストークン送付以外のいかなるメッセージ送信も意味を持ちません。

### アクセストークン送付によるセッション開始

#### リクエストメッセージ

権限のあるアクセストークンを以下形式で送付することでイベントバス接続セッションを開始します。  

    {"AccessToken":"AA~91WT0GNoVGFHJFQ.......e"}

#### レスポンスメッセージ

有効なトークンであれば以下の応答が返り、セッション開始となります。

    {"Response":"AccessToken", "Result":"Success", "ExpiresIn":3600, "Timestamp":1518612600}

トークンが無効であったり、トークンに必要な権限がない場合は以下の応答を返し、WebSocket接続を切断します。

    {"Response":"AccessToken", "Result":"Error", "Reason":"Token inactive", "Timestamp":1518612600}


## セッション開始後の通信

セッション確立後は以下のコマンドをリクエストメッセージとしてクライアントから送信可能です。

* アクセストークンの再送信

アクセストークン送信のコマンドで新たなアクセストークンを送信することでセッションの有効期限を延ばすことができます。

リクエストメッセージを送信すると速やかにレスポンスメッセージが返ります。
リクエストメッセージの記述に問題があるときはエラー応答メッセージを返し、WebSocket接続を切断します。

## データの受け取り

topicにデータが送信されると、JSON形式のデータがクライアントに送られます。  

    {
      "From":"{CellURL}", 
      "Body":{データ}
    }

Fromには、topicにデータを送信したCellのCellURLが設定されます。Bodyには送信されたデータが設定されます。  
例えば、
```
{"hoge":"testmessage", "flag":true}
```
が cell1 (https://cell1.unit1.example/) から送信されたときは、 
```
{"From":"https://cell1.unit1.example/", "Body":{"hoge":"testmessage", "flag":true}}
```
を受信します。

## エラーレスポンスメッセージ

    {"Response": "${CorrespondingRequest}", "Result":"Error", "Reason": "${ErrorMessage}"}

|エラーメッセージ|説明|
|:--|:--|
|Invalid message|リクエストメッセージが不正なとき|
|Token inactive|トークンが無効なとき|
|Session expired|トークンの有効期限が切れたとき。リクエスト時のみレスポンスが返ります。CorrespondingRequestはUnknownとなります。|


## WebSocket詳細仕様

|項目|仕様|
|:--|:--|
|プロトコル|Sec-WebSocket-Version 13(RFC 6455)|
|メッセージフォーマット|JSON|
|ping/pong|アクセストークンメッセージ受領後毎分1回pingをCellから送信|

* クライアント側で10回PONGの返信がないとセッションを切断する
* ブラウザの場合は自動でPONGが返信されるため対応不要
