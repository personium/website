---
id: version-1.7.21-357_Retrieve_Property
title: Retrieve Property
sidebar_label: Retrieve Property
original_id: 357_Retrieve_Property
---

## Overview

Retrieve existing Property information

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
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata/Property(Name='property_name',
_EntityType.Name='{EntityTypeName}')
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
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
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

#### Property specific response body

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|{3}|type|string|ODataSvcSchema.Property|
|{2}|Name|string|Property Name|
|{2}|_EntityType.Name|string|EntityType name to be attached|
|{2}|Type|string|Type definition|
|{2}|Nullable|boolean|Null value authorization|
|{2}|DefaultValue|string|Default value|
|{2}|CollectionKind|string|Array type|
|{2}|IsKey|boolean|Primary key setting|
|{2}|UniqueKey|string|Unique key setting|
|{2}|IsDeclared|boolean|Declared true or false|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/Property
(Name='property1',_EntityType.Name='entity-type1')",
        "etag": "W/\"1-1487635336196\"",
        "type": "ODataSvcSchema.Property"
      },
      "Name": "property1",
      "_EntityType.Name": "entity-type1",
      "Type": "Edm.String",
      "Nullable": true,
      "DefaultValue": null,
      "CollectionKind": "None",
      "IsKey": true,
      "UniqueKey": null,
      "IsDeclared": true,
      "__published": "/Date(1487635336196)/",
      "__updated": "/Date(1487635336196)/",
      "_EntityType": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/Property
(Name='property1',_EntityType.Name='entity-type1')/_EntityType"
        }
      }
    }
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/Property\
(Name='property1',_EntityType.Name='entity-type1')" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


