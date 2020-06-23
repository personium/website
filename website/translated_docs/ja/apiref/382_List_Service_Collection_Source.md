---
id: 382_List_Service_Collection_Source
title: サービスコレクションソース取得
sidebar_label: サービスコレクションソース取得
---
## 概要
サービスソース情報を取得する
### 必要な権限
read

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
GET
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
#### サービスコレクションソース取得固有リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-None-Match|ETagの値を指定し、変更がない場合は304、変更されている場合は最新リソースを返却する|String|×||
### リクエストボディ
なし


## レスポンス
### ステータスコード
200
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|ResourceのContent-Type||
|ETag|リソースのバージョン情報||
### レスポンスボディ
ファイルの内容を返却する
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/collection1/__src/{ResourceName}" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

