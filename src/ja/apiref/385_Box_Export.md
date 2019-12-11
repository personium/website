---
id: 385_Box_Export
title: Boxエクスポート
sidebar_label: Boxエクスポート
---
## 概要
指定されたBoxをbarファイル形式でエクスポートする。barファイルフォーマットについては 「[barファイル](301_Bar_File.md)」を参照。  

### 必要な権限
read  
read-acl  

### 制限事項
#### 未対応の項目
- 30_extroles.json, 70_$links.jsonのエクスポート
- 10_odatarelations.jsonのエクスポート
- 90_data以下のエクスポート
- MainBoxのエクスポート

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}
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
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}  override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/zip+x-personium-bar|○||

### リクエストボディ
なし  

## レスポンス
### ステータスコード
|コード|メッセージ|概要|備考|
|:--|:--|:--|:--|
|200|OK|エクスポート成功時||

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|ファイルのContent-Type|application/zip+x-personium-bar|
|Content-Length|ファイルのContent-Length||

### レスポンスボディ
ファイルの内容をバイナリで返却する  

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照  

### レスポンスサンプル
なし  

## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1" -X GET -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/zip+x-personium-bar' -o "/home/user/export.bar"
```
