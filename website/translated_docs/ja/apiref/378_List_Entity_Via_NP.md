---
id: 378_List_Entity_Via_NP
title: EntityのNavigation Property経由での他オブジェクト一覧取得
sidebar_label: EntityのNavigation Property経由での他オブジェクト一覧取得
---
## 概要
ユーザデータのEntity一覧をNavigation Property経由で取得します。
### 必要な権限
read


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}('{EntityID}')
/{NavigationPropertyName}
```
|パス|概要|
|:--|:--|
|{CellName}|Cell名|
|{BoxName}|Box名|
|{ODataCollecitonName}|コレクション名|
|{EntityTypeName}|EntityTypeName名|
|{EntityID}|EntityのID|
|{NavigationPropertyName}|NavigationProperty名|
指定できるNavigationProperty名は、EntitySetと以下の関連を持つものに限る。

|From|To|
|:--|:--|
|0 .. 1|0 .. 1|
|0 .. 1|1|
|0 .. 1|*|
|1|0 .. 1|
|1|1|
|1|*|
|*|0 .. 1|
|*|1|
|*|*|
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
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
なし


## レスポンス
### ステータスコード
200
### レスポンスヘッダ
|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン情報|正常にEntityが作成できた場合のみ返却する|
### レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおり

|オブジェクト|名前（キー）|型|値|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{3}|type|string|EntityType名|
|{2}|__id|string|EntityのID(__id)|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{2}|{NP名}|string|オブジェクト{4}<br>Linkが結ばれている場合のみ返却される。{NP名}:NavigationPropert名|
|{4}|__deferred|object|オブジェクト{5}|
|{5}|uri|string|関係を結んでいるリソースのuri|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

上記以外にスキーマ設定した項目、または登録時に指定した動的な項目を返却
#### 数値の扱い
#### 小数値（Edm.Single型）
* JSON形式でUserODataを取得する場合の取り扱いは以下の通り
	* 10.0等の小数部が0となる値は、整数値として返却する

#### 数値（Edm.Double型）
※PersoniumでのDouble型の扱いは、JavaのDoubleの仕様に従います
* JSON形式でUserODataを取得する場合の取り扱いは以下の通り
	* 10.0等の小数部が0となる値は、整数値として返却する
* 返却される値について
	* 登録時の入力値が倍精度以上の精度を持った数である場合、倍精度に丸められてデータ登録を行う
		* 内部的には浮動小数点数として管理されるが、出力時には情報落ちの起こらない範囲で固定小数点数表現に変換して出力する  
		出力された固定小数点数を入力に用いた場合、その入力数ともとの数との同一性は保証される

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')",
          "etag": "W/\"2-1487645572476\"",
          "type": "UserData.entity-type1"
        },
        "__id": "100-1_20101108-111352093",
        "__published": "/Date(1487645572476)/",
        "__updated": "/Date(1487645572476)/",
        "TestProperty": null,
        "_TestEntity": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')/navigation-property1"
          }
        }
      }
    ]
  }
}

```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('100-1_20101108-111352093')\
/navigation-property1" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H \
'Accept: application/json'
```

