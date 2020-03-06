---
id: version-1.7.21-304_Get_Box_URL
title: BoxURL取得
sidebar_label: BoxURL取得
---
## 概要
BoxのURLを取得するために用いるリソースです。スキーマ認証を行ったアプリケーションはアクセストークンをつけてこのリソースにアクセスすることでスキーマ認証されたアプリケーションのためのBoxのURLにリダイレクトします。  
スキーマ認証に対応していないアプリケーションはパラメタでschema urlを与えることで、対応するBoxのURLにリダイレクトします。

### 必要な権限
以下どちらかを満たしている必要があります。
* スキーマ認証済み
* BoxルートACLのrequireSchemaAuthz属性がnone  
かつ  
利用者がBoxルートをread可能（Boxルートが全公開である場合は利用者認証不要）

※ACLのrequireSchemaAuthz属性については、[アクセス制御モデル](006_Access_Control.md)内の「スキーマ権限要求レベル」を参照。

## リクエスト
### リクエストURL
```
{CellURL}__box
```
### メソッド
GET

### リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
|schema|アプリセルURL|URL形式|×|桁数：1&#65374;1024<br>URIの形式に従う|


### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}  override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
### リクエストボディ
なし


## レスポンス
### ステータスコード

|コード|メッセージ|概要|
|:--|:--|:--|
|200|FOUND|取得成功|
### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|Location|Boxメタデータ取得API用URL|リクエストの指定方法により、以下の値となる<br>schemaクエリを指定<br>schemaクエリで指定されたアプリセルURLに対応するBoxのURL<br>schemaクエリなしで、Authorizationヘッダのみを指定<br>トークンに含まれるスキーマURLに対応するBoxのURL|
Locationサンプル
```
Location:https://cell1.unit1.example/box1
```

### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```
Location:https://cell1.unit1.example/box1
```

## cURLサンプル
### スキーマ認証済
```sh
curl "https://cell1.unit1.example/__box" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```
### スキーマ認証未対応
```sh
curl "https://cell1.unit1.example/__box?schema=https://app-cell1.unit1.example/" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

