# Retrieve Cell snapshot file

## Overview

Obtain a Cell snapshot file.<br>The content to be returned varies depending on the ETag value specified in the If-None-Match header.

### Required Privileges

root


## Request

### Request URL

```
{CellURL}__snapshot/{FileName}
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
|X-HTTP-Method-Override|Method override function|User-defined|No|When this value is specified at the time of request in the POST method, the specified value is used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|If-None-Match|Specify the value of ETag|String<br>Specify the ETag value in the following format<br>"*"or "{Half size} - {Half size}"|No|Example) When specifying ETag value "1-1372742704414"<br>"1-1372742704414"|

### Request Body

None


## Response

### Response Code

* If the If-None-Match header is not specified in the request, or if the ETag value of the If-None-Match header does not match the ETag of the resource stored in WebDav in the request<br>(Including cases where the format of the specified ETag value is invalid)

|Code|Message|Overview|
|:--|:--|:--|
|200|OK|Acquisition success|

* If the ETag value of the If-None-Match header in the request matches the ETag of the resource stored in WebDav

|Code|Message|Overview|
|:--|:--|:--|
|304|Not Modified|The document has not been updated|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Resource Content-Type|Return only for status code 200|
|ETag|Resource version information||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

Return the contents of the file  
However, when the status code is 304, the response body is not returned

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Sample

```sh
curl "https://cell1.unit1.example/__snapshot/snapshot-file1" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA'
```

