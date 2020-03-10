---
id: 002_CORS_Support
title: CORS(Cross Origin Resource Sharing)対応
sidebar_label: CORS(Cross Origin Resource Sharing)対応
---
## 概要
PersoniumのすべてのAPIは、一部例外を除き原則CORS(Cross Origin Resource Sharing)での利用を想定しています。  
具体的には特段例外としての記述が無い場合、全APIエンドポイントがリクエストに応じて以下のレスポンスヘッダを返却します。
1. Access-Control-Allow-Origin
2. Access-Control-Allow-Methods
3. Access-Control-Allow-Headers

これにより、JavaScriptなどのウェブブラウザ搭載のスクリプト言語でサーバとのHTTP非同期通信を行うため、XMLHttpRequest Level 2を使用することができます。
### Access-Control-Allow-Originレスポンスヘッダの返却
すべてのAPIにおいて、Access-Control-Allow-Originレスポンスヘッダとして*を返却します。  
Access-Control-Allow-Originレスポンスヘッダはアクセスを許可しているドメインを返却するものですが、Personiumは全てのドメインからのアクセスを許可すべくこのような振る舞いをします。  
次に示すのは、Access-Control-Allow-Originのレスポンスヘッダの例です。
```
Access-Control-Allow-Origin: *
```
### ブラウザからのプレフライトリクエストへの対応
ブラウザからのプレフライトリクエストへの対応として、すべてのAPIにおいてOPTIONSメソッドのリクエストを発行すると以下の振る舞いをします。
1. Access-Control-Allow-Methods レスポンスヘッダの返却
2. Access-Control-Allow-Headers レスポンスヘッダの返却

#### Access-Control-Allow-Methods レスポンスヘッダの返却
すべてのAPIにおいてOPTIONSメソッドのリクエストを発行すると、Access-Control-Allow-Methodsレスポンスヘッダを返却します。  
Access-Control-Allow-Methodsレスポンスヘッダの内容は、APIのアクセス制御設定とAuthorizationヘッダの内容によって以下のように変化します。

|条件|結果|
|:--|:--|
|公開（Authorizationヘッダなしでも読み取り可能）なリソース|そのリソースがサポートするすべてのHTTPメソッドを返します。|
|非公開（公開でない）リソースへのAuthorizationヘッダなしでのOPTIONSリクエスト|PersoniumがサポートしうるすべてのHTTPメソッドを返します。|
|非公開リソースへの有効な※AuthorizationヘッダつきでのOPTIONSリクエスト|そのリソースがサポートするすべてのHTTPメソッドを返します。|
※ Authorizationヘッダつきのリクエストでは、そのヘッダ内容に応じて以下のエラーとなることもあります。
1. 401: Authorizationヘッダの内容が無効である。
2. 403: アクセス制御等の状況によりリクエストが受け付けられない。（読み取りが許可されていない。）

リクエストURLにて許可をしているリクエストメソッドを返却します。  
次に示すのは、Access-Control-Allow-Methodsのレスポンスヘッダの例です。
```
Access-Control-Allow-Methods: GET, OPTIONS
```
#### Access-Control-Allow-Headers レスポンスヘッダの返却
すべてのAPIにおいて、リクエストヘッダにAccess-Control-Request-Headersを指定した場合、Access-Control-Allow-Headersを返却します。  
次に示すのは、Access-Control-Request-Headersに「sample」を指定した場合のレスポンスヘッダの例です。
```
Access-Control-Allow-Headers: sample
```
### 参考
CORSの詳細については[こちら](http://www.w3.org/TR/cors/)を参照してください。

