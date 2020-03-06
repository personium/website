---
id: version-1.7.21-323_Link_AssociationEnd
title: AssociationEndと他オブジェクトとのリンク
sidebar_label: AssociationEndと他オブジェクトとのリンク
---
## 概要
ユーザデータスキーマのAssociationEndのリンク情報を登録する  

### 必要な権限
alter-schema


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata/AssociationEnd(Name='{AssociationEndName}',
_EntityType.Name='{EntityTypeName}')/$links/_AssociationEnd
```
### メソッド
POST

### リクエストクエリ
特になし

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### リクエストボディ

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|uri|linkするAssociationEndのuri|存在するAssociationEnd|○||
### リクエストサンプル
```JSON
{"uri": "https://cell1.unit1.example/box1/odata-collection2/$metadata/AssociationEnd
(Name='association-end2',_EntityType.Name='entity-type2')"}
```

## レスポンス
### ステータスコード
204
### レスポンスヘッダ
|項目名|概要|備考|
|:--|:--|:--|
|DataServiceVersion|ODataProtocolのバージョン情報|正常にAssociationEndが作成できた場合のみ返却する|
### レスポンスボディ
特になし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/AssociationEnd\
(Name='association-end1',_EntityType.Name='entity-type1')/\$links/_AssociationEnd" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d "{\"uri\": \"https://cell1.unit1.example/box1/odata-collection2/\$metadata/AssociationEnd\
(Name='association-end2',_EntityType.Name='entity-type2')\"}"
```

