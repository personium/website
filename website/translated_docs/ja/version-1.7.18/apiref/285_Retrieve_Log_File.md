---
id: version-1.7.18-285_Retrieve_Log_File
title: ログファイル取得
sidebar_label: ログファイル取得
---
## 概要
イベントログファイルを取得します。

### 必要な権限
log-read
### 制限事項
計画されているログの出力設定は未サポートで、以下の固定設定が適用されます。

* ログファイル名は"default.log"固定です。
* ログサイズが一定の値に達したときローテートしてアーカイブされます。 (50MB)
* ローテート時のファイル名は、 default.log.{Timestamp} となります。 {Timestamp}は、ローテートされたときの時刻です。
* アーカイブは一定数のログファイルのみを保持します。（12世代）
* アーカイブログが最大数に達したときには、最古のログが自動削除されます

|アクション|アーカイブされたログファイル|説明|備考|
|:--|:--|:--|:--|
|First Rotation|archive/<br>default.log.1402910774659|<br>新規にローテートされたファイル|<br>2014-06-16 18:26:14 +0900|
|2nd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659|<br>前回ローテートされたファイル<br>新規にローテートされたファイル|<br>2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900|
|3rd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659<br>default.log.1403910784659|<br>前々回にローテートされたファイル<br>前回ローテートされたファイル<br>新規にローテートされたファイル|<br>2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900<br>2014-07-09 21:59:44 +0900|


## リクエスト
### リクエストURL
#### 最新のログファイルを取得
```
{CellURL}__log/current/{LogName}
```
#### ローテートされたログファイルを取得
```
{CellURL}__log/archive/{LogName}
```
※{LogName}は、ログファイル情報取得API で返却されたファイル名を指定する。
### メソッド
GET
### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
### リクエストボディ
なし
### リクエストサンプル
なし


## レスポンス
### ステータスコード
200
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|Resourceのデータ形式に応じたMimeType|"text/csv"または"application/zip"|
### レスポンスボディ
currentのログ取得時にログが存在しない場合は、空のレスポンスボディを返却する。  
ローテートのサイズ設定値よりも5MB程度大きなサイズとなる場合がある。  
出力形式は以下の通り。
```
{dateTime},[{level}],{RequestKey},{external},{schema},{subject},{type},{object},{info}
```
|項目名|概要|備考|
|:--|:--|:--|
|dateTime|ログ書込み日時（ISO8601 UTC形式）|YYYY-MM-DDTHH:MM:SS.sssZ|
|level|ログレベル INFO,WARN,ERRORのいずれか|文字列|
|RequestKey|X-Personium-RequestKeyヘッダで指定された値<br>X-Personium-RequestKeyヘッダ指定がない場合、PCS-${UUIDで32文字の文字列}|文字列|
|external|外部イベント：true<br>内部イベント：false|文字列|
|schema|受け付けたURLのboxのschema|URL形式|
|subject|イベントの主体|URL形式|
|type|外部イベント：イベント受付で定義されたtype<br>内部イベント：イベント毎に定義された型|文字列|
|object|外部イベント：イベント受付で定義されたobject<br>内部イベント：リクエストされたリソースパス|文字列|
|info|外部イベント：イベント受付で定義されたinfo<br>内部イベント：HTTPステータスコード|文字列|
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
外部イベント
```
2013-02-04T00:50:12.761Z,[INFO ],"Req_animal-access_1001","true","https://cell1.unit1.example/",
"https://unitadmin.unit1.example/#admin","authSchema","https://cell1.unit1.example/box1/service_name/token_keeper",
"[XXXX2033] Success schema authorization. cellUrl=https://keeper-d4a57bb26eae481486b07d06487051d1.unit1.example/"
```

内部イベント
```
2013-04-18T14:52:39.778Z,[INFO ],"PCS-1364350331902","false","https://app-cell1.unit1.example/",
"https://app-cell1.unit1.example/#staff","cellctl.Role.list","https://homeClinic.unit1.example/__ctl/Role","200"
```


## cURLサンプル

```sh
curl "https://cell1.unit1.example/__log/current/default.log" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

