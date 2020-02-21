---
id: version-1.7.18-286_Delete_Log_File
title: Delete Log File
sidebar_label: Delete Log File
original_id: 286_Delete_Log_File
---

## Overview

Deletes an arhcived log files. The most recent log file cannot be deleted. 
Log file is rotated when the size reaches a certain amount (50MB). 
Only a certain number of archived logs are kept.  (12 generations)
When the number of archived files exceeds the maximum, the oldest log file is automatically deleted.

### Required Privileges

log

## Request

### Request URL

#### rotated log file

```
{CellURL}__log/archive/{LogName}
```

\*{LogName} specifies the file name returned by the log file information acquisition API.

### Request Method

DELETE

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

None


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|204|No Content|Delete success|

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|application/json|To be returned only if it fails to remove|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/__log/archive/default.log" -X DELETE -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

