# スキーマ取得（$metadata）
## 概要
ユーザデータのスキーマ定義を行うためのスキーマ情報を取得する

### 必要な権限
read


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{OdataCollectionName}/$metadata
```
### メソッド
GET

### リクエストクエリ
共通リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ
#### 共通リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
### リクエストボディ
なし


## レスポンス
### ステータスコード
200

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
|DataServiceVersion|ODataのバージョン情報||
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"*"固定|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|

### レスポンスボディ
レスポンスサンプル参照

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
```xml
<?xml version="1.0" encoding="utf-8"?>
<edmx:Edmx Version="1.0" xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" 
xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" 
xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" 
xmlns:p="urn:x-personium:xmlns">
  <edmx:DataServices m:DataServiceVersion="1.0">
    <Schema xmlns="http://schemas.microsoft.com/ado/2006/04/edm" Namespace="UserData">
      <ComplexType Name="TestComplexType">
        <Property Name="TestComplexTypeProperty" Type="Edm.String" Nullable="true"></Property>
      </ComplexType>
      <EntityType Name="TestEntity" OpenType="true">
        <Key>
          <PropertyRef Name="__id"></PropertyRef>
        </Key>
        <Property Name="__id" Type="Edm.String" Nullable="false" DefaultValue="UUID()" 
p:Format="regEx('^[a-zA-Z0-9][a-zA-Z0-9-_:]{0,199}$')"></Property>
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

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA'
```

