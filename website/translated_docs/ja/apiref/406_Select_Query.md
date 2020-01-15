---
id: 406_Select_Query
title: $select クエリ
sidebar_label: $select クエリ
---
## 概要
返却するプロパティを指定する場合、$selectクエリを使用する  
省略した場合は、取得したすべてのプロパティを返却する  
ただし、以下のプロパティについては$selectに指定しなくても、必ず返却する  
* \__id
* \__published
* \__updated
* \__metadata

※$selectに存在しないプロパティ名を指定した場合、指定された項目を無視する  
※$selectで指定したDynamicプロパティの値がnullの場合は、プロパティ値を取得することはできない  
※プロパティ名は「'」(シングルクォート)で囲わずに指定する
## リクエストクエリ
```
$select={propertyName}
```
※省略時は $select=* となる

|Path|概要|
|:--|:--|
|{PropertyName}|返却するプロパティ名<br>複数指定する場合はカンマ区切りで指定する|
## cURLサンプル
例：Box一覧を取得する際、Nameプロパティのみ返却する場合:
```sh
curl "https://cell1.unit1.example/__ctl/Box?\$select=Name" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```
例：Box一覧を取得する際、全プロパティを返却する場合:
```
curl "https://cell1.unit1.example/__ctl/Box?\$select=*" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```


