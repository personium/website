---
id: version-1.7.21-214_List_Account
title: Account一覧取得
sidebar_label: Account一覧取得
---
## 概要
既存のAccount情報の一覧を取得する

### 必要な権限
auth-read

### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする
* $formatクエリオプションにatom または xmlを指定した場合、エラーとはならないが、レスポンスボディのデータの保証はない


## リクエスト
### リクエストURL
```
{CellURL}__ctl/Account
```
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
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
### リクエストボディ
なし


## レスポンス
### ステータスコード
200

### レスポンスヘッダ
なし

### レスポンスボディ

|オブジェクト|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|__metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|__published|string|作成日(UNIX時間)|
|{2}|__updated|string|更新日(UNIX時間)|
|{1}|__count|string|$inlinecountクエリでの取得結果件数|

### Account固有レスポンスボディ
|オブジェクト|項目名|型|備考|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.Account|
|{2}|Name|string|Account名|
|{2}|IPAddressRange|string|デフォルト：null|
|{2}|Status|string|デフォルト："active"|
|{2}|Type|string|デフォルト："basic"|
|{2}|Cell|string|デフォルト：null|

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Account('account1')",
          "etag": "W/\"1-1486462510467\"",
          "type": "CellCtl.Account"
        },
        "Name": "account1",
        "IPAddressRange": null,
        "Status": "active",
        "Type": "basic",
        "Cell": null,
        "__published": "/Date(1486462510467)/",
        "__updated": "/Date(1486462510467)/",
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account1')/_Role"
          }
        },
        "_ReceivedMessageRead": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account1')/_ReceivedMessageRead"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Account('account2')",
          "etag": "W/\"1-1486465908803\"",
          "type": "CellCtl.Account"
        },
        "Name": "account2",
        "IPAddressRange": "192.127.0.2,192.128.0.0/24",
        "Status": "deactivated",
        "Type": "basic",
        "Cell": null,
        "__published": "/Date(1486465908803)/",
        "__updated": "/Date(1486465908803)/",
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account2')/_Role"
          }
        },
        "_ReceivedMessageRead": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account2')/_ReceivedMessageRead"
          }
        }
      }
    ]
  }
}
```

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Account" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

