---
id: 364_Create_Entity
title: Create Entity
sidebar_label: Create Entity
---

## Overview

Create Entity of user data.

### Required Privileges

write

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error
* User data restrictions
    * Property scope of Edm.DateTime type is not properly checked
    * Array of Edm.DateTime type is not supported
    * If SYSUTCDATETIME () is specified as the property of Edm.DateTime type, the set system time may be different
    * \*When setting in request body and setting with DefaultValue (\_\_published, \_\_ updated is the latter timing)
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

POST

### Request Query

#### Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

#### OData Common Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default<br>Not compatible|
|Content-Type|Specifies the request body format|application/json|No|When omitted, treat it as [application/json] <br>Not compatible|

### Request Body

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|__id|EntityID|Number of digits: 1-400<br>String|No|If not specified a unique ID will be assigned|

#### Property

Set up schema-defined properties and dynamic (schema-undefined) properties, up to 400 properties in total  
Contains the number of properties defined by ComplexType in the above

#### Schema-defined properties

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Property associated with EntityType|User defined item|Based on DefaultValue of default value Property|Based on Property Nullable||

#### Valid value of value of schema-defined property

|Data type|Effective Value|
|:--|:--|
|String|Number of digits: 0-51200 byte<br>Character type: When a control code is used as a value of a character string, return it in an escaped state at the time of acquisition<br>When "\\" is used, it must be specified with "\\\\"<br>When an integer value, a decimal value, a boolean value, or a date type value is set in a property of a character string type, it is converted into a character string type and registered|
|Integer value|-2147483648 - 2147483647|
|Decimal point|Number of digits in integer part: 1-5 digits<br>Number of digits in decimal part: 1-5 digits|
|Boolean value|true / false / null(treat null as false)|
|Date|It is specified as a character string in the format of Date ([time of long type])<br>The valid value of [time of long type] is -6847804800000(1753-01-01T00:00:00.000Z)-253402300799999(9999-12-31T23:59:59.999Z)<br>In addition, you can specify the following as reserved words<br>SYSUTCDATETIME (): server time|

### Dynamic (schema undefined) property

Set up schema-defined properties and dynamic (schema-undefined) properties, up to 400 properties in total  
Contains the number of properties defined by ComplexType in the above

#### Valid value of dynamic property's key

|Data type|Effective Value|
|:--|:--|
|String|Number of digits: 1-128 :<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_")<br>However, - (hyphen) and \_ (underscore) can not be specified as the first character <br>_published, _updated is a reserved word, so it is not possible to specify the request body|

#### Valid value of value of dynamic property

Same as valid value of value of schema-defined property  
Array, associative array can not be specified

### Request Sample

```JSON
{"__id": "100-1_20101108-111352093","animalId": "100-1","name": "episode","startedAt": "2010-11-08",
"episodeType": "care","endedAt": "","outcome": "During treatment"}
```

```JSON
{"__id": "100-1_20101108-111352093","animalId": "100-1","name": "episode","update": "SYSUTCDATETIME()"}
```

```JSON
{"__id": "100-1_20101108-111352093","animalId": "100-1","name": "episode","update": "\/Date(1350451322147)\/"}
```


## Response

### Response Code

201

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|Location|Resource URL of created Entity|Return only when Entity can be created successfully|
|DataServiceVersion|OData version information|Return only when Entity can be created successfully|
|ETag|Resource version information|Return only when Entity can be created successfully|

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
|{3}|type|string|UserData.{EntityTypeName}|
|{2}|__id|string|EntityID(__id)|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

In addition to the above, return dynamic user data specified at the time of registration

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/collection1/entity-type1
('100-1_20101108-111352093')",
        "etag": "W/\"1-1487662179733\"",
        "type": "UserData.entity-type1"
      },
      "__id": "100-1_20101108-111352093",
      "__published": "/Date(1487662179733)/",
      "__updated": "/Date(1487662179733)/",
      "PetName": null,
      "animalId": "100-1",
      "name": "episode",
      "startedAt": "2010-11-08",
      "episodeType": "care",
      "endedAt": "",
      "outcome": "During treatment"
    }
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1" -X POST -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' -d '{"__id": "100-1_20101108-111352093",\
"animalId": "100-1","name": "episode","startedAt": "2010-11-08","episodeType": "care","endedAt": \
"","outcome": "During treatment"}'
```
