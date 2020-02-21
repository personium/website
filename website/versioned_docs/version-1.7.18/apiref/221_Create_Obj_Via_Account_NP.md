---
id: version-1.7.18-221_Create_Obj_Via_Account_NP
title: Create other objects via Account's Navigation Property
sidebar_label: Create other objects via Account's Navigation Property
original_id: 221_Create_Obj_Via_Account_NP
---

## Overview

register Role via Account Navigation Property

### Required Privileges

write

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

#### Navigation Property to Role

```
{CellURL}__ctl/Account(Name='{AccountName}')/_Role
```

or

```
{CellURL}__ctl/Account('{AccountName}')/_Role
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
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

When registering Role

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|Account Name|Character type: Half size alphanumeric characters and following half-width symbol (-_!$*=^`{&#124;}~.@) <br>However, the first character can not be specified as the first character|Yes||

### Request Sample

```JSON
{
  "Name": "account1"
}
```


## Response

### Response Code

201

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|Content-Type|Format of data to be returned||
|Location|URL to the resource that was created||
|ETag|Resource version information||
|DataServiceVersion|OData version||

### Response Body

|Item Name|Overview|Notes|
|:--|:--|:--|
|d|||
|d / results|||
|d / results / __published|Created date||
|d / results / __updated|Updated date||
|d / results / __metadata|||
|d / results / __metadata / etag|ETag value||
|d / results / __metadata / uri|URL to the resource that was created||
|d / results / __metadata / type|EntityType||
|d / results / Name|Role Name||
|d / results / _Box.Name|Box name to be related||

#### When registered Account

Account specific response body

|Object|Item Name|Data Type|Notes|
|:--|:--|:--|:--|
|{2}|Name|string|Account name|
|{2}|Cell|string|null|
|{2}|Type|string|basic|
|{3}|Type|string|CellCtl.Account|

### Response Sample

```JSON
{
  "d": {
    "results": {
      "Name": "account1",
      "__published": "/Date(1349355810698)/",
      "Cell": null,
      "__updated": "/Date(1349355810698)/",
      "Type": "basic",
      "__metadata": {
        "etag": "1-1349355810698",
        "type": "CellCtl.Account",
        "uri": "https://cell1.unit1.example/__ctl/Account('account1')"
      }
    }
  }
}   
```

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

### Register via Account and Role Navigation Property

```sh
curl "https://cell1.unit1.example/__ctl/Account('account1')/_Role" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{"Name":"role1"}'
```


