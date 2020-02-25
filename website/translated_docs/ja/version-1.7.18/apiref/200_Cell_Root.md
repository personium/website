---
id: version-1.7.18-200_Cell_Root
title: Cellルート取得
sidebar_label: Cellルート取得
---
## 概要
Cellルートとして設定されているHTMLファイルを取得する。

### 前提条件
[Unitの設定](../../server-operator/unit_config_list.md)または[対象Cellのプロパティ設定](./291_Cell_Change_Property.md)が必要。2つを同時に設定した場合、対象Cellのプロパティ設定が優先される。  

Unitの設定  
```
io.personium.core.cell.relayhtmlurl.default={htmlが取得可能なURL}
```

対象Cellのプロパティ設定  
```xml
<p:relayhtmlurl>{htmlが取得可能なURL}</p:relayhtmlurl>
```
URLに指定可能なスキームは"http", "https", "personium-localunit", "personium-localcell"。

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
|Accept|レスポンスボディの形式を指定する|text/html|×|省略時は[text/html]として扱う|


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
対象Cellのプロパティに設定されているURLから取得したHTML。

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/" -X GET -i -H 'Accept: text/html'
```
