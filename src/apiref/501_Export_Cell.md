---
id: 501_Export_Cell
title: Export Cell
sidebar_label: Export Cell
---

## Overview

This API export all data in Cell as Cell snapshot file.  
The snapshot file is created in a special area (Cell snapshot area) in PersoniumUnit.  
When exported successfully, created the file which suffix is ".zip" and when fail created the file which suffix is ".error".(In the ".error" file, detail error message is described)  
The Cell snapshot area is excluded from the Cell export.  
Since this API employs the asynchronous communication method, it immediately returns after accepting the API.  
To confirm the Cell export executing status, use [Get Cell Export status](502_Progress_of_Export_Cell.md),[Get Cell Snapshot property](505_Get_Property_Snapshot_Cell.md).  
An example of calling from acceptance at the client to completion of processing is shown below.

```
Call export call example (with 10 seconds polling on the client)
 1. Cell export reception
    -- POST https://cell1.unit1.example/__export
 2. Cell export status check
    -- GET https://cell1.unit1.example/__export -> return "in progress"
    -- wait 10 seconds
 3. Cell export finished
    -- GET https://cell1.unit1.example/__export -> return "acceptable"
 4. confirm Cell export finished successfully
    -- PROPFIND /{cell}/__snapshot -> when the file suffix is ".zip" exported successfully, ".error" error occured.
 * The process in the above 2 loops and polls until completion of processing.
 * When you wish to acquire details at abnormal termination, refer to the contents of & quot; .error & quot; file.
```

### Required Privileges

root

### Restrictions

* Always handles Content-Type in the request header as application/json
* Accept only JSON format for request body


## Error file

### Overview

If the Cell export fails, a file with the extension ". Error" is generated in the Cell snapshot area. (The file name is the name specified by the body)<br>The error content is described in JSON format in the quot; .error & quot; file.<br>The format of the & quot;. error & quot; file is shown below.

|Object|Key|Type|Value|Notes|
|:--|:--|:--|:--|:--|
|Root|code|string|||
|Root|message|object|||
|message|lang|string|||
|message|value|string|||

### Sample

```
{
  "code":"PR503-SV-0001",
  "message":
  {
    "lang":"en",
    "value":"Too many concurrent requests."
  }
}
```


## Request

### Request URL

```
{CellURL}__export
```

### Request Method

POST

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
|Content-Type|Specifies the request body format|application / json|No|[application/json] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|Snapshot file name (excluding extension)|Number of digits: 1-192<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")|No|Default [{CellName}_yyyyMMdd_HHmmss]|

### Request Sample

```json
{"Name":"CellExport_2017_01"}
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|202|Accepted|Processing reception|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|Return only if creation fails|
|Location|URL for retrieving Cell export status||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

Return error message only if creation fails

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Sample

```sh
curl "https://cell1.unit1.example/__export" -X POST -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' -d '{"Name":"CellExport_2017_01"}'
```

