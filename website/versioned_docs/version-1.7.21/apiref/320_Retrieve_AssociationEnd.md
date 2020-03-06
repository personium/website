---
id: version-1.7.21-320_Retrieve_AssociationEnd
title: Retrieve AssociationEnd
sidebar_label: Retrieve AssociationEnd
original_id: 320_Retrieve_AssociationEnd
---

## Overview

Retrieve existing AssociationEnd information

### Required Privileges

read

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata/AssociationEnd(Name='{AssociationEndName}',_EntityType.Name='{EntityTypeName}')
```

### Request Method

GET

### Request Query

The following query parameters are available

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

[$select  Query](406_Select_Query.md)

[$expand  Query](405_Expand_Query.md)

[$format  Query](404_Format_Query.md)

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

#### OData Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

#### OData Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|
|If-None-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

None


## Response

### Response Code

200

### Response Header

None

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

#### AssociationEnd unique response body

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
      "__updated": "/Date(1487652733383)/",
      "_EntityType": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name='entity-type1')/_EntityType"
        }
      },
      "_AssociationEnd": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name='entity-type1')/_AssociationEnd"
        }
      }
    }
  }
}
```

## Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/AssociationEnd\
(Name='association-end1',_EntityType.Name='entity-type1')" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

