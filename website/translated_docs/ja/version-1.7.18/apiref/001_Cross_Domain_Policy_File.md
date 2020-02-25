---
id: version-1.7.18-001_Cross_Domain_Policy_File
title: クロスドメインポリシーファイル
sidebar_label: クロスドメインポリシーファイル
---
## 概要
クロスドメインポリシーファイル(crossdomain.xml)を取得します。  
クロスドメインポリシーファイルはすべての利用者が取得できます。

## リクエスト
### リクエストURL
```
/crossdomain.xml
```
### メソッド
GET
### リクエストクエリ
なし
### リクエストヘッダ
なし
### リクエストボディ
なし

## レスポンス
### ステータスコード
200
### レスポンスヘッダ
なし
### レスポンスボディ
XML形式

|項目名|概要|
|:--|:--|
|/cross-domain-policy/site-control|メタポリシーの許可設定情報。固定で属性値「permitted-cross-domain-policies="all"」を返却する|
|/cross-domain-policy/allow-access-from|現在のドメインにアクセス可能なドメイン。固定で属性値「domain="*"」を返却する|
|/cross-domain-policy/allow-http-request-headers-from|現在のドメインに送信可能なヘッダ情報と、ヘッダ送信元ドメイン。固定で属性値「domain="\*" headers="*"」を返却する|
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル
```sh
curl "https://unit1.example/crossdomain.xml" -X GET -i
```

