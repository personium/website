---
id: version-1.7.21-371_Get_Schema
title: スキーマ取得 ($metadata)
sidebar_label: スキーマ取得 ($metadata)
---
## 概要
スキーマ情報を取得する
### 必要な権限
read
### 制限事項
* レスポンスボディの正常系はXML形式とし、レスポンスヘッダのContent-Typeはapplication/xmlとする
* レスポンスボディの異常系はJSON形式とし、レスポンスヘッダのContent-Typeはapplication/jsonとする
* $formatがatomsvcまたはAcceptヘッダがapplication/atomsvc+xmlの場合、SchemaのAtom ServiceDocumentを返却する
* $formatがatomsvcでなく、Acceptヘッダがapplication/atomsvc+xmlでない場合は、ユーザデータのEDMXを返却する
* ComplexTypeおよび、Documentationタグは対応していないため返却しない


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{odataname}/$metadata
```
### メソッド
GET
### リクエストクエリ
#### 共通クエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
#### 個別クエリ
$formatにatomsvcを指定した場合、SchemaのAtom ServiceDocumentを返却する  
その他は無視する
### リクエストヘッダ
#### 共通リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合は、UUIDの独自短縮表現として${4桁}_${18桁}の形式のBase64url文字列を自動採番|
#### 個別リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Accept|返却されるデータの形式|application/atomsvc+xml<br>application/xml|×|指定がない場合、ユーザデータスキーマのスキーマ情報取得となる|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {認証トークン}|×|※認証トークンは認証トークン取得APIで取得したトークン|
### リクエストボディ
なし


## レスポンス
### ステータスコード
200
### レスポンスヘッダ
#### 共通レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|指定がない場合、最新のAPIバージョンが指定される|

#### スキーマ取得固有レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン||
### レスポンスボディ
#### ユーザデータの場合
|URI|概要|参考prefix|
|:--|:--|:--|
|http://schemas.microsoft.com/ado/2007/06/edmx|edmxの名前空間|edmx:|
|http://schemas.microsoft.com/ado/2007/08/dataservices|WCF Data Servicesの名前空間|d:|
|http://schemas.microsoft.com/ado/2007/08/dataservices/metadata|WCF Data Services metadataの名前空間|m:|
|urn&#58;x-personium:xmlns|Personiumの名前空間|p:|
|http://schemas.microsoft.com/ado/2006/04/edm|schemeの名前空間|-|
※ 参考prefixは以下表の可読性を高めるためのもので、このprefix文字列の使用を保証するものでも要求するものでもありません。
#### XMLの構造
ボディはXML(edmx)で、以下のスキーマに従っています。

|ノード名|名前空間|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|Edmx|edmx:|要素|EDMXドキュメントのルートを表し、子に必ず１つのDataServices要素を持つ||
|Version|edmx:|属性|EDMXドキュメントのバージョンを表す。属性値は必ず'1.0'となる||
|DataServices|edmx:|要素|データサービスを表し、子に複数のSchema要素を持つ||
|DataServiceVersion|m:|属性|データサービスのバージョンを表す。属性値は必ず'1.0'となる||
|Schema|-|要素|CSDLドキュメントの最上位要素を表し、子にAssociation・ComplexType・<br>EntityType・EntityContainer・Documentationの要素を持つ||
|Namespace|-|属性|スキーマの名前を表すし、必須な属性。|値として、System、Transient、または Edm を使用することはできない|
|ComplexType|-|要素|複合型を表し、子にDocumentation・Propertyの要素を持つ||
|Name|-|属性|複合のスキーマ名を表し、必須な属性|ODataコレクション内にComplexTypeが存在する場合のみ必須|
|Abstract|-|属性|プロパティの形式のデータを表す|Abstractが存在する場合のみ表示|
|Documentation|-|要素|複合型のドキュメントを表す|存在する場合のみ表示|
|EntityType|-|要素|エンティティ型を表し、子にDocumentation・HasStream・BaseType・<br>Key・Property・NavigationPropertyの要素を持つ||
|HasStream|-|属性|エンティティがメディア リソース ストリームに関連付けられているかを表す||
|BaseType|-|属性|エンティティ型の基本型を表す||
|Documentation|-|要素|エンティティ型のドキュメントを表す||
|Key|-|要素|エンティティのキーを表し、必ず１個以上のPropertyRefが子となる||
|PropertyRef|-|要素|キーの参照プロパティを表す||
|Name|-|属性|参照されているプロパティの名前を表し、必須の属性となる||
|NavigationProperty|-|要素|ナビゲーションプロパティを表す||
|Name|-|属性|ナビゲーションプロパティの名前を表し、必須の属性となる||
|Documentation|-|要素|ナビゲーションプロパティのドキュメントを表||
|Relationship|-|属性|モデルのスコープ内にあるアソシエーションの名前を表し、必須の属性となる||
|FromRole|-|属性|参照元ロールを表す||
|ToRole|-|属性|参照先ロールを表す||
|Association|-|要素|アソシエーションを表し、子にDocumentation・Endの要素を持つ||
|Name|-|属性|アソシエーション名を表し、必須な属性||
|Documentation|-|要素|アソシエーションのドキュメントを表す|存在する場合のみ表示|
|End|-|要素|アソシエーションエンドの名前を表し、必須な属性||
|Role|-|属性|アソシエーションエンドの名前を表し、必須な属性||
|Type|-|属性|アソシエーションエンドの型を表し、必須な属性||
|Multiplicity|-|属性|アソシエーションエンドの多重度を表し、必須な属性||
|EntityContainer|-|要素|エンティティコンテナを表し、子にDocumentation・EntitySet・<br>FunctionImport・AssociationSetの要素を持つ||
|Name|-|属性|エンティティコンテナ名を表し、必須な属性||
|IsDefaultEntityContainer|m:|属性|デフォルトエンティティコンテナフラグを表す||
|Documentation|-|要素|エンティティコンテナのドキュメントのドキュメントを表す||
|EntitySet|-|要素|エンティティセットを表し、子に Documentationの要素を持つ||
|Documentation|-|要素|エンティティコンテナのドキュメントのドキュメントを表す||
|Name|-|属性|エンティティセットを表し、子に Documentationの要素を持つ||
|EntityType|-|属性|エンティティセットのエンティティタイプを表す||
|Name|-|属性|エンティティセット名を表し、必須な属性||
|FunctionImport|-|要素|関数インポート（モデル宣言関数）を表す||
|Name|-|属性|関数インポート名を表し、必須な属性||
|EntitySet|-|属性|関数インポートのエンティティセットを表し、子に Documentationの要素を持つ|存在するエンティティセット分 繰り返す|
|ReturnType|-|属性|戻り値の型を表す||
|HttpMethod|m:|属性|メソッドを表し、必須な属性|FunctionImportが存在する場合|
|Documentation|-|要素|関数インポートのドキュメントを表す||
|Parameter|-|要素|関数インポートの引数を表す||
|Name|-|属性|関数インポートの引数名を表し、必須な項目|FunctionImport、Parameterが存在する場合|
|Type|-|属性|関数インポートの引数の型を表し、必須な項目|FunctionImport、Parameterが存在する場合|
|Mode|-|属性|関数インポートの引数のモードを表し、有効値：'In'、'Out'、または 'InOut'||
|Documentation|-|要素|関数インポートの引数のドキュメントを表す|存在する場合のみ表示|
|AssociationSet|-|要素|アソシエーションセットを表し、子にDocumentationと２つのEndを持つ||
|Name|-|属性|アソシエーションセット名を表し、必須な属性||
|Association|-|属性|アソシエーションセットのアソシエーションを表し、必須な属性||
|Documentation|-|要素|アソシエーションセットのドキュメントを表す|存在する場合のみ表示|
|End|-|要素|アソシエーションセット ENDを表し、必須な要素||
|Role|-|属性|ロールを表し、必須な属性||
|EntitySet|-|属性|エンティティセットを表し、必須な属性||
#### プロパティ
|ノード名|名前空間|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|Property|-|要素|エンティティ型のPropertyを表す||
|Name|-|属性|プロパティの名前を表す||
|Type|-|属性|プロパティ値の型を表す||
|Nullable|-|属性|null 値の割り当ての可否を表す||
|MaxLength|-|属性|プロパティの許容最大長を表す||
|DefaultValue|-|属性|プロパティの既定値を表す||
|Precision|-|属性|プロパティの有効桁数を表す||
|Scale|-|属性|プロパティの小数点以下桁数を表す||
|CollectionKind|-|属性|プロパティの配列種別を表す|コレクションが配列の場合List,それ以外はNone<br>Noneの場合は表示されない|
|Format|p:|属性|プロパティの文字フォーマットを表す||
|IsDeclared|p:|属性|静的プロパティか否かを表す|動的プロパティの場合falseで表示,静的プロパティの場合は表示されない|
#### ドキュメンテーション
未対応

|ノード名|名前空間|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|Summary|-|要素|ドキュメントのサマリを表す||
|LongDescription|-|要素|ドキュメントの詳細を表す||
#### DTD表記
名前空間:edmx:
```dtd
<!ELEMENT Edmx (DataServices)>
<!ATTLIST Edmx Version CDDATA "1.0">
<!ELEMENT DataServices (Schema*)>
```
名前空間: m:
```dtd
<!ATTLIST DataServices DataServiceVersion CDDATA "1.0">
<!ATTLIST FunctionImport HttpMethod CDDATA #IMPLIED>
<!ATTLIST EntityContainer IsDefaultEntityContainer CDDATA "true">
```
名前空間:http://schemas.microsoft.com/ado/2006/04/edm
```dtd
<!ELEMENT Schema (Association*,ComplexType*,EntityType*,EntityContainer*)>
<!ATTLIST Schema Namespace CDDATA #REQUIRED>
<!ELEMENT ComplexType (Documentation?,Property*)>
<!ATTLIST ComplexType Name CDDATA #IMPLIED
                      Abstract CDDATA #IMPLIED>
<!ELEMENT Documentation (Summary?,LongDescription?)>
<!ELEMENT Summary (#PCDATA)>
<!ELEMENT LongDescription (#PCDATA)>
<!ELEMENT Property EMPTY>
<!ATTLIST Property Name CDDATA #REQUIRED
                   Type CDDATA #REQUIRED
                   Nullable CDDATA (true|false) #REQUIRED
                   MaxLength CDDATA #IMPLIED
                   DefaultValue CDDATA #IMPLIED
                   Precision CDDATA #IMPLIED
                   Scale CDDATA #IMPLIED
                   CollectionKind (List|None) #IMPLIED>
<!ELEMENT EntityType (Documentation?,Key・Property*・NavigationProperty*)>
<!ATTLIST EntityType OpenType (true|false) #REQUIRED
                     HasStream CDDATA #IMPLIED
                     BaseType CDDATA #IMPLIED>
<!ELEMENT Key (PropertyRef*)>
<!ELEMENT PropertyRef ENPTY>
<!ATTLIST PropertyRef Name CDDATA #REQUIRED>
<!ELEMENT NavigationProperty (Documentation?)>
<!ATTLIST PropertyRef Name CDDATA #REQUIRED
                      Relationship CDDATA #REQUIRED
                      FromRole CDDATA #REQUIRED
                      ToRole  CDDATA #REQUIRED>
<!ELEMENT Association (Documentation?|End+)>
<!ATTLIST Association Name CDDATA #REQUIRED>
<!ELEMENT End ENPTY>
<!ATTLIST End Role CDDATA #REQUIRED
          Type CDDATA #REQUIRED
          Multiplicity ("1","0..1","*") #REQUIRED>
<!ELEMENT EntityContainer (Documentation?|EntitySet*|FunctionImport*|AssociationSet*)>
<!ATTLIST FunctionImport Name CDDATA #REQUIRED
                         EntitySet CDDATA #IMPLIED
                         ReturnType CDDATA #IMPLIED>
<!ELEMENT Parameter (Documentation?)>
<!ATTLIST Parameter Name CDDATA #REQUIRED
                    Type CDDATA #REQUIRED
                    Mode  ("In","Out","InOut") #IMPLIED>
<!ELEMENT AssociationSet (Documentation?|End+)>
<!ATTLIST AssociationSet Name CDDATA #REQUIRED
                         Association CDDATA #REQUIRED>
<!ELEMENT End (Documentation?)>
<!ATTLIST End Role CDDATA #IMPLIED
              EntitySet CDDATA #REQUIRED>
```
名前空間:p:
```dtd
<!ATTLIST Property Format CDDATA #IMPLIED>
```
### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
#### SchemaのAtom ServiceDocumentの場合
以下を固定で返却する。
```xml
<?xml version="1.0" encoding="utf-8"?>
<service xmlns="http://www.w3.org/2007/app" xml:base="https://demo.Personium/kouroki/TestBox
/TestOData/$metadata/" xmlns:atom="http://www.w3.org/2005/Atom" 
xmlns:app="http://www.w3.org/2007/app">
  <workspace>
    <atom:title>Default</atom:title>
    <collection href="EntityType">
      <atom:title>EntityType</atom:title>
    </collection>
    <collection href="AssociationEnd">
      <atom:title>AssociationEnd</atom:title>
    </collection>
    <collection href="ComplexTypeProperty">
      <atom:title>ComplexTypeProperty</atom:title>
    </collection>
    <collection href="Property">
      <atom:title>Property</atom:title>
    </collection>
    <collection href="ComplexType">
      <atom:title>ComplexType</atom:title>
    </collection>
  </workspace>
</service>
```
#### ユーザデータの場合
```xml
<?xml version="1.0" encoding="utf-8"?>
<edmx:Edmx Version="1.0" xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" 
xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m=
"http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:p="urn:x-personium:xmlns">
  <edmx:DataServices m:DataServiceVersion="1.0">
    <Schema xmlns="http://schemas.microsoft.com/ado/2006/04/edm" Namespace="UserData">
      <ComplexType Name="Address"></ComplexType>
      <ComplexType Name="TestComplexType">
        <Property Name="TestComplexTypeProperty" Type="Edm.String" Nullable="true"></Property>
      </ComplexType>
      <EntityType Name="TestEntity" OpenType="true">
        <Key>
          <PropertyRef Name="__id"></PropertyRef>
        </Key>
        <Property Name="__id" Type="Edm.String" Nullable="false" DefaultValue="UUID()" p:Format=
"regEx('^[a-zA-Z0-9][a-zA-Z0-9-_:]{0,199}$')"></Property>
        <Property Name="__published" Type="Edm.DateTime" Nullable="false" DefaultValue=
"SYSUTCDATETIME()" Precision="3"></Property>
        <Property Name="__updated" Type="Edm.DateTime" Nullable="false" DefaultValue=
"SYSUTCDATETIME()" Precision="3"></Property>
        <Property Name="TestProperty" Type="Edm.String" Nullable="true"></Property>
        <NavigationProperty Name="_TestEntity" Relationship="UserData.TestEntity-TestEntity-assoc" 
FromRole="TestEntity:TestAssociationEndFrom" ToRole="TestEntity:TestAssociationEndTo">
        </NavigationProperty>
      </EntityType>
      <Association Name="TestEntity-TestEntity-assoc">
        <End Role="TestEntity:TestAssociationEndFrom" Type="UserData.TestEntity" Multiplicity="1">
        </End>
        <End Role="TestEntity:TestAssociationEndTo" Type="UserData.TestEntity" Multiplicity="0..1">
        </End>
      </Association>
      <EntityContainer Name="UserData" m:IsDefaultEntityContainer="true">
        <EntitySet Name="TestEntity" EntityType="UserData.TestEntity"></EntitySet>
        <EntitySet Name="animal" EntityType="UserData.animal"></EntitySet>
        <EntitySet Name="Profile" EntityType="UserData.Profile"></EntitySet>
        <AssociationSet Name="TestEntity-TestEntity-assoc" Association=
"UserData.TestEntity-TestEntity-assoc">
          <End Role="TestEntity:TestAssociationEndFrom" EntitySet="TestEntity"></End>
          <End Role="TestEntity:TestAssociationEndTo" EntitySet="TestEntity"></End>
        </AssociationSet>
      </EntityContainer>
    </Schema>
  </edmx:DataServices>
</edmx:Edmx>

```


## cURLサンプル
### SchemaのAtom ServiceDocumentの場合
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept:application/atomsvc+xml'
```
### ユーザデータの場合
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept:application/xml'
```

