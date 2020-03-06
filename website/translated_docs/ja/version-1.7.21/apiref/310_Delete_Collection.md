---
id: version-1.7.21-310_Delete_Collection
title: コレクション削除
sidebar_label: コレクション削除
---
## 概要
コレクションを削除する

### 必要な権限
write

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{CollectionName}
```


|パス|概要|備考|
|:--|:--|:--|
|{CellName}|セル名||
|{BoxName}|ボックス名||
|{CollectionName}|コレクション名|有効値 桁数:1&#65374;256|

### メソッド
DELETE

### リクエストクエリ
共通リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|


### WebDav 共通リクエストクエリ

なし

### リクエストヘッダ
#### 共通リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-Match|対象ETag値を指定する|ETag値|×|省略時は[*]として扱う|
|X-Personium-Recursive|再帰削除の指定|文字列|×|trueの場合はコレクションの再帰削除を実施<br>falseの場合およびヘッダの指定がなかった場合は通常の削除を実施|
### リクエストボディ
なし


## レスポンス
### ステータスコード
204

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|application/json|削除に失敗した場合のみ返却する|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/collection1" -X DELETE -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

