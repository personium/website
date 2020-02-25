---
id: version-1.7.18-333_List_ComplexType_links
title: ComplexTypeと他オブジェクトとのリンク一覧取得
sidebar_label: ComplexTypeと他オブジェクトとのリンク一覧取得
---
## 概要
ComplexTypeに紐付いたODataリソースを一覧取得する  
以下のODataリソースを指定することができる  
* Property

### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする


## リクエスト
### リクエストURL
Propertyとの$links
```
{CellURL}{BoxName}/{CollectionName}/$metadata/ComplexType('{ComplextypeName}')/$links/_Property
```

### メソッド
GET

### リクエストクエリ
以下のクエリパラメタが利用可能です。

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

<!---
[$select クエリ](406_Select_Query.md)

[$expand クエリ](405_Expand_Query.md)

[$format クエリ](404_Format_Query.md)

[$filter クエリ](403_Filter_Query.md)

[$inlinecount クエリ](407_Inlinecount_Query.md)

[$orderby クエリ](400_Orderby_Query.md)
-->

[$top クエリ](401_Top_Query.md)

[$skip クエリ](402_Skip_Query.md)

<!---
[全文検索(q)クエリ](408_Full_Text_Search_Query.md)
-->

### リクエストヘッダ
#### 共通リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|

#### OData共通リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|

#### OData一覧取得リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### リクエストボディ
なし


## レスポンス
### ステータスコード
200

### レスポンスヘッダ
#### 共通レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|

#### ODataレスポンスヘッダ

|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン情報||

### レスポンスボディ
#### OData $links レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおりです。

|オブジェクト|名前（キー）|型|値|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|uri|string|紐付いているODataリソースへのURL|

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": [
      {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/Property
(Name='property1',_EntityType.Name='entity-type1')"
      },
      {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/Property
(Name='property2',_EntityType.Name=null)"
      }
    ]
  }
}
```

## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/$metadata/ComplexType('complex-type1')\
/$links/_Property" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json'
```

