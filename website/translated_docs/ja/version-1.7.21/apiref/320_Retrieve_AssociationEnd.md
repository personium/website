---
id: version-1.7.21-320_Retrieve_AssociationEnd
title: AssociationEnd取得
sidebar_label: AssociationEnd取得
---
## 概要
既存のAssociationEnd情報を取得する

### 必要な権限
read

### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata/AssociationEnd(Name='{AssociationEndName}'
,_EntityType.Name='{EntityTypeName}')
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

### リクエストヘッダ
#### 共通リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
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

|オブジェクト|名前（キー）|型|値|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

#### AssociationEnd固有レスポンスボディ

|オブジェクト|名前（キー）|型|値|
|:--|:--|:--|:--|
|{3}|type|string|ODataSvcSchema.AssociationEnd|
|{2}|Name|string|AssociationEnd名|
|{2}|Multiplicity|string|多重度|
|{2}|_EntityType.Name|string|関係対象のEntityType名|

### レスポンスサンプル
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name='entity-type1')",
        "etag": "W/\"1-1487652733383\"",
        "type": "ODataSvcSchema.AssociationEnd"
      },
      "Name": "association-end1",
      "Multiplicity": "1",
      "_EntityType.Name": "entity-type1",
      "__published": "/Date(1487652733383)/",
      "__updated": "/Date(1487652733383)/",
      "_EntityType": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name='entity-type1')/_EntityType"
        }
      },
      "_AssociationEnd": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name='entity-type1')/_AssociationEnd"
        }
      }
    }
  }
}
```
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/AssociationEnd\
(Name='association-end1',_EntityType.Name='entity-type1')" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

