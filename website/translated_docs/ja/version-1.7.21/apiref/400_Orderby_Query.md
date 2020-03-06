---
id: version-1.7.21-400_Orderby_Query
title: $orderby クエリ
sidebar_label: $orderby クエリ
---
## 概要
一覧取得時に検索結果を並べ替える場合は$orderbyクエリを使用する  
※$orderbyに存在しないプロパティ名を指定した場合は、指定された項目を無視する
## リクエストクエリ
```
$orderby={propertyName} {option}, ・・・
```
※ {propertyName} {option}はカンマ区切りで複数指定可能

|Path|概要|
|:--|:--|
|{PropertyName}|並び替えのキーに指定するプロパティ名|
|{Option}|並び替え方法<br>asc:昇順<br>desc:降順<br>デフォルト値:asc|
## cURLサンプル
例：セル情報をセル名の降順で取得する場合:
```sh
curl "https://unit1.example/__ctl/Cell?\$orderby=Name%20desc" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```
## 動作詳細
* null値を含む場合のソート順序  
	昇順を指定した場合、降順を指定した場合ともにnullはソート結果の末尾になるようにソートします。  
	※ただし、マイナーバージョン 0.19.9を使用している場合は、以下の規則に従いソートします。

* 文字列型に対するソート
	* asc
		null⇒文字列
	* desc
		文字列⇒null
* 数値型
	* asc
		負数⇒null⇒0⇒なし⇒正数
	* desc
		正数⇒null⇒0⇒なし⇒負数

* $orderbyに存在しないプロパティ名を指定した場合は、指定された項目を無視する
* $orderbyに配列型のプロパティ名を指定した場合は、400エラーを返却する


