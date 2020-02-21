---
id: version-1.7.18-295_Box_Recursive_Delete
title: Delete Recursive Box
sidebar_label: Delete Recursive Box
original_id: 295_Box_Recursive_Delete
---

## Overview

* This API deletes all the relevant data specified Box, data under Box and data linked to Box.
* This API deletes the following data:
    * Role
    * Relation
    * ExtRole
    * ReceivedMessage
    * SentMessage
    * Collection
    * AssociationEnd
    * EntityType
    * ComplexType
    * Property
    * ComplexTypeProperty
    * $links
    * User data

### Required Privileges

Box


## Request

### Request URL

```
{CellURL}{BoxName}
```

### Request Method

DELETE

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|Yes|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|X-Personium-Recursive|Specifies a bulk delete|String|Yes|True:This API implements the bulk delete<br>When there is no specified header or False: returns the error response code 412|

### Request Body

None


## Response

### Response Code

204

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1" -X DELETE -i -H 'X-Personium-Recursive: true' -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

