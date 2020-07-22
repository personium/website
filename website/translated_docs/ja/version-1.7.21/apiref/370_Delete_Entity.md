---
id: version-1.7.21-370_Delete_Entity
title: Entity削除
sidebar_label: Entity削除
---
## 概要
ユーザデータのEntityを一件削除します。
### 必要な権限
write
### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない
* ユーザデータ制限事項
	- Edm.DateTime型のプロパティの有効範囲のチェックが適切に行われない
	- Edm.DateTime型の配列は未サポート
	- Edm.DateTime型のプロパティにSYSUTCDATETIME()を指定した場合、設定されるシステム時間が異なる場合がある
      - リクエストボディでの設定時とDefaultValueでの設定時（\__published、\__updatedは後者のタイミング）
	- 1つのEntityTypeに対して作成出来るのは、DynamicProperty・DeclaredProperty・ComplexTypeProperty合わせて400個まで


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}({EntityID})}
```
|パス|概要|
|:--|:--|
|{CellName}|Cell名|
|{BoxName}|Box名|
|{ODataCollecitonName}|コレクション名|
|{EntityTypeName}|EntityType名|
|{EntityID}|削除するEntityのID|
### メソッド
DELETE
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
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
#### OData共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
#### OData削除リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|If-Match|対象ETag値を指定する|ETag値|×|省略時は[*]として扱う|
### リクエストボディ
なし


## レスポンス
### ステータスコード
204
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式|Entityの削除に失敗した場合のみ返却する|
|DataServiceVersion|ODataのバージョン情報|正常にEntityが削除できた場合のみ返却する|
### レスポンスボディ
なし  
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('100-1_20101108-111352093')" \
-X DELETE -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

