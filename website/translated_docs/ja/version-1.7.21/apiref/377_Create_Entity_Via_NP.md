---
id: version-1.7.21-377_Create_Entity_Via_NP
title: EntityのNavigation Property経由での他オブジェクト登録
sidebar_label: EntityのNavigation Property経由での他オブジェクト登録
---
## 概要
ユーザデータのEntityをNavigation Property経由で作成します。
### 必要な権限
write
### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない
* ユーザデータ制限事項
	- Edm.DateTime型のプロパティの有効範囲のチェックが適切に行われない
	- Edm.DateTime型の配列は未サポート
	- Edm.DateTime型のプロパティにSYSUTCDATETIME()を指定した場合、設定されるシステム時間が異なる場合がある
      - リクエストボディでの設定時とDefaultValueでの設定時（\__published、\__updatedは後者のタイミング）
	- 1つのEntityTypeに対して作成出来るのは、DynamicProperty・DeclaredProperty・ComplexTypeProperty合わせて400個まで


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}('{EntityID}')
/{NavigationPropertyName}
```
|パス|概要|
|:--|:--|
|{CellName}|セル名|
|{BoxName}|ボックス名|
|{ODataCollecitonName}|コレクション名|
|{EntityTypeName}|EntityType名|
|{EntityID}|EntityのID|
|{NavigationPropertyName}|NavigationProperty名|
指定できるNavigationProperty名は、EntitySetと以下の関連を持つものに限る。  

|From|To|
|:--|:--|
|0 .. 1|1|
|0 .. 1|*|
|1|1|
|1|*|
|*|*|
### メソッド
POST

### リクエストクエリ
#### 共通リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン<br>テスト未実施|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う<br>未対応|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う<br>未対応|
### リクエストボディ
|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|__id|EntityのID|桁数：1&#65374;400<br>文字列|×|指定しない場合ユニークなIDが割り当てられます|
* \__id以外に動的なユーザデータを登録することが可能
	- 文字列のみ設定可能
	- 数値、真偽値、nullを指定した場合は、文字列として扱われる
	- Hash値の指定は不可
	- 最大で400個のユーザデータを指定可能
	- \_published、\_updatedは、予約語であるためリクエストボディの指定は不可

### リクエストサンプル
```JSON
{"__id": "100-1_20101108-111352093","animalId": "100-1","name": "episode","startedAt":
"2010-11-08","episodeType": "care","endedAt": "","outcome": "治療中"}
```


## レスポンス
### ステータスコード
201
### レスポンスヘッダ
|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|Location|作成したEntityのリソースURL|正常にEntityが作成できた場合のみ返却する|
|DataServiceVersion|ODataのバージョン情報|正常にEntityが作成できた場合のみ返却する|
|ETag|リソースのバージョン情報|正常にEntityが作成できた場合のみ返却する|
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
|{5}|uri|string|関係を結んでいるリソースのuri<br>テスト未実施|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

上記以外にスキーマ設定した項目、または登録時に指定した動的な項目を返却
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')",
        "etag": "W/\"1-1487929403469\"",
        "type": "UserData.entity-type1"
      },
      "__id": "100-1_20101108-111352093",
      "__published": "/Date(1487929403469)/",
      "__updated": "/Date(1487929403469)/",
      "PetName": null,
      "navigation-property1": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')/navigation-property1"
        }
      }
    }
  }
}
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('{100-1_20101108-111352093}')\
/navigation-property1" -X POST -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H \
'Accept: application/json' -d '{"__id": "100-1_20101108-111352093"}'

```
