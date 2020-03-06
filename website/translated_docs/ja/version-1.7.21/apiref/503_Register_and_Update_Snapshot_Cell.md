---
id: version-1.7.21-503_Register_and_Update_Snapshot_Cell
title: Cellスナップショットファイル登録更新
sidebar_label: Cellスナップショットファイル登録更新
---
## 概要
Cellスナップショットを登録・更新する。

### 必要な権限
root


## リクエスト
### リクエストURL
```
{CellURL}__snapshot/{FileName}
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
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-Match|対象ETag値を指定する|ETag値|×|省略時は[*]として扱う|
|Content-Type|登録・更新ファイルのコンテンツ形式を指定する|String|×|ZIP形式で登録・更新する場合<br>Content-Type:application/zip|

### リクエストボディ
|概要|有効値|必須|備考|
|:--|:--|:--|:--|
|登録・更新するコンテキスト情報をバイナリでリクエストボディに指定する|Content-Typeヘッダで指定した方式|○||


## レスポンス
### ステータスコード
|コード|メッセージ|概要|
|:--|:--|:--|
|201|Created|登録成功|
|204|No Content|更新成功|

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式|更新・作成時に失敗した場合のみ返却する|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|ETag|リソースのバージョン情報||

### レスポンスボディ
更新・作成時に失敗した場合のみ返却する

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル
```sh
curl "https://cell1.unit1.example/__snapshot/CellExport_2017_01.zip" -X PUT -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' -d '{ファイル内容}'
```
```sh
curl "https://cell1.unit1.example/__snapshot/CellExport_2017_01.zip" -X PUT -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' -T "/home/user/CellExport.zip"
```

