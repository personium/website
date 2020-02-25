---
id: version-1.7.18-291_Cell_Change_Property
title: プロパティ変更
sidebar_label: プロパティ変更
---
## 概要
プロパティを変更する

### 必要な権限
ユニットユーザのみ可能

## リクエスト
### リクエストURL
```
{CellURL}
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
|propertyupdate|DAV:|propertyupdate（アクセス制御リスト）のルート|○|<ELEMENT propertyupdate! (Set &#124; remove)>||
|set|DAV:|プロパティ設定|×|<! ELEMENT set (prop *)>||
|remove|DAV:|プロパティ削除|×|<! ELEMENT set (prop *)>||
|prop|DAV:|プロパティ|×|<! ELEMENT prop ANY>|ANYに指定したXMLタグをキーとして設定または削除を行う|

※ 下記はシステムで予約されています。
  * p:relayhtmlurl （詳細は[Cellルート取得](./200_Cell_Root.md) を参照）
  * p:authorizationhtmlurl （詳細は[OAuth2.0 認可エンドポイント](./292_OAuth2_Authorization_Endpoint.md) を参照）
  * p:authorizationpasswordchangehtmlurl （詳細は[OAuth2.0 認可エンドポイント](./292_OAuth2_Authorization_Endpoint.md) を参照）
  * p:accountsnotrecordingauthhistory （詳細は[OAuth 2.0 トークンエンドポイント](./293_OAuth2_Token_Endpoint.md) を参照）

### リクエストサンプル
```xml
<D:propertyupdate xmlns:D="DAV:"  
    xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:foo>bar</p:foo>
    </D:prop>
  </D:set>
  <D:remove>
    <D:prop>
      <p:foo/>
    </D:prop>
  </D:remove>
</D:propertyupdate>
```

## レスポンス
### ステータスコード
|コード|メッセージ|概要|
|:--|:--|:--|
|207|MULTI_STATUS|成功|

### レスポンスヘッダ
なし

### レスポンスボディ

|項目名|Namespace|概要|備考|
|:--|:--|:--|:--|
|multistatus|DAV:|レスポンスボディのルート|<! ELEMENT multistatus (response *)>|
|response|DAV:|responseのルート|<! ELEMENT response (href, propstat)>|
|href|DAV:|PROPPATCHを実行したリソースのURL|PROPPATCHを実行したリソースのURL|
|propstat|DAV:|プロパティ設定結果|<! ELEMENT propstat (prop, status)>|
|prop|DAV:|プロパティ設定内容|リソース設定の結果を以下のように表示する<br>設定成功：設定したキーと値<br>削除成功：削除したキー|
|status|DAV:|プロパティ設定ステータスコード|設定成功の場合200(OK)が返る|
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/</href>
    <propstat>
      <prop>
        <p:foo xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">bar</p:foo>
        <p:foo xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:"/>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```

## cURLサンプル
```sh
curl "https://cell1.unit1.example/" -X PROPPATCH -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8" ?>\
<D:propertyupdate xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns"><D:set><D:prop>\
<p:foo>bar</p:foo></D:prop></D:set><D:remove><D:prop><p:foo/></D:prop>\
</D:remove></D:propertyupdate>'
```
