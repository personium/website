---
id: version-1.7.21-402_Skip_Query
title: $skip クエリ
sidebar_label: $skip クエリ
---
## 概要
$skipクエリは、コレクションのうち指定した自然数Nの数だけ省き、N+1件目からの情報を取得する際に用いる。  
以下の表記で記述する。
```
$skip={number}
```
## cURLサンプル
例：10Cellの取得を省き、11Cell目からの情報を取得する場合:
```sh
curl "https://unit1.example/__ctl/Cell?\$skip=10" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json'
```

