---
id: version-1.7.21-507_Import_Cell
title: Cellインポート
sidebar_label: Cellインポート
---
## 概要
CellスナップショットファイルからCellのデータをインポートする。  
CellスナップショットファイルはPersoniumUnit内の特殊な領域(Cellスナップショット領域)のものを使用する。  
処理に失敗した場合、Cellのステータスを"import failed"に変更する。  
処理に成功した場合、Cellのステータスが"import failed"であれば"normal"に変更する。  
Cellのステータスが"import failed"の場合、対象のCellは一部API以外を受け付けない。詳細は[プロパティ取得](290_Cell_Get_Property.md)を参照。  
本APIは非同期通信方式を採用しているため、APIを受け付けた後、即復帰する。  
Cellインポートの状況を確認するには[Cellインポート状態取得](508_Progress_of_Import_Cell.md)を使用する。  
クライアントにおける受付から処理完了までの呼び出し例を以下に示す。  

```
Cellインポートの呼び出し例（クライアントでのポーリングを10秒とした場合)
 1. Cellインポート受付
    -- POST https://cell1.unit1.example/__import
 2. Cellインポート状態確認
    -- GET https://cell1.unit1.example/__import -> "処理中"で返却。
    -- 10秒ポーリング
 3. Cellインポート完了
    -- GET https://cell1.unit1.example/__import -> "受付可能"で返却。
 ※上記 2. の処理はループして処理完了までポーリングする。
```

### 必要な権限
root

### 制限事項
- リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
- リクエストボディはjson形式のみ受け付ける
- 処理が途中で失敗した場合でもロールバックは行わない  
※Cellインポートを実施する前に、一旦Cellのエクスポートを実施しておくことを推奨します。  

## リクエスト
### リクエストURL
```
{CellURL}__import
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
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application / json|×|省略時は[application/json]として扱う|

### リクエストボディ
#### Format
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Name|スナップショットファイル名(拡張子は除く)|桁数：1～192<br>文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)|○||

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
|Location|Cellインポート状態取得用のURL||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
作成に失敗した場合のみエラーメッセージを返却する

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル
```sh
curl "https://cell1.unit1.example/__import" -X POST -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -d '{"Name":"CellExport_2017_01"}'
```
