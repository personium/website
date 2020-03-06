---
id: version-1.7.21-244_List_Obj_Via_Relation_NP
title: RelationのNavigation Property経由での他オブジェクト一覧取得
sidebar_label: RelationのNavigation Property経由での他オブジェクト一覧取得
---
## 概要
セル制御オブジェクトをNavigation Property経由で取得する

### 必要な権限
* Roleを取得する場合  
auth-read
* Relationを取得する場合  
social-read

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションは無視される


## リクエスト
### リクエストURL
#### BoxへのnavigationProperty
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/_Box
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/_Box
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/_Box
```
#### ExtCellへのnavigationProperty
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/_ExtCell
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/_ExtCell
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/_ExtCell
```
#### ExtRoleへのnavigationProperty
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/_ExtRole
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/_ExtRole
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/_ExtRole
```
#### RoleへのnavigationProperty
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/_Role
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/_Role
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/_Role
```
※ \_Box.Nameパラメタを省略した場合は、nullが指定されたものとする  

### メソッド
GET

### リクエストクエリ
以下のクエリパラメタが利用可能です。

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|_

[$select クエリ](406_Select_Query.md)

[$expand クエリ](405_Expand_Query.md)

[$format クエリ](404_Format_Query.md)

[$filter クエリ](403_Filter_Query.md)

[$inlinecount クエリ](407_Inlinecount_Query.md)

[$orderby クエリ](400_Orderby_Query.md)

[$top クエリ](401_Top_Query.md)

[$skip クエリ](402_Skip_Query.md)

[全文検索(q)クエリ](408_Full_Text_Search_Query.md)

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値};override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
なし


## レスポンス
### ステータスコード
200

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン||
### レスポンスボディ

|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|etag|string|Etag値|
|{3}|uri|string|作成したリソースへのURL|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

#### Relationを取得した場合

|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.Relation|
|{3}|Name|string|Relation名|
|{2}|_Box.Name|string|関係対象のBox名|

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": {
      "Name": "relation1",
      "_Box.Name": "box1",
      "__metadata": {  
        "uri": "https://cell1.unit1.example/__ctl/Relation(Name='relation1'
,_Box.Name='box1')",
        "type": "CellCtl.relation"  
      },  
      "__published" : "\/Date(1339128525502)\/",  
      "__updated"   : "\/Date(1339128525502)\/"  
    }
  }
}
```


## cURLサンプル
なし

