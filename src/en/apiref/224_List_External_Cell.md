# Retrieve List of ExtCell

## Overview

acquire existed ExtCell

### Required Privileges

auth-read

### Restrictions

* Accept in the request header is ignored
* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* $formatQuery options ignored


## Request

### Request URL

```
{CellURL}__ctl/ExtCell
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

|Header Name|Summary|Valid Value|Required|Remarks|
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

|Object|Item Name|Data Type|Remarks|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

### ExtCell specific response body

|Object|Item Name|Data Type|Notes|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ExtCell|
|{2}|Url|string|URL of target Cell|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri":
          "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell2.unit1.example%2F')",
          "etag": "W/\"1-1486519006899\"",
          "type": "CellCtl.ExtCell"
        },
        "Url": "https://cell2.unit1.example/",
        "__published": "/Date(1486519006899)/",
        "__updated": "/Date(1486519006899)/",
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell2.unit1.example%2F')
/_Role"
          }
        },
        "_Relation": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell2.unit1.example%2F')
/_Relation"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell3.unit1.example%2F')",
          "etag": "W/\"1-1486520191416\"",
          "type": "CellCtl.ExtCell"
        },
        "Url": "https://cell3.unit1.example/",
        "__published": "/Date(1486520191416)/",
        "__updated": "/Date(1486520191416)/",
        "_Role": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell3.unit1.example%2F')
/_Role"
          }
        },
        "_Relation": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell3.unit1.example%2F')
/_Relation"
          }
        }
      }
    ]
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/ExtCell" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```
