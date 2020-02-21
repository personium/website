---
id: version-1.7.18-285_Retrieve_Log_File
title: Retrieve Log File
sidebar_label: Retrieve Log File
original_id: 285_Retrieve_Log_File
---

## Overview

Retrieves an event log file. 

### Required Privileges

log-read

### Restrictions

Planned log output configuration is not yet supported.  Following fixed configuration is applied.

* log file name is "default.log".
* Log file is rotated when the size reaches a certain amount (50MB). 
* When rotated the file will be renamed to "default.log. {Timestamp}". {Timestamp} represents the time when the file is rotated.
* Only a certain number of archived logs are kept.  (12 generations)
* When the number of archived files exceeds the maximum, the oldest log file is automatically deleted.

|Action|Archived log file|Description|Notes|
|:--|:--|:--|:--|
|First Rotation|archive/<br>default.log.1402910774659|<br>Newly rotated file|<br>2014-06-16 18:26:14 +0900|
|2nd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659|<br>the preceding roteted file<br>Newly rotated file|<br>2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900|
|3rd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659<br>default.log.1403910784659|<br>the file before preceding file<br>the preceding roteted file<br>Newly rotated file|<br>2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900<br>2014-07-09 21:59:44 +0900|


## Request

### Request URL

#### Recent log file

```
{CellURL}__log/current/{LogName}
```

#### Log file that is rotated

```
{CellURL}__log/archive/{LogName}
```

\*{LogName} specifies the file name returned by the log file information acquisition API.

### Request Method

GET

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

None


## Response

### Response Code

200

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|MimeType depending on Resource|"text/csv" or "application/zip"|

### Response Body

If there is no log at current log acquisition time, return an empty response body.  
There is a possibility that the rotate size is about 5MB larger than it configured  
Output form is following

```
{dateTime},[{level}],{RequestKey},{external},{schema},{subject},{type},{object},{info}
```

|Item Name|Overview|Notes|
|:--|:--|:--|
|dateTime|Log write date and time (ISO8601 UTC format)|YYYY-MM-DDTHH:MM:SS.sssZ|
|level|log level INFO,WARN,ERROR|String|
|RequestKey|Value specified on X-Personium-RequestKey header<br>when the X-Personium-RequestKey header is not specified, PCS-${32 character string with UUID}|String|
|external|External events:true<br>Internal events:false|String|
|schema|Schema of box of accepted URL|URL format|
|subject|Principal events|URL format|
|type|External events: Type defined in the event reception<br>Internal events: Type defined for each event|String|
|object|External events: Object defined in the event reception<br>Internal events:Requested resource path|String|
|info|External events: Info defined in the event reception<br>Internal events:HTTP status code|String|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

External Events

```
2013-02-04T00:50:12.761Z,[INFO ],"Req_animal-access_1001","true","https://cell1.unit1.example/",
"https://unitadmin.unit1.example/#admin","authSchema","https://cell1.unit1.example/box1/service_name/token_keeper",
"[XXXX2033] Success schema authorization. cellUrl=https://keeper-d4a57bb26eae481486b07d06487051d1.unit1.example/"
```

Internal Event

```
2013-04-18T14:52:39.778Z,[INFO ],"PCS-1364350331902","false","https://app-cell1.unit1.example/",
"https://app-cell1.unit1.example/#staff","cellctl.Role.list","https://homeClinic.unit1.example/__ctl/Role","200"
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__log/current/default.log" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

