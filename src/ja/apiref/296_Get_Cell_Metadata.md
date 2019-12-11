# Cellメタデータ取得
## 概要
Cellのメタデータを取得する。メタデータには、以下の情報が含まれる。  
* Cellの名前
* CellのURL
* [Unitメタデータ](107_Get_Unit_Metadata.md)

### 必要な権限
なし


## リクエスト
### リクエストURL
```
{CellURL}
```

### メソッド
GET

### リクエストクエリ
なし

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Accept|レスポンスボディの形式を指定する|application/json|○||


## レスポンス
### ステータスコード
200

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|Personium APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
レスポンスはJSON形式で、オブジェクト（サブオブジェクト）に定義される。  
キー(名前)と型、並びに値の対応は以下のとおり。  

|オブジェクト|名前(キー)|型|値|備考|
|:--|:--|:--|:--|:--|
|ルート|cell|object|Object (cell format)||
|cell|name|string|Cellの名前||
|cell|url|string|CellのURL||
|ルート|unit|object|Object (unit format)||
|unit|url|string|UnitのURL||
|unit|path_based_cellurl_enabled|boolean|true:path based cell url<br>false:per cell fqdn url||

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "cell": {
    "name": "cell1",
    "url": "https://cell1.unit1.example/"
  },
  "unit": {
    "url": "https://unit1.example/",
    "path_based_cellurl_enabled": true
  }
}
```

## cURLサンプル

```sh
curl "https://cell1.unit1.example/" -X GET -i -H 'Accept: application/json'
```
