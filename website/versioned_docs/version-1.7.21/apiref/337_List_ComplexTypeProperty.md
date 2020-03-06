---
id: version-1.7.21-337_List_ComplexTypeProperty
title: Retrieve List of ComplexTypeProperty
sidebar_label: Retrieve List of ComplexTypeProperty
original_id: 337_List_ComplexTypeProperty
---

## Overview

Obtain a list of existing ComplexTypeProperty information

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
{CellURL}{BoxName}/{ODataCollecitonName}/$metadata/ComplexTypeProperty
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
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

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

#### Property specific response body

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|{3}|type|string|ODataSvcSchema.ComplexTypeProperty|
|{2}|Name|string|ComplexTypeProperty name|
|{2}|_ComplexType.Name|string|ComplexType name attached|
|{2}|Type|string|Type definition|
|{2}|Nullable|boolean|Null value authorization|
|{2}|DefaultValue|string|Default value|
|{2}|CollectionKind|string|Array type|

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
/ComplexTypeProperty(Name='complex-type-property1',_ComplexType.Name='complex-type1')",
          "etag": "W/\"1-1487587033861\"",
          "type": "ODataSvcSchema.ComplexTypeProperty"
        },
        "Name": "complex-type-property1",
        "_ComplexType.Name": "complex-type1",
        "Type": "Edm.String",
        "Nullable": true,
        "DefaultValue": null,
        "CollectionKind": "None",
        "__published": "/Date(1487587033861)/",
        "__updated": "/Date(1487587033861)/",
        "_ComplexType": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/ComplexTypeProperty(Name='complex-type-property1',_ComplexType.Name='complex-type1')
/_ComplexType"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/ComplexTypeProperty(Name='complex-type-property2',_ComplexType.Name='complex-type2')",
          "etag": "W/\"1-1487658277593\"",
          "type": "ODataSvcSchema.ComplexTypeProperty"
        },
        "Name": "complex-type-property2",
        "_ComplexType.Name": "complex-type2",
        "Type": "Edm.String",
        "Nullable": true,
        "DefaultValue": null,
        "CollectionKind": "None",
        "__published": "/Date(1487658277593)/",
        "__updated": "/Date(1487658277593)/",
        "_ComplexType": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/ComplexTypeProperty(Name='complex-type-property2',_ComplexType.Name='complex-type2')
/_ComplexType"
          }
        }
      }
    ]
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/ComplexTypeProperty" \
-X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

