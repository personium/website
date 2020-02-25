---
id: version-1.7.18-373_Link_User_Data
title: Entityと他オブジェクトとのリンク
sidebar_label: Entityと他オブジェクトとのリンク
---
## 概要
ユーザデータのEntityに$linksで指定したODataリソースを紐付ける  
以下のODataリソースと紐付けることができる  
* ユーザデータ

### 必要な権限
No
### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない

### ユーザデータ制限事項
* Edm.DateTime型のプロパティの有効範囲のチェックが適切に行われない
* Edm.DateTime型の配列は未サポート
* Edm.DateTime型のプロパティにSYSUTCDATETIME()を指定した場合、設定されるシステム時間が異なる場合がある
* リクエストボディでの設定時とDefaultValueでの設定時（\__published、\__updatedは後者のタイミング）
* 1つのEntityTypeに対して作成出来るのは、DynamicProperty・DeclaredProperty・ComplexTypeProperty合わせて400個まで


## リクエスト
### リクエストURL
ユーザデータとの$links
```
{CellURL}{BoxName}/{CollectionName}/{EntityTypeName}('{EntityID}')/$links/_{EntityTypeName}
```
### メソッド
POST
### リクエストクエリ
#### 共通リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
#### OData 共通リクエストクエリ
なし
### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
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
{"uri":"https://cell1.unit1.example/box1/odata-collection1/entity-type1('{100-1_20101108-111352093}')"}

```


## レスポンス
### ステータスコード
204
### レスポンスヘッダ
#### 共通レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

#### OData $links レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|DataServiceVersion|ODataのバージョン||
### レスポンスボディ
なし
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('{100-1_20101108-111352093}')\
/\$links/_entity-type1" -X POST -i -H 'Authorization: Bearer {AA~PBDc...(省略)...FrTjA}' -H \
'Accept: application/json' -d "{\"uri\":\"https://cell1.unit1.example/box1/odata-collection1\
/entity-type1('{100-1_20101108-111352093}')\"}"
```

