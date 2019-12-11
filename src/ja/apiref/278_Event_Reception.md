# 外部イベント受付
## 概要
Cellのイベント処理機能で扱うための任意の外部イベントを受付ける。

### 必要な権限
event

## リクエスト
### リクエストURL
```
{CellURL}__event
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
### リクエストボディ
JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Type|イベントの型|文字列型<br>桁数：0&#65374;51200 byte|×||
|Object|イベントの対象オブジェクト|文字列型<br>桁数：0&#65374;51200 byte|×||
|Info|イベントの情報|文字列型<br>桁数：0&#65374;51200 byte|×||
#### リクエストサンプル
```JSON
{
  "Type":"authSchema",
  "Object":"https://cell1.unit1.example/box1/service_name/token_keeper",
  "Info":"[XXXX2033] Success schema authorization. cellUrl=https://keeper-d4a57bb26eae481486b07d06487051d1.unit1.example/"
}
```

## レスポンス
### ステータスコード
|コード|メッセージ|概要|
|:--|:--|:--|
|200|OK|受付成功時|
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
### レスポンスボディ
なし
### エラーレスポンス
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル
```sh
curl "https://cell1.unit1.example/__event" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json' \
-d '{"Type":"authSchema", "Object":"https://cell1.unit1.example/box1/service_name/token_keeper", \
"Info":"[XXXX2033] Success schema authorization. \
cellUrl=https://keeper-d4a57bb26eae481486b07d06487051d1.unit1.example/"}'
```
