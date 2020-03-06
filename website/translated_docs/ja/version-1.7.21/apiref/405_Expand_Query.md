---
id: version-1.7.21-405_Expand_Query
title: $expand クエリ
sidebar_label: $expand クエリ
---
## 概要
$expandクエリにNavigationProperty名を指定することで、関連情報を展開して取得することが可能。  
一覧取得時の関連情報の展開は最大100件まで展開する。  
一件取得時の関連情報の展開は最大10000件まで展開する。  
$expandで取得した関連データのソート順は下記の通り。  

|関連|ソート条件|順序|
|:--|:--|:--|
|0 .. 1:0 .. 1|展開するナビゲーションプロパティのエンティティ作成日時|降順|
|0 .. 1: *|展開するナビゲーションプロパティのエンティティ作成日時|降順|
|*: 0 .. 1|展開するナビゲーションプロパティのエンティティ作成日時|降順|
|*: *|展開するナビゲーションプロパティとのリンク情報作成日時|降順|
※Multiplicityが"1"の場合は、"0..1"と同様のソート結果となる
## リクエストクエリ
```
$expand={NavigationPropertyName}
```
|Path|概要|
|:--|:--|
|{NavigationPropertyName}|展開するナビゲーションプロパティ名<br>複数指定する場合はカンマ区切りで指定する|
※$expandに存在しないNavigationProperty名を指定した場合は「400 Bad Request」を返却する
### ナビゲーションプロパティ指定可能数
一覧取得時のナビゲーションプロパティは2件まで指定可能  
一件取得時のナビゲーションプロパティは10件まで指定可能  
※指定可能なナビゲーションプロパティ数を超えた場合は「400 Bad Request」を返却する
## cURLサンプル
ナビゲーションプロパティに紐付く情報を展開して取得する
```
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1\
('100-1_20101108-111352093')?\$expand={NavigationPropertyName}" -X GET -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'\
 -H 'Accept: application/json'
```
## 制限事項
* 関連情報の展開は1階層のみ可能
* 展開した関連情報がすべての件数を返却しているかを示すために、\__countを関連情報一覧の項目として追加する（未サポート）


