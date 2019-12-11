# Execute Service

## Overview

Execute the registered service

### Required Privileges

exec

## Request

### Request URL

```
{CellURL}{BoxName}/{CollectionName}/{ServiceName}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{CollectionName}|Service Collection Name|Valid values <br>Number of digits:1-256|
|{ServiceName}|Specify the name of the registered service|Valid values(limit) <br>Number of digits:1-256|

### Request Method

GET / POST / PUT / DELETE

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

### Request Body

None


## Response

### Response Code

When the script is executed, the response code of the script is returned

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Return script-dependent format|text/html|

### Response Body

When the script is executed, the response body of the script is returned

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/collection1/service1" -X GET -i -H \
"Authorization:Bearer AA~PBDc...(snip)...FrTjA" -H "Accept:application/json"
```


