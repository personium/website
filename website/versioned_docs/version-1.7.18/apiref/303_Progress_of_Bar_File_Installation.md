---
id: version-1.7.18-303_Progress_of_Bar_File_Installation
title: Retrieve Box Meta Data
sidebar_label: Retrieve Box Meta Data
original_id: 303_Progress_of_Bar_File_Installation
---

## Overview

Get the metadata of Box. The metadata includes the following information.

* Box status  
    Box installation status (installation result, progress rate, error message, etc.)
* There are the following three types of states of Box
    * Box available
    * Box installation process in progress
    * Box installation process terminated abnormally
* Box name
* Box URL
* Box Schema URL
* Box creation date and time
* [Cell Metadata](296_Get_Cell_Metadata.md)
* [Unit Metadata](107_Get_Unit_Metadata.md)

### Required Privileges

read

### Restrictions

* The expiration date that Box installation status can be confirmed is until the deadline set in Unit after completion of Box installation (including abnormal termination)
* If Box installation fails, you need to refer to the log output to EventBus


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

### Request Body

None


## Response

### Response Code

|Code|Message|Overview|Notes|
|:--|:--|:--|:--|
|200|OK|On success|Refer to response body for success / failure of Box installation|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

Response is JSON format, defined in object (subobject).  
The correspondence between key (name) and type, and value are as follows.

|Object|Name(Key)|Type|Value|Notes|
|:--|:--|:--|:--|:--|
|Root|box|object|Object (box format)||
|box|status|string|One of the following strings: <br>- "ready"<br>- "installation in progress"<br>- "installation failed"|Box shows usable state<br>Box indicating that the installation process is in progress<br>Box indicates completion of installation (abnormal termination)|
|box|started_at|string|Start time (ISO 8610 UTC format)|Do not output when status is below.<br>- "Ready"|
|box|progress|string|Progress rate (for example, "30%")|Do not output when status is below.<br>- "Ready"|
|box|message|object|Object (message format)|Output only when status is below.<br>- "Installation failed"<br>For details, see the [error message list](004_Error_Messages.md)|
|box|name|string|The name of the Box||
|box|url|string|The URL of the Box||
|box|schema|string|The URL of the schema to which the Box is attached|Null for no schema|
|box|installed_at|string|Start time (ISO 8610 UTC format)|Do not output when status is one of the following.<br>- "Installation in Progress"<br>- "installation failed"|
|Root|cell|object|Object (cell format)||
|cell|name|string|The name of the Cell||
|cell|url|string|The URL of the Cell||
|Root|unit|object|Object (unit format)||
|unit|url|string|The URL of the Unit||
|unit|path_based_cellurl_enabled|boolean|true:path based cell url<br>false:per cell fqdn url||

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

After creating Box (including when Box installation is completed)

```JSON
{
  "box": {
    "status": "ready",
    "installed_at": "2017-02-13T09:00:00.000Z",
    "name": "app-box1",
    "url": "https://cell1.example.com/app-box1/",
    "schema": "https://app-cell1.example.com/"
  },
  "cell": {
    "name": "cell1",
    "url": "https://cell1.unit1.example/"
  },
  "unit": {
    "url": "https://unit1.example/",
    "path_based_cellurl_enabled": true
  }
}
```

During Box installation process

```JSON
{
  "box": {
    "status": "installation in progress",
    "started_at": "2017-02-13T09:00:00.000Z",
    "progress": "81%",
    "name": "app-box1",
    "url": "https://cell1.unit1.example/app-box1/",
    "schema": "https://app-cell1.unit1.example/"
  },
  "cell": {
    "name": "cell1",
    "url": "https://cell1.unit1.example/"
  },
  "unit": {
    "url": "https://unit1.example/",
    "path_based_cellurl_enabled": true
  }
}
```

When Box installation is completed (abnormal termination)  
(After expiration of Box installation, within the expiration date)
```JSON
{
  "box": {
    "status": "installation failed",
    "started_at": "2017-02-13T09:00:00.000Z",
    "progress": "81%",
    "message": {
      "code" : "PR409-OD-0003",
      "message" : {
        "lang" : "en",
        "value" : "The entity already exists."
      }
    },
    "name": "app-box1",
    "url": "https://cell1.unit1.example/app-box1/",
    "schema": "https://app-cell1.unit1.example/"
  },
  "cell": {
    "name": "cell1",
    "url": "https://cell1.unit1.example/"
  },
  "unit": {
    "url": "https://unit1.example/",
    "path_based_cellurl_enabled": true
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

