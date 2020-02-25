---
id: version-1.7.18-386_Configure_Stream_Collection
title: Streamコレクションソース設定変更
sidebar_label: Streamコレクションソース設定変更
---
## 概要
Streamコレクションソースの設定を変更する

### 必要な権限
write-properties

## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{CollectionName}
```

### メソッド
PROPPATCH

### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|コンテンツ形式を指定する|application/xml|×||
|Accept|レスポンスで受け入れ可能なメディアタイプを指定する|application/xml|×||

### リクエストボディ
名前空間

|URI|概要|参考prefix|
|:--|:--|:--|
|DAV:|WebDAVの名前空間|D:|
|urn&#58;x-personium:xmlns|Personium APIの名前空間|p:|

※ 参考prefixは以下表の可読性を高めるためのもので、このprefix文字列の使用を保証するものでも要求するものでもありません。


XMLの構造  
ボディはXMLで、以下のスキーマに従っています。

|ノード名|名前空間|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|propertyupdate|D:|要素|propertyupdateのルートを表し、setとremoveが子となる||
|set|D:|要素|プロパティ設定を表し、1つ以上複数のpropが子となる||
|remove|D:|要素|プロパティ削除設定を表し、1つ以上複数のpropが子となる||
|prop|D:|要素|プロパティ値を表し、1つ以上複数の任意の要素が子となる|set時：子のノード名がキーとなる<br>remove時：子のノードを名キーとして削除を行う|

DTD表記
```dtd
<!ELEMENT propertyupdate (set, remove)
<!ELEMENT set (prop*) >
<!ELEMENT remove (prop*) >
<!ELEMENT prop ANY>
```

### Streamコレクション設定固有定義
|ノード名|名前空間|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|queues|p:|要素|queue設定を表し、1つ以上複数のqueue要素を子とする||
|queue|p:|要素|queue名の設定を表す。||
|topics|p:|要素|topic設定を表し、1つ以上複数のtopic要素を子とする||
|topic|p:|要素|topic名の設定を表す。||

DTD表記
```dtd
<!ELEMENT queues (queue*)>
<!ELEMENT queue (#PCDATA)>
<!ELEMENT topics (topic*)>
<!ELEMENT topic (#PCDATA)>
```
### リクエストサンプル
```xml
<D:propertyupdate xmlns:D="DAV:"
    xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:queues>
        <p:queue>queueName</p:queue>
      </p:queues>
      <p:topics>
        <p:topic>topicName</p:topic>
      </p:topics>
    </D:prop>
  </D:set>
</D:propertyupdate>
```


## レスポンス
### ステータスコード
207

### レスポンスヘッダ
なし

### レスポンスボディ
名前空間

|URI|概要|参考prefix|
|:--|:--|:--|
|DAV:|WebDAVの名前空間|D:|
※ 参考prefixは以下表の可読性を高めるためのもので、このprefix文字列の使用を保証するものでも要求するものでもありません。


XMLの構造  
ボディはXMLで、以下のスキーマに従っています。

|ノード名|名前空間|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|multistatus|D:|要素|multistatusのルートを表し、1つ以上複数のresponseが子となる||
|response|D:|要素|multistatusの内容を表し、hrefとpropstatが子となる||
|href|D:|要素|PROPPATCHを実行したリソースのURL||
|propstat|D:|要素|プロパティ設定結果を表し、propとstatusが子となる||
|prop|D:|要素|プロパティ設定内容を表す|リソース設定の結果を以下のように表示する<br>設定成功：設定したキーと値<br>削除成功：削除したキー|
|status|D:|要素|プロパティ設定ステータスコード|設定成功の場合200(OK)が返る|

DTD表記
```dtd
<!ELEMENT multistatus (response*)>
<!ELEMENT response (href, propstat)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT propstat (prop, status)>
<!ELEMENT prop ANY>
<!ELEMENT status (#PCDATA)>
```
### レスポンスサンプル
```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/box1/stream-collection1</href>
    <propstat>
      <prop>
        <p:queues xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">
          <p:queue>queueName</p:queue>
        </p:queues>
        <p:topics xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">
          <p:topic>topicName</p:topic>
        </p:topics>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/stream-collection1" -X PROPPATCH -i -H \
"Authorization:Bearer AA~PBDc...(省略)...FrTjA" -H "Accept:application/xml" -d "<?xml version=\"1.0\" \
encoding=\"utf-8\" ?><D:propertyupdate xmlns:D=\"DAV:\" xmlns:p=\"urn:x-personium:xmlns\"><D:set>\
<D:prop><p:queues><p:queue>queueName</p:queue></p:queues><p:topics><p:topic>topicName</p:topic></p:topics>\
</D:prop></D:set></D:propertyupdate>"
```
