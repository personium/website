---
id: version-1.7.18-214_List_Account
title: Retrieve List of Account
sidebar_label: Retrieve List of Account
original_id: 214_List_Account
---

## Overview

Obtain a list of existing Account information

### Required Privileges

auth-read

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{CellURL}__ctl/Account
```

### Request Method

GET

### Request Query

The following query parameters are available

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

[$select  Query](406_Select_Query.md)

[$expand  Query](405_Expand_Query.md)

[$format  Query](404_Format_Query.md)

[$filter  Query](403_Filter_Query.md)

[$inlinecount  Query](407_Inlinecount_Query.md)

[$orderby  Query](400_Orderby_Query.md)

[$top  Query](401_Top_Query.md)

[$skip  Query](402_Skip_Query.md)

[Full-text Search (q) Query](408_Full_Text_Search_Query.md)

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

None


## Response

### Response Code

200

### Response Header

None

### Response Body

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

### Account specific response body

|Object|Item Name|Type|Notes|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.Account|
|{2}|Name|string|Account name|
|{2}|IPAddressRange|string|default: null|
|{2}|Status|string|default: "active"|
|{2}|Type|string|default: "basic"|
|{2}|Cell|string|default: null|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Account('account1')",
          "etag": "W/\"1-1486462510467\"",
          "type": "CellCtl.Account"
        },
        "Name": "account1",
        "IPAddressRange": null,
        "Status": "active",
        "Type": "basic",
        "Cell": null,
        "__published": "/Date(1486462510467)/",
        "__updated": "/Date(1486462510467)/",
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account1')/_Role"
          }
        },
        "_ReceivedMessageRead": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account1')/_ReceivedMessageRead"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Account('account2')",
          "etag": "W/\"1-1486465908803\"",
          "type": "CellCtl.Account"
        },
        "Name": "account2",
        "IPAddressRange": "192.127.0.2,192.128.0.0/24",
        "Status": "deactivated",
        "Type": "basic",
        "Cell": null,
        "__published": "/Date(1486465908803)/",
        "__updated": "/Date(1486465908803)/",
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account2')/_Role"
          }
        },
        "_ReceivedMessageRead": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Account('account2')/_ReceivedMessageRead"
          }
        }
      }
    ]
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/Account" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


