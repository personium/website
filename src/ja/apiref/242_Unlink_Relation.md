# Relationと他オブジェクトとのリンク解除
## 概要
Relationとの$links情報を削除する  
以下のODataリソースを指定できる  
* Box
* ExtCell
* ExtRole
* Role

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションは無視される


## リクエスト
### リクエストURL
#### Linking with Box
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_Box('{BoxName}')
```
#### Linking with ExtCell
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_ExtCell('{ExtCellURL}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtCell('{ExtCellURL}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtCell('{ExtCellURL}')
```
#### Linking with ExtRole
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name='{RelationName}',_Relation._Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}'
,_Relation.Name='{RelationName}',_Relation._Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}'
,_Relation.Name='{RelationName}',_Relation._Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name='{RelationName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}'
,_Relation.Name='{RelationName}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}'
,_Relation.Name='{RelationName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_ExtRole(ExtRole='{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_ExtRole('{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole('{ExtRoleURL}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole('{ExtRoleURL}')
```
#### Linking with Role
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Role(Name='{RoleName}'
,_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_Role(Name='{RoleName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Role(Name='{RoleName}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Role(Name='{RoleName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links
/_Role('{RoleName}')
```
または、
```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Role('{RoleName}')
```
または、
```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Role('{RoleName}')
```
※ \_Box.Name, \_Relation.Name, \_Relation.\_Box.Nameパラメタを省略した場合は、nullが指定されたものとする  
※ ExtCellのキーはURLエンコードした文字列を指定する
### メソッド
DELETE
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
なし

## レスポンス
### ステータスコード
204
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|DataServiceVersion|ODataのバージョン||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ
なし
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Relation(Name='relation1',_Box.Name='box1')\
/\$links/_Role(Name='role1',_Box.Name='box2')" -X DELETE -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

