---
id: 230_Update_External_Cell_links
title: Extcell_$links更新
sidebar_label: Extcell_$links更新
---
## 概要
Extcellに紐付いたODataリソースを更新する<br>以下のODataリソースを指定することができる

* Box
* ExtCell
* ExtRole
* Role

### 制限事項
* OData制限
	- リクエストヘッダのAcceptは無視される
	- リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
	- リクエストボディはJSON形式のみ受け付ける
	- レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
	- $formatクエリオプションは無視される


## リクエスト
### リクエストURL
#### ExtCellとの$links
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/
_ExtCell('{ExtCellURL}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtCell('{ExtCellURL}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtCell('{ExtCellURL}')
```
### メソッド
PUT

### リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値} &#160;override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Contents-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|If-Match|対象ETag値を指定する|ETag値|×|省略時は[*]として扱う|
### リクエストボディ
### 形式
JSON

### 説明

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Url|CellへのURL|桁数：1&#65374;1024<br>URIの形式に従う<br>scheme：http, https<br>トレイリングスラッシュ(URL終端の/)必須|○||
### リクエストサンプル
```JSON
{"uri":"https://cell1.unit1.example/__ctl/Box('box3')"}
```

## レスポンス
### ステータスコード
204

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン||
### ODataレスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|DataServiceVersion|ODataのバージョン||
|ETag|リソースのバージョン情報||
### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
なし


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Relation(Name='relation1',_Box.Name='box1')\
/$links/_Box('box2')" -X PUT -i -H 'If-Match:*' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '{"uri":"https://cell1.unit1.example/\__ctl/Box('box3')"}'
```

