---
id: version-1.7.18-504_Get_Snapshot_Cell
title: Cellスナップショットファイル取得
sidebar_label: Cellスナップショットファイル取得
---
## 概要
Cellスナップショットファイルを取得する。  
If-None-Matchヘッダに指定されたETag値によって、返却される内容が異なる。  

### 必要な権限
root


## リクエスト
### リクエストURL
```
{CellURL}__snapshot/{FileName}
```
### メソッド
GET

### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きする。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-None-Match|ETagの値を指定する|String<br>以下のフォーマットでETag値を指定する<br>"*"または、"{半角数字}-{半角数字}"|×|例）ETag値「1-1372742704414」を指定する場合<br>"1-1372742704414"|

### リクエストボディ
なし


## レスポンス
### ステータスコード
- リクエストでIf-None-Matchヘッダが指定されていない場合、またはリクエストでIf-None-MatchヘッダのETag値がWebDavに保存されているリソースのETagと一致しない場合<br>（指定されたETag値のフォーマットが不正な場合を含む）

|コード|メッセージ|概要|
|:--|:--|:--|
|200|OK|取得成功|

- リクエストでIf-None-MatchヘッダのETag値がWebDavに保存されているリソースのETagと一致する場合

|コード|メッセージ|概要|
|:--|:--|:--|
|304|Not Modified|ドキュメントが更新されていない|

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|リソースのContent-Type|ステータスコード200の場合のみ返却する|
|ETag|リソースのバージョン情報||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
ファイルの内容を返却する  
ただし、ステータスコードが304の場合はレスポンスボディを返却しない

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル
```sh
curl "https://cell1.unit1.example/__snapshot/snapshot-file1" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```

