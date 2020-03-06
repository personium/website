---
id: version-1.7.21-370_Delete_Entity
title: Delete Entity
sidebar_label: Delete Entity
original_id: 370_Delete_Entity
---

## Overview

Delete single item the Entity of user data

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
    * When setting in request body and setting with DefaultValue (\_\_published, \_\_ updated is the latter timing)
    * For EntityType, you can create up to 400 DynamicProperty / DeclaredProperty / ComplexTypeProperty


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}({EntityID})}
```

|Path|Overview|
|:--|:--|
|{CellName}|Cell Name|
|{BoxName}|Box Name|
|{ODataCollecitonName}|Collection Name|
|{EntityTypeName}|EntityType name|
|{EntityID}|ID of Entity to delete|

### Request Method

DELETE

### Request Query

#### Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

#### OData Common Request Query

None

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

#### OData Delete Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

None


## Response

### Response Code

204

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|Return only if you failed to delete Entity|
|DataServiceVersion|OData version information|Return only when the Entity can be successfully deleted|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('100-1_20101108-111352093')" \
-X DELETE -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

