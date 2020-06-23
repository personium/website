---
id: 401_Top_Query
title: $top クエリ
sidebar_label: $top クエリ
---
## 概要
$topクエリに整数値を指定することで、データ一覧の取得件数を制限することが可能  
登録データ件数が取得件数未満の場合は、全てのデータを取得する  
登録データ件数が取得件数を超える場合は、登録データの先頭から取得件数分までを取得する  
$topクエリで取得したデータはソートされないため、$orderbyクエリなどのソート条件を指定する必要がある

※$topに整数値以外を指定した場合は「400 Bad Request」を返却する

## リクエストクエリ
```
$top={number}
```
|Value|概要|有効値|備考|
|:--|:--|:--|:--|
|{number}|返されるフィードに含まれるエンティティの数を指定する|半角数字の0-10000(デフォルト:25)<br>$expandクエリ指定時は0-100(デフォルト:25)||
## cURLサンプル
例：Cellを10件取得する場合:
```sh
curl "https://unit1.example/__ctl/Cell?\$top=10" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json'
```
## 制限事項
* 処理性能を考慮した場合、$skipクエリと併用する
	この際、$topクエリの推奨値は50以下


