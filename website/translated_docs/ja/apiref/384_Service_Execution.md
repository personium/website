---
id: 384_Service_Execution
title: サービス実行
sidebar_label: サービス実行
---
## 概要
登録されたサービスを実行する
### 必要な権限
exec

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{CollectionName}/{ServiceName}
```
|パス|概要|備考|
|:--|:--|:--|
|{CellName}|セル名||
|{BoxName}|Box名||
|{CollectionName}|サービスコレクション名|有効値 桁数:1&#65374;256|
|{ServiceName}|登録されたサービスの名前を指定|有効値(制限) 桁数:1&#65374;256|
### メソッド
GET / POST / PUT / DELETE
### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
### リクエストボディ
なし


## レスポンス
### ステータスコード
スクリプトが実行された場合はスクリプトのレスポンスコードが返却される
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|スクリプトに依存した形式を返却する|text/html|
### レスポンスボディ
スクリプトが実行された場合はスクリプトのレスポンスボディが返却される
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/collection1/service1" -X GET -i -H \
"Authorization:Bearer AA~PBDc...(省略)...FrTjA" -H "Accept:application/json"
```

