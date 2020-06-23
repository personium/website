---
id: 381_Create_Service_Collection_Source
title: サービスコレクションソース作成
sidebar_label: サービスコレクションソース作成
---
## 概要
サービスソース情報を登録・更新する
### 必要な権限
write

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{CollectionName}/__src/{ResourceName}
```
|パス|概要|備考|
|:--|:--|:--|
|{CellName}|Cell名||
|{BoxName}|Box名||
|{CollectionName}|サービスコレクション名|有効値 桁数:1&#65374;256|
|{ResourceName}|リソース名|有効値(制限) 桁数:1&#65374;256|
### メソッド
PUT
### リクエストクエリ
#### 共通リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
#### 個別リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-Match|対象ETag値を指定する|String|×|省略時は[*]として扱う|
|Content-Type|登録・更新ファイルのコンテンツ形式を指定する|String|○|JSでのリソースを形式で登録・更新する場合<br>Content-Type:text/javascript|
### リクエストボディ
|概要|有効値|必須|備考|
|:--|:--|:--|:--|
|登録・更新するコンテキスト情報をバイナリでリクエストボディに指定する|Content-Typeヘッダで指定した形式|○||


## レスポンス
### ステータスコード
|コード|メッセージ|概要|
|:--|:--|:--|
|201|Created|登録成功時|
|204|No Content|更新成功時|
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式|更新・作成に失敗した場合のみ返却する|
|ETag|リソースのバージョン情報||
### レスポンスボディ
なし
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/collection1/__src/{ResourceName}" -X PUT -i  -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' -H \
'Content-Type:text/javascript' -d '【ファイル内容】'
```

