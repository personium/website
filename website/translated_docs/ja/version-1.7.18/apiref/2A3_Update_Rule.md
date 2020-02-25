---
id: version-1.7.18-2A3_Update_Rule
title: Rule更新
sidebar_label: Rule更新
---
## 概要
既存のRule情報を更新する

### 必要な権限
rule

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする

## リクエスト
### リクエストURL
```
{CellURL}__ctl/Rule(Name='{RuleName}',_Box.Name='{BoxName}')
```
または、
```
{CellURL}__ctl/Rule(Name='{RuleName}')
```
または、
```
{CellURL}__ctl/Rule('{RuleName}')
```
※ \_Box.Nameパラメタを省略した場合は、nullが指定されたものとする

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
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### リクエストボディ
#### Format

Formatは[こちら](2A0_Create_Rule.md)を参照

### リクエストサンプル
```JSON
{"Name":"rule2", "EventExternal":true, "Action":"log"}
```

## レスポンス
### ステータスコード
204

### レスポンスヘッダ
なし

### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
なし

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Rule('rule1')" -X PUT -i -H 'If-Match: *' -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '{"Name":"rule2", "EventExternal":true, "Action":"log"}'
```
