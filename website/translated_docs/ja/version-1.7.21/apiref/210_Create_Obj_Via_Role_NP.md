---
id: version-1.7.21-210_Create_Obj_Via_Role_NP
title: RoleのNavigation Property経由での他オブジェクト登録
sidebar_label: RoleのNavigation Property経由での他オブジェクト登録
---
## 概要

RoleのNavigation Property経由での他のCell制御オブジェクトを登録します。これにより最初からリンクされた形でオブジェクト登録が可能です。

### 必要な権限
write

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションは無視される


## リクエスト
### リクエストURL
#### AccountへのnavigationProperty
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/_Account
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/_Account
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/_Account
```
#### ExtCellへのnavigationProperty
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/_ExtCell
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/_ExtCell
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/_ExtCell
```
#### ExtRoleへのnavigationProperty
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/_ExtRole
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/_ExtRole
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/_ExtRole
```
#### RelationへのnavigationProperty
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/_Relation
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/_Relation
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/_Relation
```
※ \_Box.Nameパラメタを省略した場合は、nullが指定されたものとする
### メソッド
POST
### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
#### Roleを登録する場合
|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Name|Role名|桁数：1&#65374;128<br>文字種:半角英数字と-(半角ハイフン と_(半角アンダーバー)<br>ただし、先頭文字に-(半角ハイフン)と_(半角アンダーバー)は指定不可|○||
|_Box.Name|関係対象のBox名|桁数：1&#65374;128<br>文字種：半角英数字と-(半角ハイフン)と_(半角アンダーバー)<br>ただし、先頭文字に-(半角ハイフン)と_(半角アンダーバー)は指定不可<br>説明：Box登録APIにて登録済みのBoxのNameを指定<br>特定のBoxと関連付けない場合はnullを指定|×||
### リクエストサンプル
```JSON
{
  "Name": "role1",
  "_Box.Name": "box1"
}
```


## レスポンス
### ステータスコード
201
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|Location|作成したリソースへのURL||
|DataServiceVersion|ODataのバージョン||
|ETag|リソースのバージョン情報||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ
|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

#### Roleを登録した場合
|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.Role|
|{2}|Name|string|Role名|
|{2}|_Box.Name|string|関係対象のBox名|
### レスポンスサンプル
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1',_Box.Name='box1')",
        "etag": "W/\"1-1486515294719\"",
        "type": "CellCtl.Role"
      },
      "Name": "role1",
      "__published": "/Date(1486515294719)/",
      "__updated": "/Date(1486515294719)/",
      "_Box.Name": "box1"
    }
  }
}
```
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

#### RelationのnavigationProperty経由登録
```sh
curl "https://cell1.unit1.example/__ctl/Role('role1')/_Relation" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json' -d '{"Name":"relation1"}'
```

