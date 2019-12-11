# イベントバスへの Web Socket 接続

## 概要

Cellで発生するイベントが通るイベントバスにWebSocketで接続して、発生イベント情報を受け取ったり、バスに外部イベントを送信することができます。
本APIは最初にアクセストークンの送信を要求します。該当トークンがイベントバス接続可能な権限をもつときのみ接続を許可します。
次に購読条件を指定します。これにより条件に合致するイベントのみがリアルタイムにクライアントに送信されます。

### 必要な権限

event-read : イベント情報の購読取得  
event : 外部イベントを送信

## 接続とセッション開始

### 接続エンドポイントURL

    wss://{UnitFQDN}/{CellName}/__event

か

    wss://{CellName}.{UnitFQDN}/__event

まず上記URLにWebSocketでの接続を行ってください。アクセストークンを受け付ける状態となります。この状態ではアクセストークン送付以外のいかなるメッセージ送信も意味を持ちません。

### アクセストークン送付によるセッション開始

#### リクエストメッセージ

権限のあるアクセストークンを以下形式で送付することでイベントバス接続セッションを開始します。  

    {"AccessToken":"AA~91WT0GNoVGFHJFQ.......e"}

#### レスポンスメッセージ

有効なトークンであれば以下の応答が返り、セッション開始となります。セッション開始によりイベント購読可能状態となりますが、まだイベント購読はしていないため何もイベントは流れてきません。

    {"Response":"AccessToken", "Result":"Success", "ExpiresIn":3600, "Timestamp":1518612600}

トークンが無効であったり、トークンに必要な権限がない場合はCellはWebSocket接続を切断します。


## セッション開始後の通信

セッション確立後は以下のコマンドをリクエストメッセージとしてクライアントから送信可能です。

1. イベントの購読
1. 外部イベントの発火
1. イベントの購読解除
1. セッションの状態取得
1. アクセストークンの再送信

イベントを購読することで、購読条件に合致するイベントの発生時にリアルタイムでイベント情報が流れてくるようになります。またイベントの購読は条件を変えながら任意の数の複数行うことができます。セッション状態取得コマンドで現在の購読状況やセッションの残り時間などの情報が取得可能です。また、アクセストークン送信のコマンドで新たなアクセストークンを送信することでセッションの有効期限を延ばすことができます。

これらコマンドのリクエストメッセージを送信すると速やかにレスポンスメッセージが返ります。リクエストメッセージの記述に問題があるときはエラー応答メッセージが返ります。

## イベントの購読

### リクエストメッセージ

    {"Subscribe": {"Type": "${EventType}", "Object": "${EventObject}"}}

* Type, Objectともに前方一致でのマッチを判定します。
* Type, Objectともに任意の値にマッチさせたい場合は * を指定します。


### レスポンスメッセージ

    {"Response":"Subscribe", "Result":"Success","Timestamp":1518612600}


## イベントの受け取り

何らかの購読設定がなされている状態で購読購読条件にに合致するイベントがCellで発生すると、以下形式のメッセージがクライアントに送られます。  

    {
      "Type":"chat", 
      "RequestKey":null,
      "Schema":null,
      "External":true,
      "Object":"general",
      "Info":"Hello World", 
      "Subject":"https:\/\/demo.personium.io\/john.doe\/#me",
      "Timestamp":1518612600
    }

## 外部イベントの発火

以下形式のメッセージを送信することで外部イベントを発火することができます。

    {
      "Type":"chat", 
      "RequestKey":null,
      "Object":"general",
      "Info":"Hello World" 
    }


## セッション状態取得

### リクエストメッセージ

購読状況の取得

    {"State": "Subscriptions"}

全状況の取得

    {"State": "All"}

### レスポンスメッセージ

購読状況の取得時

    {
      "Response":"State", 
      "Result":"Success", 
      "Subscriptions": [], 
      "Timestamp":1518612600
    }

全状況の取得時

    {
      "Response":"State", 
      "Result":"Success", 
      "Cell":"${cell_name}", 
      "ExpiresIn": 2986, 
      "Subscriptions": [], 
      "Timestamp":1518612600
    }

## イベントの購読解除

### リクエストメッセージ

    {"Unsubscribe": {"Type": "${EventType}", "Object": "${EventObject}"}}

### レスポンスメッセージ

    {"Response":"Unsubscribe","Result":"success","Timestamp":1518612600}

## エラーレスポンスメッセージ

    {"Response": "${CorrespondingRequest}", "Result":"Error", "Reason": "${ErrorMessage}"}


|エラーメッセージ|説明|
|:--|:--|
|Format error|コマンドメッセージのフォーマットが正しくないとき|
|Subscriptions not found|存在しない購読条件を購読解除しようとしたとき|


## WebSocket詳細仕様

|項目|仕様|
|:--|:--|
|プロトコル|Sec-WebSocket-Version 13(RFC 6455)|
|メッセージフォーマット|JSON|
|ping/pong|アクセストークンメッセージ受領後毎分1回pingをCellから送信|

* クライアント側で10回PONGの返信がないとセッションを切断する
* ブラウザの場合は自動でPONGが返信されるため対応不要
