---
id: version-1.7.18-311_Get_WebDav
title: Retrieve file
sidebar_label: Retrieve file
original_id: 311_Get_WebDav
---

## Overview

Retrieve specific WebDav information  
Depending on the ETag value specified in the If-None-Match header, the contents to be returned are different  
When specifying the range with the Range header, return the contents of the specified range

### Required Privileges

read

## Request

### Request URL

```
{CellURL}{BoxName}/{ResourcePath}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{ResourcePath}|Path to resource|Valid values Number of digits:1-256|

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
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

#### Individual Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|If-None-Match|Specify the value of ETag|String<br>Specify the ETag value in the following format<br>"*"<br>or <br>"{Half-width number}-{Half-width number}"|No|Example) When specifying the ETag value "1-1372742704414"<br> "1-1372742704414"|
|Range|Specify a range when acquiring a part of a resource|-Data type:String<br>[Assumption]<br>Start value of range specification starts at 0.When the size of the acquired file is Z (byte), the termination is Z-1 (byte)<br>1."Range: bytes={Half-width number}-{Half-width number}"<br>ex) "Range: bytes=10-20"<br>2."Range: bytes={Half-width number}-"<br> -> From the range start value to the end of the acquired file<br>ex) "Range: bytes=10-"<br>3."Range: bytes=-{Half-width number}"<br> -> Retrieve the specified minute from the end of the resource<br>ex) "Range: bytes=-20"|No|-Specify a start value smaller than the size of the acquired file<br>-When the format of the specified Range header is incorrect, the Range header is ignored<br>[Limitations]<br>-Not supported for multi-part response|

### Request Body

None


## Response

### Response Code

* If the If-None-Match header is not specified in the request, or if the ETag value of the If-None-Match header does not match the ETag of the resource stored in the WebDav in the request  
    (Including cases where the format of the specified ETag value is invalid)
* If the Range header is not specified in the request, or if the start value specified in the Range header in the request is larger than the termination value

|Code|Message|Overview|
|:--|:--|:--|
|200|OK|Successful acquisition|

* When valid in the Range header of the request

|Code|Message|Overview|
|:--|:--|:--|
|206|Partial Content|Partial acquisition success|

* If the ETag value of the If-None-Match header in the request matches the ETag of the resource stored in WebDav

|Code|Message|Overview|
|:--|:--|:--|
|304|Not Modified|The document has not been updated|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Content-Type of resource|The value specified when the resource is created or updated with PUT method will return.|
|ETag|Resource version information||
|Accept-Ranges|Indicates acceptance of byte range (range) request to resource||
|Content-Range|Indicates where the entity body corresponds to the part specified by the byte range request||

In case of basic authentication error, return 400 + WWW-Authenticated: Basic header

### Response Body

Return the contents of the file  
However, if the status code is 304, the response body is not returned  
If the status code is 206, the contents of the file specified in the Range header are returned

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/{ResourcePath}" -X GET -i \
-H 'If-None-Match:"1-1372742704414"' -H 'Range:bytes=10-20' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


