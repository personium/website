---
id: version-1.7.21-310_Delete_Collection
title: Delete collection
sidebar_label: Delete collection
original_id: 310_Delete_Collection
---

## Overview

Delete collection

### Required Privileges

write

## Request

### Request URL

```
{CellURL}{BoxName}/{CollectionName}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{CollectionName}|Collection Name|Valid values Number of digits:1-256|

### Request Method

DELETE

### Request Query

Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### WebDav Common Request Query

None

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|
|X-Personium-Recursive|Specify recursive deletion|String|No|If true, recursive deletion of the collection is performed.<br>If it is false or if there is no header specification, normal deletion is carried out.|

### Request Body

None


## Response

### Response Code

204

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|application/json|Return only when deletion fails|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command


```sh
curl "https://cell1.unit1.example/box1/collection1" -X DELETE -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


