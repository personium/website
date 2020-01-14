---
id: 267_Received_Message_Approval
title: メッセージ状態変更(未読,既読,承認)
sidebar_label: メッセージ状態変更(未読,既読,承認)
---
## 概要
* メッセージを承認/拒否する  
  * 承認するメッセージのTypeがmessageの場合  
    メッセージの状態を既読/未読に変更する  
  * 承認するメッセージのTypeがrequestの場合  
    * RequestTypeがrelation.add/reation.removeの場合  
      メッセージの値に従い、RelationとExtCellをリンク/リンク解除し、メッセージの状態を承認/拒否に変更する  
    * RequestTypeがrole.add/role.removeの場合  
      メッセージの値に従い、RoleとExtCellをリンク/リンク解除し、メッセージの状態を承認/拒否に変更する  
    * RequestTypeがrule.add/rule.removeの場合  
      メッセージの値に従い、Ruleを作成/削除し、メッセージの状態を承認/拒否に変更する  

### 必要な権限
message

Typeがrequestの場合はRequestTypeに応じて以下の権限も必要

|RequestType|必要な権限|
|:-|:-|
|relation.add<br>relation.remove<br>role.add<br>role.remove|social|
|rule.add<br>rule.remove|rule|
### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
```
{CellURL}__message/received/{MessageID}
```
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
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Command|メッセージコマンド|Typeがmessageの場合<br>　read: 既読<br>　unread: 未読<br>Typeがrequestの場合<br>　approved: 承認<br>　rejected: 拒否<br>　ただし既にapproved、rejectedに変更済みの場合は承認不可|○||
### リクエストサンプル
```JSON
{"Command": "approved"}
```


## レスポンス
### ステータスコード
204
### レスポンスヘッダ
|項目名|概要|備考|
|:--|:--|:--|
|ETag|リソースのバージョン情報||
|DataServiceVersion|ODataのバージョン||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
なし
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__message/received/c87b42e10df846a9bee842225d1383fe" -X POST \
-i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '{"Command": "approved"}'
```
