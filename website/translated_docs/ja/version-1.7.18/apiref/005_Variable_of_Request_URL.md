---
id: version-1.7.18-005_Variable_of_Request_URL
title: リクエストURLの変数一覧
sidebar_label: リクエストURLの変数一覧
---
## 概要
APIリファレンスのリクエストURLで使われている変数についての説明

## 変数一覧

|変数名|概要|備考|
|:--|:--|:--|
|{UnitURL}|Unitにアクセスする為のURL|URL:https&#58;//{UnitFQDN}/|
|{UnitFQDN}|Personiumが動作しているサーバのFQDN<br>Unitとは複数のCellをホストするサーバを指す||
|{CellName}|Cell名<br>Cellとはデータ主体ごとのData Stroreを指す||
|{CellURL}|Cellにアクセスする為のURL<br>CellURLには"path based cell URL"と"per cell FQDN URL"の2種類が存在し、[プロパティ](../../server-operator/unit_config_list.md)(pathBasedCellUrl.enabled)で切替可能|path based cell URL:https&#58;//{UnitFQDN}/{CellName}/<br>per cell FQDN URL:https&#58;//{CellName}.{UnitFQDN}/|
|{BoxName}|Box名<br>Boxとはアプリケーションに用いるデータを格納する領域を指す||
|{SchemaURL}|SchemaのURL<br>SchemaとはPersonium内に格納されたSchemaを指す||
|{RoleName}|Role名<br>RoleとはCellに対して定義される有効な「役割」を指す||
|{AccountName}|Account名<br>AccountとはCellでのユーザ認証手段を表す||
|{ExtCellURL}|ExtCellのURL<br>ExtCell（外部Cell）とはあるCellから見たとき外にある他のCellを指す||
|{RelationName}|Relation名<br>Relationとは自身（自Cell）と他者（外部Cell）との関係を示す||
|{ExtRoleURL}|ExtRoleのURL<br>ExtRole（外部Role）とは特定の関係にある外部Cell群において特定の役割（Role）を付与された利用者主体を指す||
|{LogName}|ログファイル名||
|{MessageID}|MessageのID<br>MessageとはCell間で送受信可能なメッセージを指す||
|{CollectionName}|Collection名<br>Collectionとは通常のファイルシステムでいうところのフォルダ・ディレクトリに相当する||
|{ResourcePath}|リソースへのパス<br>Box配下のCollectionとファイルが対象となる|有効値 桁数:1&#65374;256|
|{OdataCollectionName}|OdataCollection名<br>OdataCollectionとはユーザがODataプロトコルで任意のリレーショナルデータを扱うための特殊WebDAV拡張コレクションを指す||
|{EntityTypeName}|EntityType名<br>EntityTypeとはデータの構造をEntityDataModel(EDM)であらわすための定義体を指す|Entityの上位概念|
|{AssociationEndName}|AssociationEnd名<br>AssociationEndとはAssociationを構成するエンドポイントとなっているEntityTypeを指す||
|{ComplexTypeName}|ComplexType名<br>ComplexTypeとは下位属性を伴った属性を持つPropertyを指す|ComplexTypePropertyの上位概念|
|{PropertyName}|Property名<br>各EntityTypeの列頭の値を指し、RDBにおけるテーブルの項目名に相当する||
|{ComplexTypePropertyName}|ComplexTypeProperty名<br>ComplexTypePropertyとはComplexTypeの下位属性の名称を指す|ComplexTypeの下位属性|
|{EntityName}|Entity名<br>Entityとはデータの記録構造を指し、RDBにおけるテーブル1行分に相当する|EntityTypeの下位属性|
|{EntityID}|EntityのID||
|{NavigationPropertyName}|NavigationProperty名<br>NavigationPropertyとはEntityDataModelやODataのデータ構造において、Associationの一方のEndから別のEndへのナビゲーションを表すPropertyを指す||
|{ServiceSourceName}|ServiceSource名<br>ServiceとはServiceCollectionに登録されたユーザ定義のサーバサイドロジックを指す||
|{ServiceName}|Service名<br>Serviceを実行する際に用いられる|ServiceSource名から拡張子を除いたもの|
|{QueueName}|Queue名|文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)<br>ただし、先頭文字に-(半角ハイフン)と_(半角アンダーバー)は指定不|
|{TopicName}|Topic名|文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)<br>ただし、先頭文字に-(半角ハイフン)と_(半角アンダーバー)は指定不可|
