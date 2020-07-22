---
id: version-1.7.21-404_Format_Query
title: $formatクエリ
sidebar_label: $formatクエリ
---
## 概要
$formatクエリを指定すると、クエリオプションによって指定されたメディアタイプでレスポンスが返却される。  
$formatのクエリオプション有効値は下表の通り。

## リクエストクエリ
|$format オプション|レスポンスされるデータの形式|
|:--|:--|
|atom|application/atom+xml|
|xml|application/xml|
|json|application/json|
|上記以外のIANA定義コンテンツ形式|IANA定義コンテンツ形式|
|ある独自ODataサービスに固有のフォーマットを表すサービス特化型の値|IANA定義コンテンツ形式|

## cURLサンプル
例：Cell一覧をJSON形式で取得する場合:
```sh
curl "https://unit1.example/__ctl/Cell?\$format=json" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```


