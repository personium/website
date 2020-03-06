---
id: version-1.7.21-403_Filter_Query
title: $filterクエリ
sidebar_label: $filterクエリ
---
## 概要
一覧取得時に検索条件を指定する場合は$filterクエリを使用する
## 指定可能な型
|型|記述例|備考|
|:--|:--|:--|
|文字列|'StringValue'||
|数値|100||
|真偽値|true<br>false||
|日付|datetime'2017-12-15T09:39:10'<br>datetimeoffset'2017-12-15T18:39:10+09:00'|datetimeはタイムゾーンオフセットを指定不可。<br>タイムゾーンオフセットが指定されていない場合はUTCとして扱う。|

## Operator Support
|演算子|意味|記述例|備考|
|:--|:--|:--|:--|
|eq|等号|$filter=itemKey eq 'searchValue'|文字列、数値、真偽値、日付、nullに対応|
|ne|否定等号|$filter=itemKey ne 'searchValue'|文字列、数値、真偽値、日付、nullに対応|
|gt|より大きい|$filter=itemKey gt 1000|文字列、数値、日付に対応|
|ge|以上|$filter=itemKey ge 1000|文字列、数値、日付に対応|
|lt|より小さい|$filter=itemKey lt 1000|文字列、数値、日付に対応|
|le|以下|$filter=itemKey le 1000|文字列、数値、日付に対応|
|and|論理積|$filter=itemKey1 eq 'searchValue1' and itemKey2 eq 'searchValue2'||
|or|論理和|$filter=itemKey1 eq 'searchValue1' or itemKey2 eq 'searchValue2'||
|()|優先グループ|$filter=itemKey eq 'searchValue' or (itemKey gt 500 and itemKey lt 1500)|括弧が片方のみの場合、括弧は無視される|
## サポート関数
|Function|概要|Example|備考|
|:--|:--|:--|:--|
|startswith|前方一致|$filter=startswith(itemKey, 'searchValue')|文字列のみ対応|

※ 部分一致、後方一致は未対応

## プロパティ型別の検索仕様
### Edm.String型
検索に指定したキーワードを文字列型に変換して検索する
### Edm.Int32型
整数値またはnullが指定可能  
文字列型で整数値を指定された場合は数値型に変換して検索する
### Edm.Single型
整数、小数値またはnullが指定可能  
文字列型で整数、小数値を指定された場合は小数値に変換して検索を行う
### Edm.Boolean型
真偽値またはnullが指定可能
### Edm.DateTime型
日付またはnullが指定可能  
整数値が指定された場合はUNIX時間に変換して検索を行う

## 特記事項
※クエリを指定する際はURLエンコードが必要  
※検索対象のプロパティの有効値は半角英数字と-(半角ハイフン),\_(半角アンダーバー)が有効。  
※検索文字列にシングルクオートを含めたい場合、シングルクオートを２個「''」記述することでシングルクオートを検索文字列に指定することができる  
※$filterに存在しないプロパティ名を指定した場合、そのプロパティ名を無視して検索を行う  
## cURLサンプル
例：セル名がsampleのセルを取得する場合:
```sh
curl "https://unit1.example/__ctl/Cell?\$filter=Name%20eq%20'sample'" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json'
```

