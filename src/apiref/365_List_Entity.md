---
id: 365_List_Entity
title: Retrieve List of Entities
sidebar_label: Retrieve List of Entities
---

## Overview

Retrieve a list of Entities from an Entity Set defined in an OData Service Collection.

### Required Privileges

read

### Restrictions

* Array of Edm.DateTime type is not supported
* If SYSUTCDATETIME () is specified as the property of Edm.DateTime type, the set system time may be different
  * When setting in request body and setting with DefaultValue (\_\_published, \_\_ updated is the latter timing)
* For EntityType, you can create up to 400 DynamicProperty / DeclaredProperty / ComplexTypeProperty


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}
```

|Path|Overview|
|:--|:--|
|{CellName}|Cell Name|
|{BoxName}|Box Name|
|{ODataCollecitonName}|Collection Name|
|{EntityTypeName}|EntityType name|

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

#### OData Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Specify the format of the response body|application/json|No|When omitted, treat it as [application/json]|
|If-None-Match|Specify the value of ETag, if there is no change, 304, if it is changed return the latest resource||No|Specified when acquiring Entity not matching ETag<br>Not compatible|

## Response

### Response Code

200

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|Version information of ODataProtocol|Return only when user data can be normally acquired|

### Response Body

The response is a JSON object, the correspondence between the key (name) and type defined in the object (subobject) and the value are as follows

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{3}|type|string|UserData.{EntityTypeName}|
|{2}|__id|string|EntityID(__id)|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{2}|_{NP name}|string|Object{4}<br>It is returned only when Link is connected. {NP name}: NavigationPropert name|
|{4}|__deferred|object|Object{5}|
|{5}|uri|string|uri of the resource that has the relationship<br>Not tested|
|{1}|__count|string|Get number of results in $inlinecount query|

Return items that were schema-set other than the above, or dynamic items specified at registration

#### Numerical treatment

#### Decimal value (Edm.Single type)

* The handling when acquiring UserOData in JSON format is as follows
    * The value that the decimal part such as 10.0 becomes 0 is returned as an integer value

#### Numerical value (Edm.Double type)

\*Double type handling in Personium follows the Java Double specification

* The handling when acquiring UserOData in JSON format is as follows
    * The value that the decimal part such as 10.0 becomes 0 is returned as an integer value
* About the value to be returned
    * When the input value at the time of registration is a number having accuracy of double precision or more, data is registered by being rounded to double precision
        * Internally, it is managed as a floating point number, but at the time of output, it converts it to fixed point number representation within the range where no information drop occurs and outputs it  
            When output fixed-point number is used for input, the same number of inputs and original number is guaranteed

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')",
          "etag": "W/\"1-1487662179733\"",
          "type": "UserData.entity-type1"
        },
        "__id": "100-1_20101108-111352093",
        "__published": "/Date(1487662179733)/",
        "__updated": "/Date(1487662179733)/",
        "PetName": null,
        "animalId": "100-1",
        "endedAt": "",
        "episodeType": "care",
        "name": "episode",
        "outcome": "During treatment",
        "startedAt": "2010-11-08"
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')",
          "etag": "W/\"1-1487664427226\"",
          "type": "UserData.entity-type1"
        },
        "__id": "100-1_20101108-111352093",
        "__published": "/Date(1487664427226)/",
        "__updated": "/Date(1487664427226)/",
        "PetName": null
      }
    ]
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/collection1/entity-type1" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


