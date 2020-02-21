---
id: version-1.7.18-319_List_AssociationEnd
title: Retrieve List of AssociationEnd
sidebar_label: Retrieve List of AssociationEnd
original_id: 319_List_AssociationEnd
---

## Overview

Obtain a list of existing AssociationEnd information

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
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata/AssociationEnd
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

[$filter  Query](403_Filter_Query.md)

[$inlinecount  Query](407_Inlinecount_Query.md)

[$orderby  Query](400_Orderby_Query.md)

[$top  Query](401_Top_Query.md)

[$skip  Query](402_Skip_Query.md)

[Full-text Search (q) Query](408_Full_Text_Search_Query.md)

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

#### OData Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

#### OData ListRequest Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

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


### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name='entity-type1')",
          "etag": "W/\"2-1487587131996\"",
          "type": "ODataSvcSchema.AssociationEnd"
        },
        "Name": "association-end1",
        "Multiplicity": "1",
        "_EntityType.Name": "entity-type1",
        "__published": "/Date(1487587131996)/",
        "__updated": "/Date(1487587131996)/",
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
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end2',_EntityType.Name='entity-type2')",
          "etag": "W/\"1-1487652733383\"",
          "type": "ODataSvcSchema.AssociationEnd"
        },
        "Name": "association-end2",
        "Multiplicity": "*",
        "_EntityType.Name": "entity-type2",
        "__published": "/Date(1487652733383)/",
        "__updated": "/Date(1487652733383)/",
        "_EntityType": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end2',_EntityType.Name='entity-type2')/_EntityType"
          }
        },
        "_AssociationEnd": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end2',_EntityType.Name='entity-type2')/_AssociationEnd"
          }
        }
      }
    ]
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/AssociationEnd" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


