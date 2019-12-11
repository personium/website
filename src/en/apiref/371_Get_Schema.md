# Schema acquisition ($metadata)

## Overview

Retrieve schema information

### Required Privileges

read

### Restrictions

* The normal type of the response body is XML format, and the response header Content-Type is application/xml
* The abnormality system of the response body is assumed to be JSON format, and the Content-Type of the response header is set to application/json
* If $format is atomsvc or Accept header is application/atomsvc+xml, Schema's Atom ServiceDocument is returned
* If $format is not atomsvc and Accept header is not application/atomsvc+xml, EDMX of user data is returned
* ComplexType and Documentation tags do not correspond and do not return


## Request

### Request URL

```
{CellURL}{BoxName}/{odataname}/$metadata
```

### Request Method

GET

### Request Query

#### Common Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

#### Individual Query

If atomsvc is specified for $format, return Schema's Atom ServiceDocument  
Ignore others

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

#### Individual request header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Format of data to be returned|application/atomsvc+xml<br>application/xml|No|If not specified, the schema information of the user data schema will be acquired|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {Authentication token}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

None


## Response

### Response Code

200

### Response Header

#### Common Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|If not specified, the latest API version is specified|

#### Schema acquisition specific response header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData version||

### Response Body

#### For user data

|URI|Overview|Reference prefix|
|:--|:--|:--|
|http://schemas.microsoft.com/ado/2007/06/edmx|edmx namespace|edmx:|
|http://schemas.microsoft.com/ado/2007/08/dataservices|WCF Data Services namespace|d:|
|http://schemas.microsoft.com/ado/2007/08/dataservices/metadata|WCF Data Services metadata namespace|m:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|
|http://schemas.microsoft.com/ado/2006/04/edm|scheme namespace|-|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

#### Structure of XML

The body is XML (edmx) and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|Edmx|edmx:|Element|Represents the root of the EDMX document and always has one DataServices element in the child||
|Version|edmx:|Attributes|Represents the version of the EDMX document. The attribute value is always '1.0'||
|DataServices|edmx:|Element|Represents a data service, with multiple Schema elements for children||
|DataServiceVersion|m:|Attributes|Represents the version of the data service. The attribute value is always '1.0'||
|Schema|-|Element|It represents the top-level element of the CSDL document, Association / ComplexType <br>EntityType / EntityContainer / Having elements of Documentation||
|Namespace|-|Attributes|A mandatory attribute representing the name of the schema.|You can not use System, Transient, or Edm as the value|
|ComplexType|-|Element|It represents a complex type, and has a child Documentation / Property element||
|Name|-|Attributes|Represents a compound schema name, mandatory attribute|Required only if ComplexType exists in the OData collection|
|Abstract|-|Attributes|Represents data in the form of a property|Displayed only when Abstract exists|
|Documentation|-|Element|Represent a compound type document|Display only when it exists|
|EntityType|-|Element|It represents an entity type and has children elements<br>Documentation / HasStream / BaseType / Key / Property / NavigationProperty||
|HasStream|-|Attributes|Represents whether an entity is associated with a media resource stream||
|BaseType|-|Attributes|Represents the basic type of an entity type||
|Documentation|-|Element|Represent document of entity type||
|Key|-|Element|It represents a key of an entity, and one or more PropertyRefs are always children||
|PropertyRef|-|Element|Represents the reference property of a key||
|Name|-|Attributes|Represents the name of the property being referenced and is a required attribute||
|NavigationProperty|-|Element|Represents a NavigationProperty||
|Name|-|Attributes|It represents the name of the NavigationProperty and it is a required attribute||
|Documentation|-|Element|Represents a document of NavigationProperty||
|Relationship|-|Attributes|Represents the name of the association within the scope of the model and is a required attribute||
|FromRole|-|Attributes|Represents a referencing role||
|ToRole|-|Attributes|Represents a referenced role||
|Association|-|Element|It represents an Association, and has child element of Documentation / End||
|Name|-|Attributes|Represents an AssociationName, mandatory attribute||
|Documentation|-|Element|Represent document of Association|Display only when it exists|
|End|-|Element|Represents the name of the AssociationEnd, mandatory attribute||
|Role|-|Attributes|Represents the name of the AssociationEnd, mandatory attribute||
|Type|-|Attributes|Represents the type of AssociationEnd, mandatory attribute||
|Multiplicity|-|Attributes|Represents the multiplicity of AssociationEnd, mandatory attribute||
|EntityContainer|-|Element|It represents an entity container and has child elements <br>Documentation / EntitySet / FunctionImport / AssociationSet||
|Name|-|Attributes|Represents an EntityContainer name, mandatory attribute||
|IsDefaultEntityContainer|m:|Attributes|Represents the default EntityContainer flag||
|Documentation|-|Element|Represent document of document of EntityContainer||
|EntitySet|-|Element|Represents an EntitySet and has child elements of Documentation||
|Documentation|-|Element|Represent document of document of EntityContainer||
|Name|-|Attributes|Represents an EntitySet and has child elements of Documentation||
|EntityType|-|Attributes|Represents the EntityType of an entity set||
|Name|-|Attributes|Represents an EntitySet name, mandatory attribute||
|FunctionImport|-|Element|Represents a FunctionImport (model declaration function)||
|Name|-|Attributes|Represents a FunctionImport name, mandatory attribute||
|EntitySet|-|Attributes|Represents an entity set of FunctionImport and has elements of Documentation as children|Repeat for existing entity sets|
|ReturnType|-|Attributes|Represents the return type||
|HttpMethod|m:|Attributes|Represent method, mandatory attribute|When FunctionImport exists|
|Documentation|-|Element|Represent document of FunctionImport||
|Parameter|-|Element|Represents FunctionImport arguments||
|Name|-|Attributes|It represents the argument name of the FunctionImport, and mandatory items|When FunctionImport, Parameter exists|
|Type|-|Attributes|It represents the argument type of FunctionImport, and mandatory items|When FunctionImport, Parameter exists|
|Mode|-|Attributes|Represents the mode of the FunctionImport argument, valid values: 'In', 'Out', or 'InOut'||
|Documentation|-|Element|Represent document of FunctionImport argument|Display only when it exists|
|AssociationSet|-|Element|Represents an AssociationSet and has Documentation and two Ends in its child||
|Name|-|Attributes|Represents an AssociationSet name, mandatory attribute||
|Association|-|Attributes|Represents an AssociationSet association, mandatory attributes||
|Documentation|-|Element|Represent document of AssociationSet|Display only when it exists|
|End|-|Element|Represents an AssociationSetEnd, and essential elements||
|Role|-|Attributes|Represents a role, mandatory attributes||
|EntitySet|-|Attributes|Representing an EntitySet, mandatory attributes||

#### Property

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|Property|-|Element|Represents a Property of an EntityType||
|Name|-|Attributes|Represents the name of the Property||
|Type|-|Attributes|Represents the type of Property value||
|Nullable|-|Attributes|Indicates whether null value can be assigned||
|MaxLength|-|Attributes|Represents the maximum allowable length of a Property||
|DefaultValue|-|Attributes|Represents the default value of a Property||
|Precision|-|Attributes|Represents the number of significant digits of a Property||
|Scale|-|Attributes|Represents the number of decimal places of Property||
|CollectionKind|-|Attributes|Represents array type of Property|List if the collection is an array, otherwise None<br>It is not displayed in case of None|
|Format|p:|Attributes|Represents the character format of the Property||
|IsDeclared|p:|Attributes|Represents whether it is a static Property or not|It is displayed with false for dynamic properties, not for static Properties|

#### Documentation

Not compatible

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|Summary|-|Element|Represents a summary of the Document||
|LongDescription|-|Element|Represent Document details||

#### DTD notation

namespace:edmx:

```dtd
<!ELEMENT Edmx (DataServices)>
<!ATTLIST Edmx Version CDDATA "1.0">
<!ELEMENT DataServices (Schema*)>
```

namespace: m:

```dtd
<!ATTLIST DataServices DataServiceVersion CDDATA "1.0">
<!ATTLIST FunctionImport HttpMethod CDDATA #IMPLIED>
<!ATTLIST EntityContainer IsDefaultEntityContainer CDDATA "true">
```

namespace:http://schemas.microsoft.com/ado/2006/04/edm

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
<!ELEMENT EntityType (Documentation?,Key/Property*/NavigationProperty*)>
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

namespace:p:

```dtd
<!ATTLIST Property Format CDDATA #IMPLIED>
```

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

#### For Schema's Atom ServiceDocument

Return the following fixedly.

```xml
<?xml version="1.0" encoding="utf-8"?>
<service xmlns="http://www.w3.org/2007/app" xml:base="https://demo.Personium/kouroki/TestBox/TestOData/$metadata/" 
xmlns:atom="http://www.w3.org/2005/Atom" xmlns:app="http://www.w3.org/2007/app">
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

#### For user data

```xml
<?xml version="1.0" encoding="utf-8"?>
<edmx:Edmx Version="1.0" xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" 
xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" 
xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:p="urn:x-personium:xmlns">
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
        <EntitySet Name="animal" EntityType="UserData.animal"></EntitySet>
        <EntitySet Name="Profile" EntityType="UserData.Profile"></EntitySet>
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

### For Schema's Atom ServiceDocument

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept:application/atomsvc+xml'
```

### For user data

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept:application/xml'
```


