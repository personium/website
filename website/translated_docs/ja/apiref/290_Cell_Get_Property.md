---
id: 290_Cell_Get_Property
title: プロパティ取得
sidebar_label: プロパティ取得
---
## 概要
セルのプロパティを取得する

## 必要な権限
propfind
* ACLの設定状況を取得する場合は、合わせてacl-readが必要

## 制限事項
V1.0版での制限
* 対象リソースが返却出来るプロパティの一覧を返却する機能
* レスポンスボディで返却するプロパティを指定する機能
	- 現状allpropとなる


## リクエスト
### リクエストURL
```
{CellURL}
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
|allprop||要素|全プロパティを取得設定を表す|allprop・・・すべてのプロパティを取得する<br>リクエストボディが空の場合も、allpropとして扱う<br>allprop以外の要素はv1.2系、v1.1系未対応|

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
|207|Multi-Status|成功|
### レスポンスヘッダ

|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン情報|正常にEntityが取得できた場合のみ返却する|
### レスポンスボディ
名前空間

|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式|D:|
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
|prop|D:|要素|プロパティ詳細情報を表し、creationdateとresourcetypeとaclとproppatch設定値が子となる||
|creationdate|D:|要素|リソース作成時刻||
|getcontentlength|D:|要素|リソースのサイズ|リソースがファイルの場合のみ|
|getcontenttype|p:|要素|リソースのcontenttype|リソースがファイルの場合のみ|
|getlastmodified|p:|要素|リソース更新時刻||
|resourcetype|p:|要素|リソースのタイプを表す。 collection、odata、serviceのいずれかが子となるか、子は空となる||
|collection|p:|要素|リソースのタイプがコレクションであることを表す<br>リソースがWebDAVの場合、この要素のみが表示される||
|odata|p:|要素|リソースのタイプがODataコレクションであることを表す|ODataコレクションの場合表示|
|service|p:|要素|リソースのタイプがサービスコレクションであることを表す|Serviceコレクションの場合表示|
|cellstatus|p:|要素|Cellのステータスを表す<br>normal:正常<br>import failed:Cell Import失敗|Cellのステータスがimport failedの場合は以下のAPI以外は実行不可<br>- Unit Level API<br>- OAuth2.0 トークンエンドポイント<br>- Cellインポート|
|acl|p:|要素|リソースに設定されているACL設定|ACL設定を取得するためには、対象リソースに対するacl-read権限が必要<br>ACL要素以下の内容については、[Cell Level アクセス制御設定API](289_Cell_ACL.md)を参照|
|base|p:|要素|ACLのPrivilegeのBaseURL|CellへのPROPFINDの場合、デフォルトBox（"__"）のリソースURL|
|status|D:|要素|リソース取得のレスポンスコードを表す||

#### DTD表記
名前空間：D:
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

名前空間:p:
```dtd
<!ELEMENT odata EMPTY>
<!ELEMENT service EMPTY>
```

名前空間：xml:
```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/</href>
    <propstat>
      <prop>
        <creationdate>2017-02-03T01:27:31.130+0000</creationdate>
        <getlastmodified>Fri, 03 Feb 2017 01:27:31 GMT</getlastmodified>
        <resourcetype>
          <collection/>
        </resourcetype>
        <p:cellstatus xmlns:p="urn:x-personium:xmlns">normal</p:cellstatus>
        <acl xmlns:p="urn:x-personium:xmlns"/>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```


## cURLサンプル
```sh
curl "https://cell1.unit1.example/" -X PROPFIND -i -H 'Depth:1' \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-d '<?xml version="1.0" encoding="utf-8"?><D:propfind xmlns:D="DAV:"><D:allpop/></D:propfind>'
```

