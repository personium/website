---
id: 312_Register_and_Update_WebDAV
title:  Create/Update file
sidebar_label:  Create/Update file
---

## Overview

Register / update WebDav information.

### Required Privileges

write

## Request

### Request URL

```
{CellURL}{BoxName}/{ResourcePath}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{ResourcePath}|Path to resource|Valid values Number of digits:1-256<br>Specify a percent-encoded character string(character code:UTF-8)|

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
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

#### Individual Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|
|Content-Type|Specify the MIME Type (IANA Media Type) of the file content|String|No|The value specified here will be returned upon GET request as a response Content-Type header value. <br>See [IANA Media Types list](https://www.iana.org/assignments/media-types/media-types.xhtml) for what value to specify.|

### Request Body

|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|
|Binary byte sequence of the file content to register or update|Body content should comply with the specified format in the Content-Type header|Yes||


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|201|Created|Successful registration|
|204|No Content|Update success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|Only when it failed at the time of update / creation, return it|
|ETag|Resource version information||

### Response Body

Only when it failed at the time of update / creation, return it

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/{ResourcePath}" -X PUT -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H  'Accept: application/json' -d '{[File contents]}'
```

