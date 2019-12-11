# Retrieve service document

## Overview

Retrieve the service document of OData service to perform schema definition of OData Service Collection.

### Required Privileges

read


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata
```

### Request Method

GET

### Request Query

#### Common Request Query

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

#### Individual Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Format of data to be returned|application / atomsvc + xml|Yes|If not specified, the schema information of the user data schema will be acquired|

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
<?xml version='1.0' encoding='utf-8'?>
<service xmlns="http://www.w3.org/2007/app" xml:base="https://cell1.unit1.example/box1/odata-collection1/$metadata/" xmlns:atom="http://www.w3.org/2005/Atom" 
xmlns:app="http://www.w3.org/2007/app">
  <workspace>
    <atom:title>Default </atom:title>
    <collection href="EntityType">
      <atom:title>EntityType </atom:title>
    </collection>
    <collection href="AssociationEnd">
      <atom:title>AssociationEnd </atom:title>
    </collection>
    <collection href="ComplexTypeProperty">
      <atom:title>ComplexTypeProperty </atom:title>
    </collection>
    <collection href="Property">
      <atom:title>Property </atom:title>
    </collection>
    <collection href="ComplexType">
      <atom:title>ComplexType </atom:title>
    </collection>
  </workspace>
</service>
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata' -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/atomsvc+xml'
```


