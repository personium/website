---
id: version-1.7.18-235_List_Relation
title: Relation一覧取得
sidebar_label: Relation一覧取得
---
## 概要
既存のRelation情報の一覧を取得する

### 必要な権限
social-read

### 制限事項
* OData制限
	- リクエストヘッダのAcceptは無視される
	- リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
	- リクエストボディはJSON形式のみ受け付ける
	- レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
	- $formatクエリオプションは無視される

## リクエスト
### リクエストURL
```
{CellURL}__ctl/Relation
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

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
### ODataリクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
### OData登録リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
なし


## レスポンス
### ステータスコード
200

### レスポンスヘッダ
なし

### レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおりです。

|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

### Relation固有レスポンスボディ

|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.Relation|
|{2}|Name|string|Relation名|
|{2}|_Box.Name|string|関係対象のBox名|
### レスポンスサンプル
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri":
          "https://cell1.unit1.example/__ctl/Relation(Name='relation1',_Box.Name='box1')",
          "etag": "W/\"1-1486538244016\"",
          "type": "CellCtl.Relation"
        },
        "Name": "relation1",
        "_Box.Name": "box1",
        "__published": "/Date(1486538244016)/",
        "__updated": "/Date(1486538244016)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation1'
,_Box.Name='box1')/_Box"
          }
        },
        "_ExtCell": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation1'
,_Box.Name='box1')/_ExtCell"
          }
        },
        "_ExtRole": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation1'
,_Box.Name='box1')/_ExtRole"
          }
        },
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation1'
,_Box.Name='box1')/_Role"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation2'
,_Box.Name='box2')",
          "etag": "W/\"1-1486538757303\"",
          "type": "CellCtl.Relation"
        },
        "Name": "relation2",
        "_Box.Name": "box2",
        "__published": "/Date(1486538757303)/",
        "__updated": "/Date(1486538757303)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation2'
,_Box.Name='box2')/_Box"
          }
        },
        "_ExtCell": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation2'
,_Box.Name='box2')/_ExtCell"
          }
        },
        "_ExtRole": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation2'
,_Box.Name='box2')/_ExtRole"
          }
        },
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation2'
,_Box.Name='box2')/_Role"
          }
        }
      }
    ]
  }
}
```
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Relation" -X GET -i  \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

