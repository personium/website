---
id: version-1.7.18-507_Import_Cell
title: Import Cell
sidebar_label: Import Cell
original_id: 507_Import_Cell
---

## Overview

Import cell data from Cell snapshot file.<br>The Cell snapshot file uses a special area (Cell snapshot area) in PersoniumUnit.<br>If processing fails, change the status of Cell to " import failed ".<br>When processing is successful, if the status of Cell is " import failed ", it is changed to " normal ".<br>When the status of Cell is " import failed ", the target Cell does not accept anything other than API. See [ Retrieve Properties ](290_Cell_Get_Property.md) for details.<br>Since this API employs the asynchronous communication method, it immediately returns after accepting the API.<br>To check the status of Cell Import, use [ Cell import status acquisition ](508_Progress_of_Import_Cell.md).<br>An example of calling from acceptance at the client to completion of processing is shown below.

```
Call Import example of Cell Import (When polling on client is set to 10 seconds)
 1. Cell import reception
    -- POST https://cell1.unit1.example/__import
 2. Cell import status check
    -- GET https://cell1.unit1.example/__import -> "Processing"being returned.
    -- Polling for 10 seconds
 3. Cell Import Complete
    -- GET https://cell1.unit1.example/__import -> "Acceptable"being returned.
    * The process in the above 2 loops and polls until completion of processing.
```

### Required Privileges

root

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the json format
* Even if processing fails in the middle, rollback is not performed  
\* It is recommended that you export the Cell once before importing the Cell.

## Request

### Request URL

```
{CellURL}__import
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
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application / json|No|[application/json] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|Snapshot file name (excluding extension)|Number of digits: 1-192<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")|Yes||

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
|Location|URL for obtaining cell import status||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

Return error message only if creation fails

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Sample
```sh
curl "https://cell1.unit1.example/__import" -X POST -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -d '{"Name":"CellExport_2017_01"}'
```
