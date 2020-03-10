---
id: 309_Update_Move_Collection
title: コレクション移動名称変更
sidebar_label: コレクション移動名称変更
---
## 概要
WebDAVコレクションの名前の変更及びWebDAVファイルの移動/名前の変更。  
※ プロパティの変更は出来ない
### 必要な権限
write

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ResourcePath}/
```
### メソッド
MOVE
### リクエストクエリ
#### 共通リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
#### WebDav 共通リクエストクエリ
なし
### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
#### 個別リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Destination|変更先|Absolute URI|○|移動/名前を変更するファイル名を指定する。|
|Overwrite|上書き|"T" or "F"|×|上書き可("T")、上書き不可("F")を指定する。(初期値は"F")|
|Depth|移動階層|"infinity"|×|移動するコレクション階層の深さを指定する。(初期値は無限)|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
### リクエストボディ
なし

## レスポンス
### ステータスコード
|コード|概要|備考|
|:--|:--|:--|
|201|Created|移動または名称変更に成功(作成)|
|204|No Content|移動または名称変更に成功(上書き)|
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Location|作成したコレクションのリソースURL|正常にコレクションが作成できた場合のみ返却する|
|ETag|リソースのバージョン情報|正常にコレクションが作成できた場合のみ返却する|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
なし
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

コレクション名変更(終端の"/"は必須)
```sh
curl "https://cell1.unit1.example/box1/collection1/" -X MOVE -i \
-H 'Destination:https://cell1.unit1.example/box1/collection2/' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```

ファイル名変更
```sh
curl "https://cell1.unit1.example/box1/collection1/file1/" -X MOVE -i \
-H 'Destination:https://cell1.unit1.example/box1/collection1/file2/' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```

ファイル移動
```sh
curl  "https://cell1.unit1.example/box1/collection1/file1/" -X MOVE -i \
-H 'Destination:https://cell1.unit1.example/box1/collection2/file1/' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```

