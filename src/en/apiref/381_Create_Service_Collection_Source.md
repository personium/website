---
id: 381_Create_Service_Collection_Source
title: Create service collection source
sidebar_label: Create service collection source
---

## Overview

Register / update service source information

### Required Privileges

write

## Request

### Request URL

```
{CellURL}{BoxName}/{CollectionName}/__src/{ResourceName}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{CollectionName}|Service Collection Name|Valid values <br>Number of digits:1-256|
|{ResourceName}|Resource name|Valid values(limit) <br>Number of digits:1-256|

### Request Method

PUT

### Request Query

#### Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

#### Individual request header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|If-Match|Specifies the target ETag value|String|No|[*] by default|
|Content-Type|Specify the content format of the registration / update file|String|Yes|When registering / updating resources in JS in the form<br>Content-Type:text/javascript|

### Request Body

|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|
|Designate context information to be registered / updated as a request body in binary|Format specified by Content-Type header|Yes||


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|201|Created|Successful registration|
|204|No Content|Update success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|Return only when update / creation fails|
|ETag|Resource version information||

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/collection1/__src/{ResourceName}" -X PUT -i  -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' -H \
'Content-Type:text/javascript' -d '[File contents]'
```

