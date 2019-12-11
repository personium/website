---
id: 385_Box_Export
title: Export Box
sidebar_label: Export Box
---

## Overview
Export the bar file in the specified box. For the bar file format, see "[ bar file ](301_Bar_File.md)".  

### Required Privileges
read  
read-acl  

### Restrictions
#### Unsupported export item
- 30_extroles.json, 70_$ links.json
- 10_odatarelations.json
- Under 90_data
- MainBox

## Request

### Request URL
```
{CellURL}{BoxName}
```

### Request Method
GET  

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value} override} $: $ {value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/zip+x-personium-bar|Yes||

### Request Body
None  

## Response

### Response Code
|Code|Message|Overview|Notes|
|:--|:--|:--|:--|
|200|OK|Successful export||

### Response Header
|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Content-Type of file|application/zip+x-personium-bar|
|Content-Length|Content-Length of file||

### Response Body
Return the contents of the file in binary  

### Error Messages
Refer to [Error Message List](004_Error_Messages.md)  

### Response Sample
None  

For details of URL for [Box metadata acquisition API](303_Progress_of_Bar_File_Installation.md), see Box metadata acquisition.

## cURL Command
```sh
curl "https://cell1.unit1.example/box1" -X GET -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/zip+x-personium-bar' -o "/home/user/export.bar"
```
