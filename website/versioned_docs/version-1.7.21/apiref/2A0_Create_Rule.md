---
id: version-1.7.21-2A0_Create_Rule
title: Create Rule
sidebar_label: Create Rule
original_id: 2A0_Create_Rule
---
## Overview
Create a new event processing rule.

### Required Permissions
rule

### Limitations
* Accept of request header is ignored
* Treat all Content-Type of the request header as application / json
* Accept only JSON format for request body
* Content-Type of the response header supports only application / json, and the response body is JSON format

## request
### Request URL
```
{CellURL}__ctl/Rule
```
### Method
POST

### Request query

| Query name | Summary | Valid values | Required | Remarks |
|:--|:--|:--|:--|:--|
| p_cookie_peer | cookie authentication value | cookie authentication value returned from the server at the time of authentication | No | valid only when there is no specification of the authorization header | specify when using cookie authentication information |

### Request Header

| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| X-HTTP-Method-Override | method override function | optional | No | If you specify this value when requesting with the POST method, the specified value will be used as a method. |
| X-Override | header override function | $ {overwrite header name}: $ {value} | No | overwrites the value of normal HTTP header. To overwrite multiple headers, specify multiple X-Override headers. |
| X-Personium-RequestKey |RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
| Authorization | Specify authentication information in OAuth 2.0 format | Bearer {AccessToken} | No | * Authentication token acquired with the authentication token acquisition API Token |
| Content-Type | Specify the format of the request body | application / json | No | treat it as [application/json] when omitted |
| Accept | Specify the response body format | application / json | No | treat as [application/json] when omitted |
### Request body
#### Format

JSON

| Item name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| \_Box.Name | Box name to which the rule should be attached | valid box name. A request not specifying this key or specifying a null value is interpreted as a Rule that is not associated with any Box.| No ||
| Name | Arbitrary name to identify the rule to be created | When linking to a Box, it is unique within the Box, and if it is not tied to the Box, it must be unique in the cell. When | No | is omitted, the uuid automatically allocates | No ||
| EventType | Character string for forward match checking for the type of event that triggers a rule | For Evnet Type, the type is defined for internal events as a separate [table](277_Event_Summary.md). For external events, you can specify any Type. 'timer.oneshot' and 'timer.periodic' are the type of event that is triggered by time.| No ||
| EventSubject | Character string for perfect match checking for the subject of event that triggers a rule | Event Subject is the URL to express Account, so valid value is the exact match string. Scheme to be set is http, https or personium-localunit. | No | If value of EventSubject is able to be converted to personium-localunit scheme, respond error. Please set using personium-localunit scheme. |
| EventObject | Event Object's event object to trigger the rule String for forward match check | Event The value of object depends on the type of event. An arbitrary character string can be set, but the meaningful value depends on the event type. When EventType is 'timer.oneshot', set string of epoch time(milliseconds) that this rule will be triggered. When EventType is 'timer.periodic', set string of period(minutes) that this rule will be triggered. | No ||
| EventInfo | Character string for forward matching with info of event that triggers a rule | Event info value depends on event type. An arbitrary character string can be set, but the meaningful value depends on the event type. | No ||
| EventExternal | Flag indicating whether the event to trigger the rule is an external event | Boolean. Set to true to detect external events. | No | default value false |
| Action | Action to be started when the event matches | Valid values are the following table | Yes |||
| TargetUrl | The value to be specified depends on the value of the concrete target URL | Action for the action. The rules are as follows attached table | No ||

#### Allowed Values for Timer Event
| EventType | EventObject | EventExternal | Remarks |
|:--|:--|:--|:--|
| timer.oneshot | Epoch time on milliseconds(Required) | false | truncated to minutes internally |
| timer.periodic | minutes(Required) | false | |

Timer event will be created below based on the rule.

| Item name | Value |
|:--|:--|
| Subject | EventSubject |
| Schema | Schema of Box of \_Box.Name |
| RequestKey | null |
| External | false |
| Type | EventType |
| Object | EventObject |
| Info | EventInfo |

Therefore, this event matches with the rule.

EventSubject can be set to other cell's subject. However, after the rule was triggerred, Subject of the event is set to null. 

#### Valid Actions
| Action | Description | TargetUrl | Remarks |
|:--|:--|:--|:--|
| exec | engine script is started and event data is passed by the POST method. | Engine service url | - |
| relay | Relays events to TargetUrl. | Relay destination to relay event information Url | - |
| relay.event | Relays events to accept event api of TargetUrl. | Cell URL to relay event information | - |
| log | Log the events at info level. | - | - |
| log.info | Log the events at info level. | - | - |
| log.warn | Log the events at warn level. | - | - |
| log.error | Log the events at error level. | - | - |

#### EventObject Allowed Values

Only specific URL can be accepted for EventObject field when EventExternal is false.

| EventExternal | \_Box.Name | EventType | EventObject | Remarks |
|:--|:--|:--|:--|:--|
| false | specified | | personium-localbox:/...<br>personium-localcell:/\_\_... ||
| false | Not specified | | personium-localcell:/... ||
| false | | timer.oneshot<br>timer.periodic | Numeric string ||
| true ||| Any string ||

#### TargetUrl Allowed Values

Only specific kinds of URL can be accepted for TargetUrl field.

| Action | \_Box.Name | TargetUrl | Remarks |
|:--|:--|:--|:--|
| exec | specified | personium-localbox:/{CollectionName}/{ServiceName} ||
| exec | Not specified | personium-localcell:/{BoxName}/{CollectionName}/{ServiceName} ||
| relay | specified | URL with scheme http, https, personium-localunit, personium-localcell, personium-localbox.| If value of TargetUrl is able to be converted to personium-localunit scheme, respond error. Please set using personium-localunit scheme. |
| relay | Not specified | URL with scheme http, https, personium-localunit, personium-localcell. | If value of TargetUrl is able to be converted to personium-localunit scheme, respond error. Please set using personium-localunit scheme. |
| relay.event || Cell URL.<br>http&#58;//...<br>https&#58;//...<br>personium-localunit:{CellURL}<br>personium-localcell:/ | If value of TargetUrl is able to be converted to personium-localunit scheme, respond error. Please set using personium-localunit scheme. |

### Request sample
```JSON
{"Name":"rule1", "EventExternal":true, "Action":"log"}
```

## Response
### Status code on success
201

### Response header
| Header name | Overview | Remarks |
|:--|:--|:--|
| X-Personium-Version | Execution version of API | API version processed request |
| Access-Control-Allow-Origin | Cross-domain communication permission header | Return value is fixed as "\*" |
| Content-Type | Format of data to be returned ||
| Location | URL to created resource ||
| ETag | resource version information ||
| DataServiceVersion | OData version ||

### Response body
The response is a JSON object, and the correspondence between the key (name) and type defined in the object (subobject) and the value are as follows.

| Object | Item name | Data Type | Remarks |
|:--|:--|:--|:--|
| Route | d | object | object {1} |
| {1} | results | array | Array of objects {2}
| {2} | \_\_metadata | object | object {3} |
| {3} | uri | string | URL to created resource |
| {3} | etag | string | Etag value |
| {2} | \_\_published | string | creation date (UNIX time) |
| {2} | \_\_updated | string | Update date (UNIX time) |
| {1} | \_\_count | string | $ inlinecount number of results obtained by query |

### Rule specific response body

| Object | Item name | Data Type | Remarks |
|:--|:--|:--|:--|
| {3} | type | string | CellCtl.Rule |
| {2} | Name | string | Rule name |
| {2} | \_Box.Name | string | Box name of relation |
| {2} | EventExternal | boolean ||
| {2} | EventSubject | string ||
| {2} | EventType | string ||
| {2} | EventObject | string ||
| {2} | EventInfo | string ||
| {2} | Action | string ||
| {2} | TargetUrl | string ||

### Response body sample
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/Rule(Name='rule1',_Box.Name='box1')",
        "etag": "W/\"1-1486368212581\"",
        "type": "CellCtl.Rule"
      },
      "Name": "rule1",
      "_Box.Name": "box1",
      "EventExternal": true,
      "EventSubject": null,
      "EventType": null,
      "EventObject": null,
      "EventInfo": null,
      "Action": "log",
      "TargetUrl": null,
      "__published": "/Date(1486368212581)/",
      "__updated": "/Date(1486368212581)/"
    }
  }
}
```

### Error response
[Error message list](004_Error_Messages.md) is referred to

## cURL Sample

```sh
curl "https://cell1.unit1.example/__ctl/Rule" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{"Name":"rule1", "EventExternal":true, "Action":"log"}'
```