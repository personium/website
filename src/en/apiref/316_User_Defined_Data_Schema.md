# Retrieve schema ($ metadata)

## Overview

Retrieve schema information for schema definition of user data

### Required Privileges

read


## Request

### Request URL

```
{CellURL}{BoxName}/{OdataCollectionName}/$metadata
```

### Request Method

GET

### Request Query

Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

### Request Body

None


## Response

### Response Code

200

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData version information||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

Response sample reference

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```xml
<?xml version="1.0" encoding="utf-8"?>
<edmx:Edmx Version="1.0" xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" 
xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" 
xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:p="urn:x-personium:xmlns">
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
        <Property Name="__published" Type="Edm.DateTime" Nullable="false" DefaultValue="SYSUTCDATETIME()" 
Precision="3"></Property>
        <Property Name="__updated" Type="Edm.DateTime" Nullable="false" DefaultValue="SYSUTCDATETIME()" 
Precision="3"></Property>
        <Property Name="TestProperty" Type="Edm.String" Nullable="true"></Property>
        <NavigationProperty Name="_TestEntity" Relationship="UserData.TestEntity-TestEntity-assoc" 
FromRole="TestEntity:TestAssociationEndFrom" ToRole="TestEntity:TestAssociationEndTo"></NavigationProperty>
      </EntityType>
      <Association Name="TestEntity-TestEntity-assoc">
        <End Role="TestEntity:TestAssociationEndFrom" Type="UserData.TestEntity" Multiplicity="1"></End>
        <End Role="TestEntity:TestAssociationEndTo" Type="UserData.TestEntity" Multiplicity="0..1"></End>
      </Association>
      <EntityContainer Name="UserData" m:IsDefaultEntityContainer="true">
        <EntitySet Name="TestEntity" EntityType="UserData.TestEntity"></EntitySet>
        <AssociationSet Name="TestEntity-TestEntity-assoc" Association="UserData.TestEntity-TestEntity-assoc">
          <End Role="TestEntity:TestAssociationEndFrom" EntitySet="TestEntity"></End>
          <End Role="TestEntity:TestAssociationEndTo" EntitySet="TestEntity"></End>
        </AssociationSet>
      </EntityContainer>
    </Schema>
  </edmx:DataServices>
</edmx:Edmx>
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA'
```

