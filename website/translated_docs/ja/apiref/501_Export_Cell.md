---
id: 501_Export_Cell
title: Cellエクスポート
sidebar_label: Cellエクスポート
---
## 概要
Cell内の全てのデータをCellスナップショットファイルとしてエクスポートする。 
スナップショットファイルはPersoniumUnit内の特殊な領域(Cellスナップショット領域)に作成される。  
処理成功時は拡張子が".zip"のファイルを、失敗時は".error"のファイルを生成する。(".error"ファイルにはJSON形式で失敗原因を記載)  Cellスナップショット領域はCellエクスポートの対象外。  
本APIは非同期通信方式を採用しているため、APIを受け付けた後、即復帰する。  
Cellエクスポートの状況を確認するには[Cellエクスポート状態取得](502_Progress_of_Export_Cell.md)、[Cellスナップショットファイル設定取得](505_Get_Property_Snapshot_Cell.md)を使用する。  
クライアントにおける受付から処理完了までの呼び出し例を以下に示す。  

```
Cellエクスポートの呼び出し例（クライアントでのポーリングを10秒とした場合)
 1. Cellエクスポート受付
    -- POST https://cell1.unit1.example/__export
 2. Cellエクスポート状態確認
    -- GET https://cell1.unit1.example/__export -> "処理中"で返却。
    -- 10秒ポーリング
 3. Cellエクスポート完了
    -- GET https://cell1.unit1.example/__export -> "受付可能"で返却。
 4. Cellエクスポート正常終了確認
    -- PROPFIND /cell1/__snapshot -> ファイル拡張子が".zip"の場合正常終了。".error"の場合異常終了。
 ※上記 2. の処理はループして処理完了までポーリングする。
 ※異常終了時、詳細を取得したい場合は".error"ファイルの内容を参照する。
```

### 必要な権限
root

### 制限事項
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける


## エラーファイル
### 概要
Cellエクスポートに失敗した場合、Cellスナップショット領域に拡張子".error"のファイルが生成される。(ファイル名はボディで指定した名前)   
".error"ファイルにはエラーの内容がJSON形式で記載される。  
".error"ファイルのフォーマットを以下に示す。  

|オブジェクト|キー|型|値|備考|
|:--|:--|:--|:--|:--|
|ルート|code|string|||
|ルート|message|object|||
|message|lang|string|||
|message|value|string|||

### サンプル
```
{
  "code":"PR503-SV-0001",
  "message":
  {
    "lang":"en",
    "value":"Too many concurrent requests."
  }
}
```


## リクエスト
### リクエストURL
```
{CellURL}__export
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
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きする。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application / json|×|省略時は[application/json]として扱う|

### リクエストボディ
#### Format
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Name|スナップショットファイル名(拡張子は除く)|桁数：1～192<br>文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)|×|省略時は[{CellName}_yyyyMMdd_HHmmss]|

### リクエストサンプル
```json
{"Name":"CellExport_2017_01"}
```

## レスポンス
### ステータスコード
|コード|メッセージ|概要|
|:--|:--|:--|
|202|Accepted|処理受付|

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式|作成に失敗した場合のみ返却する|
|Location|Cellエクスポート状態取得用のURL||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
作成に失敗した場合のみエラーメッセージを返却する

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル
```sh
curl "https://cell1.unit1.example/__export" -X POST -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json' -d '{"Name":"CellExport_2017_01"}'
```

