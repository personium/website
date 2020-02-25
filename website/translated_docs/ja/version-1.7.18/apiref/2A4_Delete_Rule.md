---
id: version-1.7.18-2A4_Delete_Rule
title: Rule削除
sidebar_label: Rule削除
---
## 概要
登録されているRuleを削除する

### 必要な権限
rule

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
DELETE

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

### リクエストボディ
なし

## レスポンス
### ステータスコード
204

### レスポンスヘッダ
なし

### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Rule(Name='rule1',_Box.Name='box1')" -X DELETE -i \
-H 'If-Match: *' -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```
