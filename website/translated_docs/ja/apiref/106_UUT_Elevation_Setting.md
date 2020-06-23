---
id: 106_UUT_Elevation_Setting
title: ULUUT昇格設定
sidebar_label: ULUUT昇格設定
---
## 概要
UUT（Unit User Token）昇格設定を変更する

### 必要な権限
Unitユーザのみ可能

## リクエスト
### リクエストURL
```
{CellURL}
```
|Path|概要|
|:--|:--|
|{CellName}|セル名|

### メソッド
PROPPATCH

### リクエストクエリ
なし

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|コンテンツ形式を指定する|application / xml|×||
|Accept|レスポンスで受け入れ可能なメディアタイプを指定する|application / xml|×||
### リクエストボディ

|項目名|Namespace|概要|必須|有効値|備考|
|:--|:--|:--|:--|:--|:--|
|DAV:||XML名前空間設定|○|"DAV:"||
|urn: x-personium: xmlns||XML名前空間設定|○|"Urn: x-personium: xmlns"||
|http://www.w3.com/standards/z39.50/||XML名前空間設定|○|"http://www.w3.com/standards/z39.50/"||
|propertyupdate|DAV:|propertyupdate（アクセス制御リスト）のルート|○|<ELEMENT propertyupdate! (Set &#124; remove)>||
|set|DAV:|プロパティ設定|×|<! ELEMENT set (prop *)>||
|remove|DAV:|プロパティ削除|×|<! ELEMENT set (prop *)>||
|prop|DAV:|プロパティ削除値|×|<! ELEMENT prop ANY>|ANYに指定したXMLがタグをキーとして削除を行う|
|prop|DAV:|プロパティ設定値|×|<! ELEMENT prop ANY>|ANYに指定したXMLタグがキーとなる|
|ownerRepresentativeAccounts||昇格設定|○|<! ELEMENT ownerRepresentativeAccounts (account *)>||
|account||昇格対象アカウント設定|○|<! ELEMENT account ANY>|昇格を認めるアカウント名を値として指定する|
### XMLの構造
#### ボディはXMLで、以下のスキーマに従っています。

|ノード名|Namespace|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|propertyupdate|D:|要素|propertyupdateのルートを表し、setとremoveが子となる||
|set|D:|要素|プロパティ設定を表し、1つ以上複数のpropが子となる||
|remove|D:|要素|プロパティ削除設定を表し、1つ以上複数のpropが子となる||
|prop|D:|要素|プロパティ値を表し、1つ以上複数の任意の要素が子となる|set時：子のノード名がキーとなる<br>remove時：子のノードを名キーとして削除を行う|
### DTD表記
```dtd
<!ELEMENT propertyupdate (set, remove) >
<!ELEMENT set (prop*) >
<!ELEMENT remove (prop*) >
<!ELEMENT prop ANY>
```
### ULUUT昇格設定固有要素
#### ボディはXMLで、以下のスキーマに従っています。

|ノード名|Namespace|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|ownerRepresentativeAccounts|p:|要素|昇格設定リストを表し、１つ以上複数のaccount要素をが子となる||
|account|p:|要素|昇格対象アカウント設定を表し、昇格対象となるアカウント名を記述する||
#### DTD表記
```dtd
<!ELEMENT ownerRepresentativeAccounts (account*)>
<!ELEMENT account (#PCDATA)>
```
### リクエストサンプル
```xml
<D:propertyupdate xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:ownerRepresentativeAccounts><p:account>account1</p:account><p:account>
account2</p:account></p:ownerRepresentativeAccounts>
    </D:prop>
  </D:set>
</D:propertyupdate>
```

## レスポンス
### ステータスコード

|コード|メッセージ|概要|
|:--|:--|:--|
|207|MULTI_STATUS|成功|

### レスポンスボディ
名前空間

|URI|概要|備考 (prefix)|
|:--|:--|:--|
|multistatus|WebDAVの名前空間|D:|

### XMLの構造
#### ボディはXMLで、以下のスキーマに従っています。

|ノード名|Namespace|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|multistatus|D:|要素|multistatusのルートを表し、1つ以上複数のresponseが子となる||
|response|D:|要素|multistatusの内容を表し、hrefとpropstatが子となる||
|href|D:|要素|PROPPATCHを実行したリソースのURL||
|propstat|D:|要素|プロパティ設定結果を表し、propとstatusが子となる||
|prop|D:|要素|プロパティ設定内容を表す|リソース設定の結果を以下のように表示する 設定成功：設定したキーと値 削除成功：削除したキー|
|status|D:|要素|プロパティ設定ステータスコード|設定成功の場合200(OK)が返る|
### DTD表記
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
    <href>http://localhost:9998/testcell1/box1/patchcol</href>
    <propstat>
      <prop>
        <Z:Author xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:" 
xmlns:Z="http://www.w3.com/standards/z39.50/">Author1 update</Z:Author>
        <p:hoge xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" 
xmlns:Z="http://www.w3.com/standards/z39.50/">fuga</p:hoge>
        <Z:Author xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:" 
xmlns:Z="http://www.w3.com/standards/z39.50/"/>
        <p:hoge xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" 
xmlns:Z="http://www.w3.com/standards/z39.50/"/>
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
curl "https://cell1.unit1.example/ -X PROPPATCH" \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-d '<?xml version="1.0" encoding="utf-8" ?>\
<D:propertyupdate xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" \
xmlns:Z="http://www.w3.com/standards/z39.50/">\
<D:set><D:prop><p:requireSchemaAuthz>confidential</p:requireSchemaAuthz></D:prop></D:set>\
</D:propertyupdate>'
```

