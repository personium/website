---
id: version-1.7.21-271_Send_Message
title: メッセージ送信
sidebar_label: メッセージ送信
---
## 概要
メッセージを送信する

### 必要な権限
message

### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
```
{CellURL}__message/send
```
### メソッド
POST

### リクエストクエリ
クエリは無視する

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|BoxBound|Boxと紐付けるか否か|true / false<br>デフォルト値はfalse|×|Boxに結びつける場合に本項目を「true」にしてスキーマ認証したトークンを送る|
|InReplyTo|返信対象のメッセージID|桁数：32<br>null|×||
|To|送信先Cell URL|URL形式<br>null|※ 1|複数Cellに送信する場合はCSV形式で指定する<br>※1 ToまたはToRelationのどちらかは必須,<br>ToまたはToRelationで指定できる送信先Cell URLの最大件数は1000件|
|ToRelation|送信対象の関係名|桁数：1&#65374;128<br>文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)と+(プラス)と:(コロン)<br>ただし、先頭文字に_(半角アンダーバー)と:(コロン)は指定不可<br>null|※ 1|※1 ToまたはToRelationのどちらかは必須<br>ToまたはToRelationで指定できる送信先Cell URLの最大件数は1000件|
|Type|メッセージタイプ|message<br>request|×|省略時はmessageとして扱う|
|Title|メッセージタイトル|桁数：256文字以下|×|省略時は空文字として扱う|
|Body|メッセージ本文|桁数：64Kbyte以下|×|省略時は空文字として扱う|
|Priority|優先度|1~5|×|省略時は3として扱う|
|RequestObjects|リクエストの詳細|JSON配列|※2|※2 Typeがrequestの場合必須<br>詳細は下記RequestObject参照|

#### RequestObject
リクエストの詳細を記載する。  
RequestTypeに指定するTypeによって内容が異なる。  

##### Relation add/remove
RequestType : relation.add / relation.remove  
Name または ClassUrlで指定したRelationと、TargetUrlで指定したCellのリンク/リンク解除を依頼する。  

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|RequestType|リクエストの種別|relation.add<br>relation.remove|〇||
|Name|リレーション名|桁数：1～128<br>文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)と+(プラス)と:(コロン)<br>ただし、先頭文字に_(半角アンダーバー)と:(コロン)は指定不可|※1|※1 NameまたはClassUrlのどちらかは必須<br>Name指定時は以下のURLからの相対URLとみなす<br>BoxBoundがtrue：[対象BoxスキーマURL]\_\_relation/\_\_/<br>BoxBoundがfalse：[送信先Cell URL]\_\_relation/\_\_/|
|ClassUrl|リレーションクラスURL|リレーションクラスURL<br>詳細は[用語集](../introduction/008_Glossary.md#anc_r)を参照|※1|※1 NameまたはClassUrlのどちらかは必須|
|TargetUrl|関係を結ぶCell URL|URL形式|〇||

##### Role add/remove
RequestType : role.add / role.remove  
Name または ClassUrlで指定したRoleと、TargetUrlで指定したCellのリンク/リンク解除を依頼する。  

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|RequestType|リクエストの種別|role.add<br>role.remove|〇||
|Name|ロール名|桁数：1～128<br>文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)<br>ただし、先頭文字に-(半角ハイフン)と_(半角アンダーバー)は指定不可|※1|※1 NameまたはClassUrlのどちらかは必須<br>Name指定時は以下のURLからの相対URLとみなす<br>BoxBoundがtrue：[対象BoxスキーマURL]\_\_role/\_\_/<br>BoxBoundがfalse：[送信先Cell URL]\_\_role/\_\_/|
|ClassUrl|ロールクラスURL|ロールクラスURL<br>詳細は[用語集](../introduction/008_Glossary.md#anc_r)を参照|※1|※1 NameまたはClassUrlのどちらかは必須|
|TargetUrl|関係を結ぶCell URL|URL形式|〇||

##### Rule add/remove
RequestType : rule.add / rule.remove  
指定したRuleの作成/削除を依頼する。  

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|RequestType|リクエストの種別|rule.add<br>rule.remove|〇||
|Name|作成するルールを識別するため任意の名前|詳細は[Rule作成](2A0_Create_Rule.md)を参照|×||
|EventType|ルールをトリガーするイベントのタイプの前方一致検査用文字列|詳細は[Rule作成](2A0_Create_Rule.md)を参照|×||
|EventSubject|ルールをトリガーすべきイベントのEvent Subject一致検査用文字列|詳細は[Rule作成](2A0_Create_Rule.md)を参照|×|personium-localunitへ変換可能かチェックは行わない。|
|EventObject|ルールをトリガーすべきイベントのEvent Object前方一致検査用文字列|詳細は[Rule作成](2A0_Create_Rule.md)を参照|×||
|EventInfo|ルールをトリガーすべきイベントのEvent Info一致検査用文字列|詳細は[Rule作成](2A0_Create_Rule.md)を参照|×||
|Action|イベントがマッチしたときに起動すべきアクション|詳細は[Rule作成](2A0_Create_Rule.md)を参照|〇||
|TargetUrl|アクションに対する具体的なターゲットURL|詳細は[Rule作成](2A0_Create_Rule.md)を参照|×|personium-localunitへ変換可能かチェックは行わない。|

### リクエストサンプル
```JSON
{
  "BoxBound": true,
  "InReplyTo": "hnKXm44TTZCw-bfSEw4f0A",
  "To": "https://cell2.unit1.example/",
  "ToRelation": null,
  "Type": "request",
  "Title": "友人登録依頼です",
  "Body": "先日はありがとうごさいました。友人登録承認をお願いいたします。",
  "Priority": 3,
  "RequestObjects": [
    {
      "RequestType": "relation.add",
      "ClassUrl": "https://app-cell1.unit1.example/__relation/__/relation1",
      "TargetUrl": "https://cell2.unit1.example/"
    },
    {
      "RequestType": "role.add",
      "Name": "role1",
      "TargetUrl": "https://cell2.unit1.example/"
    }
  ]
}
```

## レスポンス
### ステータスコード
201

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|Location|作成したリソースへのURL||
|DataServiceVersion|ODataのバージョン||
|ETag|リソースのバージョン情報||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ

#### 共通レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおりです。

|オブジェクト|名前【キー）|型|値|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

#### SentMessage固有レスポンスボディ
|オブジェクト|名前【キー】|型|値|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ReceivedMessage|
|{2}|__id|string|受信メッセージID<br>UUIDで「b5d008e9092f489c8d3c574a768afc33」のような32文字の文字列を返却|
|{2}|InReplyTo|string|受信元メッセージID<br>UUIDで「b5d008e9092f489c8d3c574a768afc33」のような32文字の文字列を返却|
|{2}|To|string|送信先CellURL|
|{2}|ToRelation|string|送信対象の関係名|
|{2}|Type|string|メッセージタイプ<br>メッセージ：message<br>依頼：request|
|{2}|Title|string|メッセージタイトル|
|{2}|Body|string|メッセージ本文|
|{2}|Priority|string|優先度<br>(高)1&#65374;5(低)|
|{2}|RequestObjects|array|リクエストの詳細<br>オブジェクト{4}の配列|
|{4}|RequestType|string|リクエストの種別|
|{4}|Name|string|詳細はリクエストボディ参照|
|{4}|ClassUrl|string|詳細はリクエストボディ参照|
|{4}|TargetUrl|string|詳細はリクエストボディ参照|
|{4}|EventType|string|詳細はリクエストボディ参照|
|{4}|EventSubject|string|詳細はリクエストボディ参照|
|{4}|EventObject|string|詳細はリクエストボディ参照|
|{4}|EventInfo|string|詳細はリクエストボディ参照|
|{4}|Action|string|詳細はリクエストボディ参照|
|{2}|_Box.Name|string|関係対象のBox名|
|{2}|Result|array|送信先Cell毎の送信結果<br>オブジェクト{5}の配列|
|{5}|To|string|送信先CellURL|
|{5}|Code|string|ステータスコード|
|{5}|Reason|string|詳細メッセージ|
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/SentMessage
('3afcc60e35fc49ee9a4e4f6c1ebee426')",
        "etag": "W/\"1-1486638759524\"",
        "type": "CellCtl.SentMessage"
      },
      "__id": "3afcc60e35fc49ee9a4e4f6c1ebee426",
      "InReplyTo": "xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",
      "To": "https://cell2.unit1.example/",
      "ToRelation": null,
      "Type": "request",
      "Title": "メッセージサンプルタイトル",
      "Body": "メッセージサンプル本文です。",
      "Priority": 3,
      "RequestObjects": [
        {
          "RequestType": "relation.add",
          "Name": null,
          "ClassUrl": "https://app-cell1.unit1.example/__relation/__/relation1",
          "TargetUrl": "https://cell2.unit1.example/",
          "EventType": null,
          "EventSubject": null,
          "EventObject": null,
          "EventInfo": null,
          "Action": null
        }
      ],
      "_Box.Name": null,
      "Result": [
        {
          "To": "https://cell2.unit1.example/",
          "Code": "201",
          "Reason": "Created."
        }
      ],
      "__published": "/Date(1486638759524)/",
      "__updated": "/Date(1486638759524)/"
    }
  }
}
```

## cURLサンプル
```sh
curl "https://cell1.unit1.example/__message/send" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '{"BoxBound":false,"InReplyTo":"xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",\
"To":"https://cell2.unit1.example/","Type":"message","Title":"メッセージサンプルタイトル",\
"Body":"メッセージサンプル本文です。","Priority":3}'
```
