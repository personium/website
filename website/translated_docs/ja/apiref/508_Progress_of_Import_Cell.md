---
id: 508_Progress_of_Import_Cell
title: Cellインポート状態取得
sidebar_label: Cellインポート状態取得
---
## 概要
Cellインポートの状態を取得する。Cellインポート状態には、以下の情報が含まれる。
* Cellインポートの状態
	* Cellインポート受付可能
	* Cellインポート処理中
	* Cellインポート異常終了
* インポート開始日時
* 進捗率
* インポートファイル名
* エラーメッセージ

### 必要な権限
root


## リクエスト
### リクエストURL
```
{CellURL}__import
```

### メソッド
GET

### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}  override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|

### リクエストボディ
なし


## レスポンス
### ステータスコード
|コード|メッセージ|概要|備考|
|:--|:--|:--|:--|
|200|OK|成功時|Cellインポートの状態はレスポンスボディを参照|

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Content-Type|返却されるデータの形式||

### レスポンスボディ
レスポンスはJSON形式で、オブジェクト（サブオブジェクト）に定義される。
キー(名前)と型、並びに値の対応は以下のとおり。

|オブジェクト|キー|型|値|備考|
|:--|:--|:--|:--|:--|
|ルート|status|string|以下のいずれかの文字列:  <br>"ready"<br>"importation in progress"<br>"import failed"|"ready":Cellインポート受付可能<br>"importation in progress":Cellインポート処理中<br>"import failed":Cellインポート異常終了|
|ルート|started_at|string|Start time (ISO 8610 UTC format)|statusが以下の場合は出力しない。<br>"ready"|
|ルート|progress|string|Progress rate (for example, "30%")|statusが以下の場合は出力しない。<br>"ready"|
|ルート|importation_name|string|インポートファイル名(拡張子は除く)|statusが以下の場合は出力しない。<br>"ready"|
|ルート|message|object|Object (message format)|statusが以下の場合のみ出力する。<br>"import failed"<br>詳細は [エラーメッセージ一覧](004_Error_Messages.md)を参照|

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
Cellインポート受付可能（Cellインポート完了時を含む）
```json
{
  "status": "ready"
}
```

Cellインポート処理中の場合
```json
{
  "status": "importation in progress",
  "started_at": "2017-02-13T09:00:00.000Z",
  "progress": "81%",
  "importation_name": "CellExport_2017_01"
}
```

Cellインポート異常終了
```json
{
  "status": "import failed",
  "started_at": "2017-02-13T09:00:00.000Z",
  "progress": "81%",
  "importation_name": "CellExport_2017_01",
  "message": {
      "code" : "PR409-OD-0003",
      "message" : {
          "lang" : "en",
          "value" : "The entity already exists."
      }
  }
}
```


## cURLサンプル
```sh
curl "https://cell1.unit1.example/__import" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json'
```

