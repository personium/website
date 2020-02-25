---
id: version-1.7.18-103_Update_Cell
title: Cell更新
sidebar_label: Cell更新
---
## 概要
既存のCell情報を更新する

### 必要な権限
ユニットユーザのみ可能

### 制限事項
* OData制限
	- リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
	- リクエストボディはJSON形式のみ受け付ける
	- レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
	- $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
```
{UnitURL}__ctl/Cell(Name='{CellName}')
```
または、
```
{UnitURL}__ctl/Cell('{CellName}')
```

### メソッド
PUT
### リクエストクエリ
なし
### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|If-Match|対象ETag値を指定する|ETag値|×|省略時は[*]として扱う|
### リクエストボディ
#### Format
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Name|Cell名|桁数：1&#65374;128<br>文字種:半角英小文字と半角数字と-(半角ハイフン)<br>ただし、先頭文字に-(半角ハイフン)は指定不可|○||

### リクエストサンプル
```JSON
{"Name":"cell2"}
```


## レスポンス
### ステータスコード
204
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|ETag|リソースのバージョン情報||
|DataServiceVersion|ODataのバージョン||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|Personium APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ
なし
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://unit1.example/__ctl/Cell(Name='cell1')" -X PUT -i -H \
'Authorization: Bearer PEFzc2V...(省略)...lvbj4' -H 'Accept: application/json' -d '{"Name":"cell2"}'
```

