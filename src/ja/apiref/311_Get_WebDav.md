---
id: 311_Get_WebDav
title: ファイル取得
sidebar_label: ファイル取得
---
## 概要
特定のWebDav情報を取得する  
If-None-Matchヘッダに指定されたETag値によって、返却される内容が異なる  
Rangeヘッダで範囲指定した場合、指定した範囲の内容を返却する
### 必要な権限
read

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ResourcePath}
```
|パス|概要|備考|
|:--|:--|:--|
|{CellName}|セル名||
|{BoxName}|ボックス名||
|{ResourcePath}|リソースへのパス|有効値 桁数:1&#65374;256|
### メソッド
GET
### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
#### 個別リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-None-Match|ETagの値を指定する|String<br>以下のフォーマットでETag値を指定する<br>&quot;*&quot;<br>または、<br>"{半角数字}-{半角数字}"|×|例）ETag値「1-1372742704414」を指定する場合<br>　　"1-1372742704414"|
|Range|リソースの一部を取得する際に範囲を指定する|・データ型：String<br>【前提】<br>範囲指定の開始値は0スタート。取得ファイルのサイズがZ(byte)の場合、終端はZ-1(byte)<br>1.&quot;Range: bytes={半角数字}-{半角数字}&quot;<br>ex) &quot;Range: bytes=10-20&quot;<br>2.&quot;Range: bytes={半角数字}-&quot;<br>→範囲の開始値から取得ファイルの最後まで<br>ex) &quot;Range: bytes=10-&quot;<br>3.&quot;Range: bytes=-{半角数字}&quot;<br>→リソースの終端から指定した分を取得<br>ex) "Range: bytes=-20"|×|・開始値は取得ファイルのサイズより小さい値を指定<br>・指定されたRangeヘッダのフォーマットが不正な場合はRangeヘッダは無視される<br>【制限事項】<br>・マルチパートレスポンスには未対応|
### リクエストボディ
なし


## レスポンス
### ステータスコード
* リクエストでIf-None-Matchヘッダが指定されていない場合、またはリクエストでIf-None-MatchヘッダのETag値がWebDavに保存されているリソースのETagと一致しない場合<br>（指定されたETag値のフォーマットが不正な場合を含む）
* リクエストでRangeヘッダが指定されていない場合、またはリクエストでRangeヘッダで指定される開始値が終端値よりも大きい場合

|コード|メッセージ|概要|
|:--|:--|:--|
|200|OK|取得成功時|
* リクエストのRangeヘッダで有効である場合

|コード|メッセージ|概要|
|:--|:--|:--|
|206|Partial Content|部分取得成功時|
* リクエストでIf-None-MatchヘッダのETag値がWebDavに保存されているリソースのETagと一致する場合

|コード|メッセージ|概要|
|:--|:--|:--|
|304|Not Modified|ドキュメントが更新されていない|
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|リソースのContent-Type|PUT時に指定したContent-Typeが返ります。|
|ETag|リソースのバージョン情報||
|Accept-Ranges|リソースへのバイトレンジ(範囲)リクエストの受け入れを示す||
|Content-Range|バイトレンジリクエストで指定した分がエンティティボディ全体のうちどこに当たるものかを示す||
Basic認証エラーの場合は 400 + WWW-Authenticated:Basicヘッダを返却する
### レスポンスボディ
ファイルの内容を返却する  
ただし、ステータスコードが304の場合はレスポンスボディを返却しない  
また、ステータスコードが206の場合はRangeヘッダで指定した範囲のファイルの内容を返却する
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/{ResourcePath}" -X GET -i \
-H 'If-None-Match:"1-1372742704414"' -H 'Range:bytes=10-20' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

