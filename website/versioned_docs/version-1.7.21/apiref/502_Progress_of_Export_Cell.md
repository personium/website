---
id: version-1.7.21-502_Progress_of_Export_Cell
title: Retrieve cell export status
sidebar_label: Retrieve cell export status
original_id: 502_Progress_of_Export_Cell
---

## Overview

Get the status of Cell export. The Cell export state includes the following information.

* Cell export status
    * Cell export acceptance accepted
    * Cell export in progress
* Export start date and time
* Progress rate
* Export file name

### Required Privileges

root


## Request

### Request URL

```
{CellURL}__export
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
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

None


## Response

### Response Code

|Code|Message|Overview|Notes|
|:--|:--|:--|:--|
|200|OK|On success|Cell Export status refers to response body|

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
|Root|status|string|One of the following strings: <br>"ready"<br>"exportation in progress"|"ready":Cell export acceptance accepted<br>"exportation in progress":Cell export in progress|
|Root|started_at|string|Start time (ISO 8610 UTC format)|Do not output when status is below.<br>"ready"|
|Root|progress|string|Progress rate (for example, "30%")|Do not output when status is below.<br>"ready"|
|Root|exportation_name|string|Export file name (excluding extension)|Do not output when status is below.<br>"ready"|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

Cell export acceptance accepted (including when cell export is completed)

```json
{
  "status": "ready"
}
```

Cell export processing in progress

```json
{
  "status": "exportation in progress",
  "started_at": "2017-02-13T09:00:00.000Z",
  "progress": "81%",
  "exportation_name": "CellExport_2017_01"
}
```


## cURL Sample

```sh
curl "https://cell1.unit1.example/__export" -X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA'
```


