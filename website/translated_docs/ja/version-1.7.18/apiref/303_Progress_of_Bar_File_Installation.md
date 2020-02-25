---
id: version-1.7.18-303_Progress_of_Bar_File_Installation
title: Boxメタデータ取得
sidebar_label: Boxメタデータ取得
---
## 概要
Boxのメタデータを取得する。メタデータには、以下の情報が含まれる。  
* Boxの状態  
Boxインストールの状況（インストール結果、進捗率、エラーメッセージ等）
* Boxの状態は以下の3種類が存在する
	- Boxが使用可能
	- Boxインストール処理中
	- Boxインストールの処理が異常終了
* Boxの名前
* BoxのURL
* BoxのスキーマURL
* Boxの作成日時
* [Cellメタデータ](296_Get_Cell_Metadata.md)
* [Unitメタデータ](107_Get_Unit_Metadata.md)

### 必要な権限
read

### 制限事項
* Boxインストール状況が確認可能な有効期限は、Boxインストール完了（異常終了を含む）後Unitで設定されている期限まで
* Boxインストールに失敗した場合は、EventBusに出力されたログを参照する必要がある


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}
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
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}  override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
### リクエストボディ
なし


## レスポンス
### ステータスコード

|コード|メッセージ|概要|備考|
|:--|:--|:--|:--|
|200|OK|成功時|Boxインストール成功可否はレスポンスボディを参照|
### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ
レスポンスはJSON形式で、オブジェクト（サブオブジェクト）に定義される。
キー(名前)と型、並びに値の対応は以下のとおり。

|オブジェクト|名前(キー)|型|値|備考|
|:--|:--|:--|:--|:--|
|ルート|box|object|Object (box format)||
|box|status|string|以下のいずれかの文字列:  <br>- "ready"<br>- "installation in progress"<br>- "installation failed"|Boxが使用可能な状態を示す<br>Boxインストール処理中を示す<br>Boxインストール完了（異常終了）を示す|
|box|started_at|string|Start time (ISO 8610 UTC format)|statusが以下の場合は出力しない。<br>- "Ready"<br>|
|box|progress|string|Progress rate (for example, "30%")|statusが以下の場合は出力しない。<br>- "Ready"|
|box|message|object|Object (message format)|statusが以下の場合のみ出力する。<br>- "Installation failed"<br>詳細は [エラーメッセージ一覧](004_Error_Messages.md)を参照|
|box|name|string|Boxの名前||
|box|url|string|BoxのURL||
|box|schema|string|Boxが紐づいているスキーマのURL|スキーマなしの場合は null|
|box|installed_at|string|Start time (ISO 8610 UTC format)|statusが以下のいずれかの場合は出力しない。<br>- "Installation in Progress"<br>- "installation failed"|
|ルート|cell|object|Object (cell format)||
|cell|name|string|Cellの名前||
|cell|url|string|CellのURL||
|ルート|unit|object|Object (unit format)||
|unit|url|string|UnitのURL||
|unit|path_based_cellurl_enabled|boolean|true:path based cell url<br>false:per cell fqdn url||

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
Boxの作成後（Boxインストール完了時を含む）
```JSON
{
  "box": {
    "status": "ready",
    "installed_at": "2017-02-13T09:00:00.000Z",
    "name": "app-box1",
    "url": "https://cell1.example.com/app-box1/",
    "schema": "https://app-cell1.example.com/"
  },
  "cell": {
    "name": "cell1",
    "url": "https://cell1.unit1.example/"
  },
  "unit": {
    "url": "https://unit1.example/",
    "path_based_cellurl_enabled": true
  }
}
```


Boxインストール処理中の場合
```JSON
{
  "box": {
    "status": "installation in progress",
    "started_at": "2017-02-13T09:00:00.000Z",
    "progress": "81%",
    "name": "app-box1",
    "url": "https://cell1.unit1.example/app-box1/",
    "schema": "https://app-cell1.unit1.example/"
  },
  "cell": {
    "name": "cell1",
    "url": "https://cell1.unit1.example/"
  },
  "unit": {
    "url": "https://unit1.example/",
    "path_based_cellurl_enabled": true
  }
}
```


Boxインストール完了時（異常終了）の場合  
（Boxインストールに失敗後、有効期限以内）
```JSON
{
  "box": {
    "status": "installation failed",
    "started_at": "2017-02-13T09:00:00.000Z",
    "progress": "81%",
    "message": {
      "code" : "PR409-OD-0003",
      "message" : {
        "lang" : "en",
        "value" : "The entity already exists."
      }
    },
    "name": "app-box1",
    "url": "https://cell1.unit1.example/app-box1/",
    "schema": "https://app-cell1.unit1.example/"
  },
  "cell": {
    "name": "cell1",
    "url": "https://cell1.unit1.example/"
  },
  "unit": {
    "url": "https://unit1.example/",
    "path_based_cellurl_enabled": true
  }
}
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

