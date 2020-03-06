---
id: version-1.7.21-247_Retrieve_External_Role
title: ExtRole取得
sidebar_label: ExtRole取得
---
## 概要
既存のExtRole情報を取得する
### 必要な権限
social
### 制限事項
* OData 制限
	* リクエストヘッダのAcceptは無視される
	* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
	* リクエストボディはJSON形式のみ受け付ける
	* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
	* $formatクエリオプションは無視される

### 必要な権限
auth-read


## リクエスト
### リクエストURL
```
{CellURL}__ctl/ExtRole(ExtRole='https%3A%2F%2F{CellName}.{UnitFQDN}%2F__role%2F__%2F{RoleName}',
_Relation.Name='{RelationName}',_Relation._Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/ExtRole(ExtRole='https%3A%2F%2F{CellName}.{UnitFQDN}%2F__role%2F__%2F{RoleName}',
_Relation.Name='{RelationName}')
```
※ \_Relation.\_Box.Nameパラメタを省略した場合は、nullが指定されたものとする

### メソッド
GET
### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

[$select クエリ](406_Select_Query.md)

[$expand クエリ](405_Expand_Query.md)

[$format クエリ](404_Format_Query.md)

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|


## レスポンス
### ステータスコード
200
### レスポンスボディ
#### 共通レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおりです。

|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

#### ExtRole固有レスポンスボディ
|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ExtRole|
|{2}|ExtRole|string|外部ロールURL|
|{2}|_Relation.Name|string|Relation名|
|{2}|_Relation._Box.Name|string|Relationに紐付くBox名|
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/ExtRole(ExtRole='https%3A%2F%2Fcell1.unit1.example
%2F__role%2F__%2Frole1',_Relation.Name='relation1',_Relation._Box.Name='box1')",
        "etag": "W/\"1-1486717404966\"",
        "type": "CellCtl.ExtRole"
      },
      "ExtRole": "https://cell1.unit1.example/__role/__/role1",
      "_Relation.Name": "relation1",
      "_Relation._Box.Name": "box1",
      "__published": "/Date(1486717404966)/",
      "__updated": "/Date(1486717404966)/",
      "_Role": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/__ctl/ExtRole(ExtRole='https%3A%2F%2Fcell1.unit1.example
%2F__role%2F__%2Frole1',_Relation.Name='relation1',_Relation._Box.Name='box1')/_Role"
        }
      },
      "_Relation": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/__ctl/ExtRole(ExtRole='https%3A%2F%2Fcell1.unit1.example
%2F__role%2F__%2Frole1',_Relation.Name='relation1',_Relation._Box.Name='box1')/_Relation"
        }
      }
    }
  }
}
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/ExtRole\
(ExtRole='https%3A%2F%2Fcell2.unit1.example%2F__role%2F__%2Frole1',_Relation.Name='relation1'\
,_Relation._Box.Name='box1')" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json'
```
