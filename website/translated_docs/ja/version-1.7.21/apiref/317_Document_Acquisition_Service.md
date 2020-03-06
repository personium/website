---
id: version-1.7.21-317_Document_Acquisition_Service
title: サービスドキュメント取得
sidebar_label: サービスドキュメント取得
---
## 概要
ユーザデータのスキーマ定義を行うためのODataサービスのサービスドキュメントを取得する。

### 必要な権限
read

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata
```
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
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
#### 個別リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Accept|返却されるデータの形式|application / atomsvc &#8203;&#8203;+ xml|○|指定がない場合、ユーザデータスキーマのスキーマ情報取得となる|
### リクエストボディ
なし

## レスポンス
### ステータスコード
200
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン情報||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
レスポンスサンプル参照
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```xml
<?xml version='1.0' encoding='utf-8'?>
<service xmlns="http://www.w3.org/2007/app" xml:base="https://cell1.unit1.example/box1/odata-collection1/$metadata/" xmlns:atom="http://www.w3.org/2005/Atom" 
xmlns:app="http://www.w3.org/2007/app">
  <workspace>
    <atom:title>Default </atom:title>
    <collection href="EntityType">
      <atom:title>EntityType </atom:title>
    </collection>
    <collection href="AssociationEnd">
      <atom:title>AssociationEnd </atom:title>
    </collection>
    <collection href="ComplexTypeProperty">
      <atom:title>ComplexTypeProperty </atom:title>
    </collection>
    <collection href="Property">
      <atom:title>Property </atom:title>
    </collection>
    <collection href="ComplexType">
      <atom:title>ComplexType </atom:title>
    </collection>
  </workspace>
</service>
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata' -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/atomsvc+xml'
```

