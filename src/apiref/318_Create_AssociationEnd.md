---
id: 318_Create_AssociationEnd
title: Create AssociationEnd
sidebar_label: Create AssociationEnd
---

## Overview

Register user data AssociationEnd

### Required Privileges

alter-schema

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error
* AssociationEnd restriction
    * When AssociationEnd specifies"1"in Multiplicity, it operates as "0..1".


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata/AssociationEnd
```

### Request Method

POST

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

#### OData Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

#### OData Create Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|AssociationName|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_")<br>However, the string cannot start with a single-byte hyphen ("-") or underscore ("\_")|Yes||
|Multiplicity|Multiplicity|"0 .. 1" / "1" / "*"|Yes||
|_EntityType.Name|EntityType name of relation target|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_")<br>However, the string cannot start with a single-byte hyphen ("-") or underscore ("\_")<br>Explanation: Registered EntityType by EntityType registration API|Yes||

### Request Sample

```JSON
{
   "Name": "association-end1",
  "Multiplicity": "1",
  "_EntityType.Name": "entity-type1"  
}
```


## Response

### Response Code

201

### Response Header

#### Common Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

#### OData Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|Location|URL to the resource that was created||
|DataServiceVersion|OData version||
|ETag|Resource version information||

### Response Body

#### Common

The response is a JSON object, the correspondence between the key (name) and type defined in the object (subobject) and the value are as follows

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

#### AssociationEnd Individual response body

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|{3}|type|string|ODataSvcSchema.AssociationEnd|
|{2}|Name|string|AssociationEndName|
|{2}|Multiplicity|string|Multiplicity|
|{2}|_EntityType.Name|string|EntityType name of relation target|

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name='entity-type1')",
        "etag": "W/\"1-1487652733383\"",
        "type": "ODataSvcSchema.AssociationEnd"
      },
      "Name": "association-end1",
      "Multiplicity": "1",
      "_EntityType.Name": "entity-type1",
      "__published": "/Date(1487652733383)/",
      "__updated": "/Date(1487652733383)/"
    }
  }
}
```

## Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/AssociationEnd" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{ "Name": "association-end1", "Multiplicity": "1", "_EntityType.Name": "entity-type1"}'
```

