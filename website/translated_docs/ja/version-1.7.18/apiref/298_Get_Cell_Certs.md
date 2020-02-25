---
id: version-1.7.18-298_Get_Cell_Certs
title: Cell公開鍵取得
sidebar_label: Cell公開鍵取得
---
## 概要
OpenID ConnectのID Tokenの検証に利用可能な公開鍵情報を取得する。  
公開鍵情報には、以下の情報が含まれる。

* キータイプ
* 署名アルゴリズム
* キーID
* Modulus (RSA)
* Exponent (RSA)

### 必要な権限
なし


## リクエスト
### リクエストURL
```
{CellURL}/__certs
```

### メソッド
GET

### リクエストクエリ
なし

### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Accept|レスポンスボディの形式を指定する|application/json|x||


## レスポンス
### ステータスコード
200

### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|Personium APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
レスポンスはJSON形式で、オブジェクト（サブオブジェクト）に定義される。  
キー(名前)と型、並びに値の対応は以下のとおり。  

|オブジェクト|名前(キー)|型|値|備考|
|:--|:--|:--|:--|:--|
|ルート|keys|array|key情報配列||
|keys|kty|string|"RSA"||
|keys|alg|string|"RS256"||
|keys|kid|string|key id|key情報が複数ある場合の識別に利用可能|
|keys|n|string|RSA Modulus||
|keys|e|string|RSA Exponent||

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```JSON
{
  "keys": [
    {
      "kty": "RSA",
      "alg": "RS256",
      "kid": "fdef9343-68e7-4104-b817-81fe933ae2a0",
      "n": "k5~(省略)",
      "e": "AQAB"
    }
  ]
}
```

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__certs" -X GET -i -H 'Accept: application/json'
```
