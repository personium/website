---
id: version-1.7.21-364_Create_Entity
title: Entity作成
sidebar_label: Entity作成
---
## 概要
ユーザデータのEntityを作成します。
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
       - ※リクエストボディでの設定時とDefaultValueでの設定時（\__published、\__updatedは後者のタイミング）
	- 1つのEntityTypeに対して作成出来るのは、DynamicProperty・DeclaredProperty・ComplexTypeProperty合わせて400個まで


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}
```
|パス|概要|
|:--|:--|
|{CellName}|セル名|
|{BoxName}|ボックス名|
|{ODataCollecitonName}|コレクション名|
|{EntityTypeName}|EntityType名|
### メソッド
POST
### リクエストクエリ
#### 共通リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
#### OData 共通リクエストクエリ
なし
### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う<br>未対応|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う <br>未対応|
### リクエストボディ
|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|__id|EntityのID|桁数：1&#65374;400<br>文字列|×|指定しない場合ユニークなIDが割り当てられます|
#### プロパティ
スキーマ定義済みのプロパティと動的（スキーマ未定義）プロパティ、合わせて最大で400個のプロパティを設定可能  
上記にはComplexTypeで定義されているプロパティ数を含む
#### スキーマ定義済みのプロパティ
|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|EntityTypeに紐づくProperty|ユーザ定義項目|デフォルト値 PropertyのDefaultValueに基づく|PropertyのNullableに基づく||
#### スキーマ定義済みプロパティのvalueの有効値  
|データ型|有効値|
|:--|:--|
|文字列|桁数：0&#65374;51200 byte<br>文字種: 文字列の値に制御コードを使用した場合、取得時にエスケープした状態で返却する<br>「\」を使用する場合、「\\\」で指定する必要がある<br>文字列型のプロパティに整数値、小数値、真偽値、日付型の値を設定した場合、文字列型に変換して登録される|
|整数値|-2147483648 &#65374; 2147483647|
|小数値|整数部分の桁数：1&#65374;5桁<br>小数部分の桁数：1&#65374;5桁|
|真偽値|true / false / null(nullを指定した場合はfalseとして扱う)|
|日付|/Date(【long型の時刻】)/の形式で文字列で指定する<br>【long型の時刻】の有効値は、-6847804800000(1753-01-01T00:00:00.000Z)&#65374;253402300799999(9999-12-31T23:59:59.999Z)<br>また、予約語として以下を指定可能<br>SYSUTCDATETIME()：サーバ時間|
### 動的（スキーマ未定義）プロパティ
スキーマ定義済みのプロパティと動的（スキーマ未定義）プロパティ、合わせて最大で400個のプロパティを設定可能  
上記にはComplexTypeで定義されているプロパティ数を含む
#### 動的プロパティのkeyの有効値
|データ型|有効値|
|:--|:--|
|文字列|桁数：1&#65374;128 :<br>文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)<br>_ただし、先頭文字に-(半角ハイフン)と_(半角アンダーバー)は指定不可  <br>_published、_updatedは、予約語であるためリクエストボディの指定は不可|
#### 動的プロパティのvalueの有効値
スキーマ定義済みプロパティのvalueの有効値と同様  
配列、連想配列は指定不可
### リクエストサンプル
```JSON
{"__id": "100-1_20101108-111352093","animalId": "100-1","name": "episode","startedAt": "2010-11-08",
"episodeType": "care","endedAt": "","outcome": "治療中"}
```
```JSON
{"__id": "100-1_20101108-111352093","animalId": "100-1","name": "episode","update":
"SYSUTCDATETIME()"}
```
```JSON
{"__id": "100-1_20101108-111352093","animalId": "100-1","name": "episode","update":
"\/Date(1350451322147)\/"}
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
#### 共通レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおりです。

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
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

上記以外に登録時に指定した動的なユーザデータを返却
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照  

### レスポンスサンプル
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/collection1/entity-type1
('100-1_20101108-111352093')",
        "etag": "W/\"1-1487662179733\"",
        "type": "UserData.entity-type1"
      },
      "__id": "100-1_20101108-111352093",
      "__published": "/Date(1487662179733)/",
      "__updated": "/Date(1487662179733)/",
      "PetName": null,
      "animalId": "100-1",
      "name": "episode",
      "startedAt": "2010-11-08",
      "episodeType": "care",
      "endedAt": "",
      "outcome": "治療中"
    }
  }
}
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1" -X POST -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' -d '{"__id": "100-1_20101108-111352093",\
"animalId": "100-1","name": "episode","startedAt": "2010-11-08","episodeType": "care","endedAt": \
"","outcome": "治療中"}'
```
