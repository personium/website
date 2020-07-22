---
id: version-1.7.21-268_List_Received_Messages
title: ReceivedMessage一覧取得
sidebar_label: ReceivedMessage一覧取得
---
## 概要
受信メッセージ情報を取得する
### 必要な権限
message または message-read
### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
```
{CellURL}__ctl/ReceivedMessage
```
### メソッド
GET
### リクエストクエリ
以下のクエリパラメタが利用可能です。

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

[$select クエリ](406_Select_Query.md)

[$expand クエリ](405_Expand_Query.md)

[$format クエリ](404_Format_Query.md)

[$filter クエリ](403_Filter_Query.md)

[$inlinecount クエリ](407_Inlinecount_Query.md)

[$orderby クエリ](400_Orderby_Query.md)

[$top クエリ](401_Top_Query.md)

[$skip クエリ](402_Skip_Query.md)

[全文検索(q)クエリ](408_Full_Text_Search_Query.md)

### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
#### OData共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
#### OData取得リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|If-None-Match|対象ETag値を指定する|ETag値|×|省略時は[*]として扱う|
### リクエストボディ
なし

## レスポンス
### ステータスコード
200
### レスポンスヘッダ
なし
### レスポンスボディ
#### 共通レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおりです。

|オブジェクト|名前(キー）|型|値|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

#### ReceivedMessage固有レスポンスボディ
|オブジェクト|名前（キー）|型|値|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ReceivedMessage|
|{2}|__id|string|受信メッセージID<br>UUIDで「b5d008e9092f489c8d3c574a768afc33」のような32文字の文字列を返却|
|{2}|_Box.Name|string|関係対象のBox名|
|{2}|InReplyTo|string|受信元メッセージID<br>UUIDで「b5d008e9092f489c8d3c574a768afc33」のような32文字の文字列を返却|
|{2}|From|string|送信元Cell URL|
|{2}|MulticastTo|string|受信先Cell URL<br>複数Cellが送信先の場合にCSV形式でCellのURLを返却|
|{2}|Type|string|メッセージタイプ<br>メッセージ：message<br>依頼：request|
|{2}|Title|string|メッセージタイトル|
|{2}|Body|string|メッセージ本文|
|{2}|Priority|string|優先度<br>(高)1&#65374;5(低)|
|{2}|Status|string|メッセージステータス<br>Typeがmessageの場合<br>　read：既読<br>　unread：未読<br>Typeがrequest<br>　approved：承認<br>　rejected：拒否<br>　none：未決|
|{2}|RequestObjects|array|リクエストの詳細<br>オブジェクト{4}の配列|
|{4}|RequestType|string|リクエストの種別|
|{4}|Name|string|詳細は[メッセージ送信](271_Send_Message.md)参照|
|{4}|ClassUrl|string|詳細は[メッセージ送信](271_Send_Message.md)参照|
|{4}|TargetUrl|string|詳細は[メッセージ送信](271_Send_Message.md)参照|
|{4}|EventType|string|詳細は[メッセージ送信](271_Send_Message.md)参照|
|{4}|EventSubject|string|詳細は[メッセージ送信](271_Send_Message.md)参照|
|{4}|EventObject|string|詳細は[メッセージ送信](271_Send_Message.md)参照|
|{4}|EventInfo|string|詳細は[メッセージ送信](271_Send_Message.md)参照|
|{4}|Action|string|詳細は[メッセージ送信](271_Send_Message.md)参照|

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/ReceivedMessage
('c87b42e10df846a9bee842225d1383fe')",
          "etag": "W/\"1-1486683974451\"",
          "type": "CellCtl.ReceivedMessage"
        },
        "__id": "c87b42e10df846a9bee842225d1383fe",
        "_Box.Name": "box1",
        "InReplyTo": "xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",
        "From": "https://cell2.unit1.example/",
        "MulticastTo": null,
        "Type": "request",
        "Title": "メッセージサンプルタイトル",
        "Body": "メッセージサンプル本文です。",
        "Priority": 3,
        "Status": "unread",
        "RequestObjects": [
          {
            "RequestType": "relation.add",
            "Name": null,
            "ClassUrl": "https://app-cell1.unit1.example/__relation/__/relation1",
            "TargetUrl": "https://cell1.unit1.example/",
            "EventType": null,
            "EventSubject": null,
            "EventObject": null,
            "EventInfo": null,
            "Action": null
          }
        ],
        "__published": "/Date(1486683974451)/",
        "__updated": "/Date(1486683974451)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ReceivedMessage
('c87b42e10df846a9bee842225d1383fe')/_Box"
          }
        },
        "_AccountRead": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ReceivedMessage
('c87b42e10df846a9bee842225d1383fe')/_AccountRead"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/ReceivedMessage
('3afcc60e35fc49ee9a4e4f6c1ebee426')",
          "etag": "W/\"3-1486688634556\"",
          "type": "CellCtl.ReceivedMessage"
        },
        "__id": "3afcc60e35fc49ee9a4e4f6c1ebee426",
        "_Box.Name": null,
        "InReplyTo": "xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",
        "From": "https://cell1.unit1.example/",
        "MulticastTo": null,
        "Type": "message",
        "Title": "メッセージサンプルタイトル",
        "Body": "メッセージサンプル本文です。",
        "Priority": 3,
        "Status": "read",
        "__published": "/Date(1486638759669)/",
        "__updated": "/Date(1486688634556)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ReceivedMessage
('3afcc60e35fc49ee9a4e4f6c1ebee426')/_Box"
          }
        },
        "_AccountRead": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ReceivedMessage
('3afcc60e35fc49ee9a4e4f6c1ebee426')/_AccountRead"
          }
        }
      }
    ]
  }
}
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/ReceivedMessage" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```
