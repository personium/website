---
id: version-1.7.21-284_Retrieve_Log_File_list
title: ログファイル一覧取得
sidebar_label: ログファイル一覧取得
---
## 概要
指定されたURL配下のログファイルの一覧を取得する
### 必要な権限
log-read

### 制限事項

計画されているログの出力設定は未サポートで、以下の固定設定が適用されます。

* ログファイル名は"default.log"固定です。
* ログサイズが一定の値に達したときローテートしてアーカイブされます。 (50MB)
* ローテート時のファイル名は、 default.log.{Timestamp} となります。 {Timestamp}は、ローテートされたときの時刻です。
* アーカイブは一定数のログファイルのみを保持します。（12世代）
* アーカイブログが最大数に達したときには、最古のログが自動削除されます。

|アクション|アーカイブされたログファイル|説明|備考|
|:--|:--|:--|:--|
|First Rotation|archive/<br>default.log.1402910774659|新規にローテートされたファイル|2014-06-16 18:26:14 +0900|
|2nd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659|前回ローテートされたファイル<br>新規にローテートされたファイル|2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900|
|3rd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659  <br>default.log.1403910784659|前々回にローテートされたファイル<br>前回ローテートされたファイル<br>新規にローテートされたファイル| 2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900<br>2014-07-09 21:59:44 +0900|


## リクエスト
### リクエストURL
#### 最新のログファイルの一覧を取得
```
{CellURL}__log/current
```
#### ローテートされたログファイルの一覧を取得
```
{CellURL}__log/archive
```
### メソッド
PROPFIND
### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Depth|取得するリソースの階層|0:対象のリソース自身<br>1:対象のリソースとそれの直下のリソース|○||
### リクエストボディ
#### 名前空間
|URI|概要|備考()prefix|
|:--|:--|:--|
|DAV:|WebDAVの名前空間|D:|
※ 参考prefixは以下表の可読性を高めるためのもので、このprefix文字列の使用を保証するものでも要求するものでもありません。
#### XMLの構造
ボディはXMLで、以下のスキーマに従っています。

|ノード名|Namespace|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|propfind|D:|要素|propfindのルート要素を表し、allpropが子となる。||
|allprop|D:|要素|全プロパティを取得設定を表す|allprop・・・すべてのプロパティを取得する<br>リクエストボディが空の場合も、allpropとして扱う<br>allprop以外の要素はv1.2系、v1.1系未対応|
#### DTD表記
```dtd
<!ELEMENT propfind (allprop) >
<!ELEMENT allprop ENPTY >
```
### リクエストサンプル
```xml
<?xml version="1.0" encoding="utf-8"?>
<D:propfind xmlns:D="DAV:">
<D:allprop/>
</D:propfind>
```


## レスポンス
### ステータスコード
|コード|メッセージ|概要|
|:--|:--|:--|
|207|Multi-Status|取得成功時|
### レスポンスヘッダ
|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|Resourceのデータ形式に応じたMimeType|"application/xml"|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|有効なバージョン|

### レスポンスボディ
#### 名前空間
|URI|概要|参考Prefix|
|:--|:--|:--|
|DAV:|WebDAVの名前空間|D:|
|urn&#58;x-personium:xmlns|Personiumの名前空間|p:|
※ 参考prefixは以下表の可読性を高めるためのもので、このprefix文字列の使用を保証するものでも要求するものでもありません。
#### XMLの構造
ボディはXMLで、以下のスキーマに従っています。

|ノード名|Namespace|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|multistatus|D:|要素|multistatusのルートを表し、1つ以上複数のresponseが子となる||
|response|D:|要素|リソース取得のレスポンスを表し、hrefとpropstatが子となる||
|href|D:|要素|リソースのurl||
|propstat|D:|要素|リソースのプロパティ情報を表し、statusとpropが子となる||
|status|D:|要素|リソース取得のレスポンスコードを表す||
|prop|D:|要素|プロパティ詳細情報を表し、creationdateとresourcetypeとaclとproppatch設定値が子となる||
|creationdate|D:|要素|リソース作成時刻||
|getcontentlength|D:|要素|リソースのサイズ|リソースがファイルの場合のみ|
|getcontenttype|p:|要素|リソースのcontenttype|リソースがファイルの場合のみ|
|getlastmodified|p:|要素|リソース更新時刻||
|resourcetype|p:|要素|リソースのタイプを表す。<br>collectionと、odataかserviceのいづれかが子となるか、子は空となる||
|collection|p:|要素|リソースのタイプがコレクションであることを表す|リソースがWebDAVの場合、この要素のみが表示される|
|odata|p:|要素|リソースのタイプがODataコレクションであることを表す|ODataコレクションの場合表示|
|service|p:|要素|リソースのタイプがサービスコレクションであることを表す|Serviceコレクションの場合表示|
|acl|p:|要素|リソースに設定されているACL設定|ACL設定を取得するためには、対象リソースに対するacl-read権限が必要 ACL要素以下の内容については、[Cell Level アクセス制御設定API](289_Cell_ACL.md)を参照|
|base|p:|要素|ACLのPrivilegeのBaseURL|CellへのPROPFINDの場合、デフォルトBox（"__"）のリソースURL|
#### DTD表記
#### 名前空間：D:
```dtd
<!ELEMENT multistatus (response*)>
<!ELEMENT response (href, propstat)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT propstat (status, prop)>
<!ELEMENT status (#PCDATA)>
<!ELEMENT prop (creationdate, resourcetype, acl, ANY)>
<!ELEMENT creationdate (#PCDATA)>
<!ELEMENT getcontentlength (#PCDATA)>
<!ELEMENT getcontenttype (#PCDATA)>
<!ELEMENT getlastmodified (#PCDATA)>
<!ELEMENT resourcetype ((collection, (odata or service) or EMPTY))>
<!ELEMENT collection EMPTY>
<!ELEMENT acl (ace*)>
```
#### 名前空間:p:
```dtd
<!ELEMENT odata EMPTY>
<!ELEMENT service EMPTY>
```
#### 名前空間：xml:
```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```
### レスポンスサンプル
#### resourcetype要素
```xml
<?xml version="1.0" encoding="utf-8"?>
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/__log/archive</href>
    <propstat>
      <prop>
        <creationdate>2017-02-03T01:27:31.093+0000</creationdate>
        <getlastmodified>Fri, 03 Feb 2017 01:27:31 GMT</getlastmodified>
        <resourcetype>
          <collection/>
        </resourcetype>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```
なお、ログファイルのローテート時にファイルのZIP圧縮有無を指定可能とする予定（ログ設定更新API）
この際、ログファイルの圧縮有無によって、href要素のファイル名と、getcontenttype要素のMimeTypeが切り替わる

|ZIP圧縮有無|href要素のファイル名(例)|getcontenttypeの値|備考|
|:--|:--|:--|:--|
|圧縮なし|default.log.1364460341902|text/csv|ローテートなしの場合も同様|
|圧縮あり|default.log.1364460341902.zip|application/zip||
#### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__log/archive" -X PROPFIND -i -H 'Depth:1' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

