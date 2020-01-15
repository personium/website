---
id: 503_Register_and_Update_Snapshot_Cell
title: Create/Update Cell snapshot file 
sidebar_label: Create/Update Cell snapshot file 
---

## Overview

Register / update Cell snapshot.

### Required Privileges

root


## Request

### Request URL

```
{CellURL}__snapshot/{FileName}
```

### Request Method

PUT

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|
|Content-Type|Specify the content format of the registration / update file|String|No|When registering and updating in ZIP format<br>Content-Type:application/zip|

### Request Body

|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|
|Designate the context information to be registered / updated as binary in the request body|The method specified in the Content-Type header|Yes||


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|201|Created|Registration success|
|204|No Content|Update success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|Only when it fails at update / creation, return it|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|
|ETag|Resource version information||

### Response Body

Only when it fails at update / creation, return it

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Sample

```sh
curl "https://cell1.unit1.example/__snapshot/CellExport_2017_01.zip" -X PUT -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' -d '{File contents}'
```

```sh
curl "https://cell1.unit1.example/__snapshot/CellExport_2017_01.zip" -X PUT -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' -T "/home/user/CellExport.zip"
```


