---
id: 332_Register_ComplexType_links
title: ComplexTypeと他オブジェクトとのリンク
sidebar_label: ComplexTypeと他オブジェクトとのリンク
---
## 概要
ComplexTypeに$linkで指定したODataリソースを紐付ける  
以下のODataリソースと紐付けることができる  
* Property

### 必要な権限
alter-schema

### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
```
Propertyとの$links
{CellURL}{BoxName}/{CollectionName}/$metadata/ComplexType('{ComplextypeName}')/$links/_Property
```
### メソッド
POST

### リクエストクエリ

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
#### OData共通リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
#### OData登録リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
#### Format
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|uri|紐付けるODataリソースのURI|桁数：1&#65374;1024<br>URIの形式に従う<br>scheme：http / https / urn|○||

### リクエストサンプル
```JSON
{"uri":"https://cell1.unit1.example/box1/odata-collection1/$metadata/AssociationEnd\
(Name='association-end1',_EntityType.Name=null)"}
```


## レスポンス
### ステータスコード
204
### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|


|ヘッダ名|概要|備考|
|:--|:--|:--|
|DataServiceVersion|ODataのバージョン||
|ETag|リソースのバージョン情報||

### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル
 EntityType
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/$metadata/EntityType\
(Name='entit-type1')/$links/_AssociationEnd" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '{"uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/AssociationEnd\
(Name="association-end1",_EntityType.Name=null)"}'
```
 AssociationEnd
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/$metadata/AssociationEnd\
(Name='association-end1',_EntityType.Name=entity-type1)/$links/_AssociationEnd" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '{"uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/AssociationEnd\
(Name="association-end2",_EntityType.Name=entity-type2)"}'
```

