# ExtCellのNavigation Property経由での他オブジェクト一覧取得
## 概要
セル制御オブジェクトをNavigation Property経由で取得する

### 必要な権限
* 取得するセル制御オブジェクトと経由するセル制御オブジェクト双方の参照権限
* 例） Role経由でRelationを取得する場合  
auth-readとsocial-read

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションは無視される


## リクエスト
### リクエストURL
#### RoleへのnavigationProperty
```
{CellURL}__ctl/ExtCell(Url='https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Role
```
または、
```
{CellURL}__ctl/ExtCell('https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Role
```
#### RelationへのnavigationProperty
```
{CellURL}__ctl/ExtCell(Url='https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Relation
```
または、
```
{CellURL}__ctl/ExtCell('https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Relation
```
※{ExtCellURL}についてはURLエンコードが必要

### メソッド
GET

### リクエストクエリ
以下のクエリパラメタが利用可能です。

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

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
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
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
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ

|オブジェクト|Item Name|Data Type|Remarks|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

#### ExtCellを取得した場合

|オブジェクト|Item Name|Data Type|Remarks|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ExtRole|
|{2}|Name|string|関係対象のRole名|
|{2}|_Box.Name|string|関係対象のBox名|
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1',_Box.Name='box1')",
          "etag": "W/\"1-1487320623218\"",
          "type": "CellCtl.Role"
        },
        "Name": "role1",
        "_Box.Name": "box1",
        "__published": "/Date(1487320623218)/",
        "__updated": "/Date(1487320623218)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_Box"
          }
        },
        "_Account": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_Account"
          }
        },
        "_ExtCell": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_ExtCell"
          }
        },
        "_ExtRole": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_ExtRole"
          }
        },
        "_Relation": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_Relation"
          }
        }
      }
    ]
  }
}
```

## cURLサンプル
#### RoleのnavigationProperty経由一覧
```sh
curl "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell2.unit1.example%2F')/_Role" \
-X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

