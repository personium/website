---
id: version-1.7.21-309_Update_Move_Collection
title: Move and Rename collection
sidebar_label: Move and Rename collection
original_id: 309_Update_Move_Collection
---

## Overview

Move / rename WebDAV collection file.  
\* You can not change properties

### Required Privileges

write

## Request

### Request URL

```
{CellURL}{BoxName}/{ResourcePath}/
```

### Request Method

MOVE

### Request Query

#### Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

#### WebDav Common Request Query

None

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
|Destination|Change destination|Absolute URI|Yes|Move / Specify the file name to change the name.|
|Overwrite|Overwrite|"T" or "F"|No|Specify Overwrite available("T") and Can not overwrite("F").(The initial value is "F")|
|Depth|Mobile hierarchy|"infinity"|No|Specify the depth of the moving collection hierarchy. (Initial value is infinite)|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

None


## Response

### Response Code

|Code|Overview|Notes|
|:--|:--|:--|
|201|Created|Move or rename name success (create)|
|204|No Content|Move or rename name success (Overwrite)|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Location|Resource URL of the created collection|Return only when collection can be created successfully|
|ETag|Resource version information|Return only when collection can be created successfully|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

None

## cURL Command

Change the collection name ("/" at the end is mandatory)

```sh
curl "https://cell1.unit1.example/box1/collection1/" -X MOVE -i \
-H 'Destination:https://cell1.unit1.example/box1/collection2/' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA'
```

File name change

```sh
curl "https://cell1.unit1.example/box1/collection1/file1/" -X MOVE -i \
-H 'Destination:https://cell1.unit1.example/box1/collection1/file2/' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA'
```

File move

```sh
curl  "https://cell1.unit1.example/box1/collection1/file1/" -X MOVE -i \
-H 'Destination:https://cell1.unit1.example/box1/collection2/file1/' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA'
```


