---
id: version-1.7.21-302_Box_Installation
title: Boxインストール
sidebar_label: Boxインストール
---
## 概要
barファイルを使って指定されたパスにBoxをインストールする。barファイルフォーマットについては 「[barファイル](301_Bar_File.md)」を参照。  
本APIは非同期通信方式を採用しているため、本APIではBoxインストールを受け付けた後、即復帰する。  
そのため、Boxインストール状況を確認するには、以下のAPIを使用する。
* [Box メタデータ取得](303_Progress_of_Bar_File_Installation.md) Boxインストールが異常終了した場合は、本APIにてBoxインストール状況を確認することで、エラーとなった原因を参照することができる。以下に、クライアントにおける受付から処理完了までの呼び出し方法を示す。

```
Boxインストールの呼び出し例（クライアントでのポーリングを30秒とした場合)
 1. Boxインストール受付
    -- MKCOL /cell1/box1
 2. Boxインストール状況確認
    -- GET /cell1/box1  -> "処理中" で返却。
    -- 30秒ポーリング
 3. GET /cell1/box1  -> "処理完了" で返却。
 ※上記 2. の処理をループして処理完了までポーリングする。
```

### 必要な権限
box-install

### 制限事項
#### Boxインストール対象Box制限
* 既に同名のBoxが存在する場合は、Boxインストールできない。
* 既に同じscheme URLが設定されたBoxが存在する場合は、Boxインストールできない。
* メインボックスへのBoxインストールはできない。

#### barファイル制限
* Boxインストール可能なbarファイルのファイルサイズは以下を上限とする。  
上限値を超えた場合はBoxインストールできない。
	- barファイルのファイルサイズ:100MB
	- barファイル内エントリの圧縮前ファイルサイズ：10MB

#### Boxインストールのログ詳細制限
* Boxインストールのログ詳細は、Boxインストール対象Boxが所属するCellのEventBusへ出力される。 下記※1
	- そのため、ログ詳細を参照する場合は、ログファイル取得APIを使用して参照する。
	- ログファイル取得APIを使用するために、"log-read" の権限が必要である。
	- Boxインストール以外のイベントログも混在するため、"RequestKey" フィールド値でフィルタリングする必要がある。
	- "Type" フィールド値が "boxinstall" の "Requestkey" フィールド値を取得し、フィルタリングする。

#### その他制限
* Boxインストール処理中にBoxインストール対象Boxを含む配下のリソースへのデータ操作はできない。
* Boxインストール中にエラーが発生した場合のロールバックは行わない。

##### ※1 Boxインストールのログ詳細フォーマット
|状態|"Type"|"Object"|"Info"|
|:--|:--|:--|:--|
|Boxインストール受付|boxinstall|BoxのURL|ステータスコード|
|Boxインストール処理中|PL-BI-1000|BoxのURL|Bar installation started.|
||PL-BI-1001|Barファイル内のエントリパス|Installation started.|
||PL-BI-1003|Barファイル内のエントリパス|Installation completed.|
||PL-BI-1004|Barファイル内のエントリパス|Installation failed({原因}).|
||PL-BI-1005||Unknown error({原因}).|
|Boxインストール完了|PL-BI-0000|BoxのURL|Bar installation completed.|
||PL-BI-0001|BoxのURL|Bar installation failed({原因}).|

##### 処理コード
|処理コード|Description|
|:--|:--|
|PL-BI-0000|Boxインストール完了(正常終了)|
|PL-BI-0001|Boxインストール完了(異常終了)|
|PL-BI-1000|Boxインストール開始|
|PL-BI-1001|barファイル内エントリインストール開始|
|PL-BI-1003|barファイル内エントリインストール完了(正常終了)|
|PL-BI-1004|barファイル内エントリインストール完了(異常終了)|
|PL-BI-1005|内部エラー|

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}
```
### メソッド
MKCOL

### リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}  override} $: $ {value}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/zip|○||
|Content-Length|リクエストボディのサイズを指定する|半角数字|×||
### リクエストボディ
|概要|有効値|必須|備考|
|:--|:--|:--|:--|
|インストールするbarファイルをバイナリでリクエストボディに指定する|Content-Typeヘッダで指定した形式|○|barファイル：Zipファイル形式|

barファイルのファイル構成については [bar ファイル](301_Bar_File.md)を参照。


## レスポンス
### ステータスコード
|コード|メッセージ|概要|備考|
|:--|:--|:--|:--|
|202|Accepted|処理受付成功時||

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Location|Boxメタデータ取得API用URL||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
Locationサンプル
```
Location: https://cell1.unit1.example/box1
```
Boxメタデータ取得API用URLの詳細は、[Boxメタデータ取得](303_Progress_of_Bar_File_Installation.md)を参照。
### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1" -X MKCOL -i -H 'Content-type: application/zip' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-T "/tmp/sample.bar"
```
