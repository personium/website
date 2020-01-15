---
id: 508_Progress_of_Import_Cell
title: Retrieve cell import status
sidebar_label: Retrieve cell import status
---

## Overview

Get Cell Import status. The Cell import state includes the following information.

* Cell import status
    * Cell import acceptance available
    * Cell import processing in progress
    * Cell Import Abnormal termination
* Import start date and time
* Progress rate
* Import file name
* Error message

### Required Privileges

root


## Request

### Request URL

```
{CellURL}__import
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
|X-Override|Header override function|${OverwrittenHeaderName}:${Value} override} $: $ {value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

None


## Response

### Response Code

|Code|Message|Overview|Notes|
|:--|:--|:--|:--|
|200|OK|On success|Cell import status refers to response body|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|
|Content-Type|Format of data to be returned||

### Response Body

Response is JSON format and is defined as an object (subobject).  
The correspondence between key (name) and type, and value are as follows.

|Object|Key|Type|Value|Notes|
|:--|:--|:--|:--|:--|
|Root|status|string|One of the following strings: <br>"ready"<br>"importation in progress"<br>"import failed"|"ready":Cell import acceptance available<br>"importation in progress":Cell import processing in progress<br>"import failed":Cell Import Abnormal termination|
|Root|started_at|string|Start time (ISO 8610 UTC format)|Do not output when status is below.<br>"ready"|
|Root|progress|string|Progress rate (for example, "30%")|Do not output when status is below.<br>"ready"|
|Root|importation_name|string|Import file name (excluding extension)|Do not output when status is below.<br>"ready"|
|Root|message|object|Object (message format)|Output only when status is below.<br>"import failed"<br>See [ Error Messages ](004_Error_Messages.md) for details|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

Cell Import accepted (Including when importing Cell)

```json
{
  "status": "ready"
}
```

When Cell import processing is in progress

```json
{
  "status": "importation in progress",
  "started_at": "2017-02-13T09:00:00.000Z",
  "progress": "81%",
  "importation_name": "CellExport_2017_01"
}
```

Cell Import Abnormal termination

```json
{
  "status": "import failed",
  "started_at": "2017-02-13T09:00:00.000Z",
  "progress": "81%",
  "importation_name": "CellExport_2017_01",
  "message": {
      "code" : "PR409-OD-0003",
      "message" : {
          "lang" : "en",
          "value" : "The entity already exists."
      }
  }
}
```


## cURL Sample

```sh
curl "https://cell1.unit1.example/__import" -X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json'
```


