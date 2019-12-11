---
id: 278_Event_Reception
title: Accept External Event
sidebar_label: Accept External Event
---

## Overview

Accept any external event to be handled by the event processing function of Cell.

### Required Privileges

event

## Request

### Request URL

```
{CellURL}__event
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
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

### Request Body

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Type|Type of event|String<br>Number of digits: 0&#45;51200 byte|No||
|Object|Object of the eventbr|String<br>Number of digits: 0&#45;51200 byte|No||
|Info|Information of the event|String<br>Number of digits: 0&#45;51200 byte|No||

### Request Sample

```JSON
{
  "Type":"authSchema",
  "Object":"https://cell1.unit1.example/box1/service_name/token_keeper",
  "Info":"[XXXX2033] Success schema authorization. cellUrl=https://keeper-d4a57bb26eae481486b07d06487051d1.unit1.example/"
}
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|200|OK|Accepted success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command
```sh
curl "https://cell1.unit1.example/__event" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' \
-d '{"Type":"authSchema", "Object":"https://cell1.unit1.example/box1/service_name/token_keeper", \
"Info":"[XXXX2033] Success schema authorization. \
cellUrl=https://keeper-d4a57bb26eae481486b07d06487051d1.unit1.example/"}'
```


