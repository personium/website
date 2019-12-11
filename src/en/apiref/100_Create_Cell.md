# Create Cell

## Overview

This API creates a new Cell

### Required Privileges

Only unit users permitted

### Restrictions

* OData Restrictions
    * Always handles Content-Type in the request header as application/json
    * Only accepts the request body in the JSON format
    * Only application/json is supported for Content-Type in the request header and the JSON format for the response body
    * Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{UnitURL}__ctl/Cell
```

### Request Method

POST

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|Cell name|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters(lower case), hyphens("-")<br>However, the string cannot start with a hyphens("-")|Yes||

### Request Sample

```JSON
{"Name":"cell1"}
```


## Response

### Response Code

201

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|Location|URL to the resource that was created||
|DataServiceVersion|OData version||
|ETag|Resource version information||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|Personium API version|Version of the API used to process the request|

### Response Body

#### Common

The response is a JSON object defined in an object (subobject)

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

#### Individual response body

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|{3}|type|string|UnitCtl.Cell|
|{2}|Name|string|Cell name|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://unit1.example/__ctl/Cell(Name='cell1')",
        "etag": "W/\"1-1486427790039\"",
        "type": "UnitCtl.Cell"
      },
      "Name": "cell1",
      "__published": "/Date(1486427790039)/",
      "__updated": "/Date(1486427790039)/"
    }
  }
}
```


## cURL Command

```sh
curl "https://unit1.example/__ctl/Cell" -X POST -i \
-H 'Authorization: Bearer PEFzc2V...(snip)...lvbj4' \
-H 'Accept: application/json' -d '{"Name":"cell1"}'
```


