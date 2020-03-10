---
id: 220_Unlink_Account
title: Accountと他オブジェクトとのリンク解除
sidebar_label: Accountと他オブジェクトとのリンク解除
---
## 概要
Accountとの$links情報を削除する

### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
Roleとの紐付け
```
{CellURL}__ctl/Account(Name='{AccountName}')/$links/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Account(Name='{AccountName}')/$links/_Role(Name='{RoleName}')
```
または、
```
{CellURL}__ctl/Account(Name='{AccountName}')/$links/_Role('{RoleName}')
```
または、
```
{CellURL}__ctl/Account('{AccountName}')/$links/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Account('{AccountName}')/$links/_Role(Name='{RoleName}')
```
または、
```
{CellURL}__ctl/Account('{AccountName}')/$links/_Role('{RoleName}')
```

### メソッド
DELETE

### リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
&#160;

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-Match|対象ETag値を指定する|ETag値|×||
### リクエストボディ
なし

## レスポンス
### ステータスコード
204

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|DataServiceVersion|ODataのバージョン||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Account('account1')/\$links/_Role('role1')" -X DELETE -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

