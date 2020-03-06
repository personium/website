---
id: version-1.7.21-366_Retrieve_Entity
title: Entity取得
sidebar_label: Entity取得
---
## 概要
ユーザデータのEntityを一件取得します。
### 必要な権限
read
### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない
  - ユーザデータ制限事項
  - Edm.DateTime型のプロパティの有効範囲のチェックが適切に行われない
  - Edm.DateTime型の配列は未サポート
  - Edm.DateTime型のプロパティにSYSUTCDATETIME()を指定した場合、設定されるシステム時間が異なる場合がある
      - リクエストボディでの設定時とDefaultValueでの設定時（\__published、\__updatedは後者のタイミング）
  - 1つのEntityTypeに対して作成出来るのは、DynamicProperty・DeclaredProperty・ComplexTypeProperty合わせて400個まで


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}({EntityID})}
```
|パス|概要|
|:--|:--|
|{CellName}|セル名|
|{BoxName}|ボックス名|
|{ODataCollecitonName}|コレクション名|
|{EntityTypeName}|EntityType名|
|{EntityID}|取得するEntityのID|
### メソッド
GET
### リクエストクエリ
以下のクエリパラメタが利用可能です。

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効クッキーの認証情報を利用する場合に指定する|

[$select クエリ](406_Select_Query.md)

[$expand クエリ](405_Expand_Query.md)

[$format クエリ](404_Format_Query.md)

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
|If-None-Match|ETagの値を指定し、変更がない場合は304、変更されている場合は最新リソースを返却する||×|ETagに一致しないEntityを取得する場合に指定<br>未対応|
### リクエストボディ
なし


## レスポンス
### ステータスコード
200

### レスポンスヘッダ
|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン情報|正常にEntityが取得できた場合のみ返却する|
### レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおり

|オブジェクト|名前（キー）|型|値|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{3}|type|string|UserData.{EntityTypeName}|
|{2}|__id|string|EntityのID(__id)|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{2}|_{NP名}|string|オブジェクト{4}<br>Linkが結ばれている場合のみ返却される。{NP名}:NavigationPropert名|
|{4}|__deferred|object|オブジェクト{5}|
|{5}|uri|string|関係を結んでいるリソースのuri<br>テスト未実施|
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
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('{EntityID}')",
        "etag": "W/\"1-1487662179733\"",
        "type": "UserData.entity-type1"
      },
      "__id": "100-1_20101108-111352093",
      "__published": "/Date(1487662179733)/",
      "__updated": "/Date(1487662179733)/",
      "PetName": null,
      "animalId": "100-1",
      "endedAt": "",
      "episodeType": "care",
      "name": "episode",
      "outcome": "治療中",
      "startedAt": "2010-11-08"
    }
  }
}
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('{100-1_20101108-111352093}')" \
-X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

