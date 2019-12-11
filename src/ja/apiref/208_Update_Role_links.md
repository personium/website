# Role_$links更新
## 概要
Roleの$link情報を更新する

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションは無視される


## リクエスト
### リクエストURL
#### Correlating with the Account
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_Account(Name='{AccountName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_Account('{AccountName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_Account(Name='{AccountName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_Account('{AccountName}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_Account(Name='{AccountName}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_Account('{AccountName}')
```
#### Correlating with ExtCell
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_ExtCell(Url='{ExtCellURL}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_ExtCell('{ExtCellURL}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_ExtCell(Url='{ExtCellURL}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_ExtCell('{ExtCellURL}')
```
#### Correlating with ExtRole
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}'
,_Relation.Name='{RelationName}',_Relation._Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}'
,_Relation.Name='{RelationName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_ExtRole(ExtRole=
'{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_ExtRole('{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}',_Relation._Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_ExtRole('{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}',_Relation._Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_ExtRole('{ExtRoleURL}')
```
#### Relation with linking
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_Relation(Name=
'{RelationName}',_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_Relation(Name=
'{RelationName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}',_Box.Name='{BoxName}')/$links/_Relation('{RelationName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_Relation(Name='{RelationName}',
_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_Relation(Name='{RelationName}')
```
または、
```
{CellURL}__ctl/Role(Name='{RoleName}')/$links/_Relation('{RelationName}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_Relation(Name='{RelationName}',_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_Relation(Name='{RelationName}')
```
または、
```
{CellURL}__ctl/Role('{RoleName}')/$links/_Relation('{RelationName}')
```
※ \_Box.Nameパラメタを省略した場合は、nullが指定されたものとする  
※ ExtCellのキーはURLエンコードした文字列を指定する  

### メソッド
PUT
### リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値} &#160;override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|If-Match|対象ETag値を指定する|ETag値|×|省略時は[*]として扱う|
### リクエストボディ
#### Format
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|uri|紐付けるODataリソースのURI|桁数：1&#65374;1024<br>URIの形式に従う<br>scheme：http / https / urn|○||

### リクエストサンプル
```JSON
{"uri":"https://cell1.unit1.example/__ctl/Box('box2')"}
```

## レスポンス
### ステータスコード
204

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|DataServiceVersion|ODataのバージョン||
|ETag|リソースのバージョン情報||
### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Role(Name="role1",_Box.Name=null)/$links/_Box" -X \
PUT -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' -d \
'{"uri":"https://cell1.unit1.example/__ctl/Box('box2')"}'
```

