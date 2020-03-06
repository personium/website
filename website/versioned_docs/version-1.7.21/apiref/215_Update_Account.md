---
id: version-1.7.21-215_Update_Account
title: Update Account
sidebar_label: Update Account
original_id: 215_Update_Account
---

## Overview

Update existing Account information

### Required Privileges

auth

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{CellURL}__ctl/Account(Name='{AccountName}')
```

or

```
{CellURL}__ctl/Account('{AccountName}')
```

### Request Method

PUT

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|
|X-Personium-Credential|Password|String|No|\* Follow the password restrictions of unit setting<br>The default is as follows<br>Number of character:6 - 32<br>Character type: Half size alphanumeric characters and following half-width symbol<br>-_!$\*=^\`{&#124;}~.@|

### Request Body

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|Account Name|Number of digits: 1 - 128<br>Character type: Half size alphanumeric characters and following half-width symbol (-_!$\*=^\`{&#124;}~.@) <br>However, the first character can not be specified as the first character|Yes||
|Type|Account Type|basic(ID/PW authentication)<br>oidc:google(Google OpenID Connect authentication)<br>or divide upper case by space character<br>Description: If omitted, it is updated with basic|No|default: basic|
|IPAddressRange|IP address range|Specify the IP address range for which authentication is permitted<br>Multiple specification with comma delimited, range specification by prefix notation possible<br>When it is null, authentication is enabled with all IP addresses<br>Description: If omitted, it is updated with null|No|default: null|
|Status|status|Specify account status<br>Refer to "Status" of [Create Account](./212_Create_Account.md)<br>Description: If omitted, it is updated with active|No|default: active|

### Request Sample

Account name update

```JSON
{
  "Name": "account2"
}
```

Account name and Account type update

```JSON
{
  "Name": "account2","Type":"oidc:google"
}
```


## Response

### Response Code

204

### Response Header

None

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

Account name update

```sh
curl "https://cell1.unit1.example/__ctl/Account('account1')" -X PUT -i -H \
'If-Match: *' -H 'X-Personium-Credential:password' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H \
'Accept: application/json' -d '{"Name":"account2"}'
```

Account name and Account type update

```sh
curl "https://cell1.unit1.example/__ctl/Account('account1')" -X PUT -i \
-H 'If-Match: *' -H 'X-Personium-Credential:password' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' -d '{"Name":"account2","Type":"oidc:google"}'
```
Account name and Status update
```sh
curl "https://cell1.unit1.example/__ctl/Account('account1')" -X PUT -i -H \
'If-Match: *' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H \
'Accept: application/json' -d '{"Name":"account2","Status":"deactivated"}'
```

Password initialization (force change)
```sh
curl "https://cell1.unit1.example/__ctl/Account('account1')" -X PUT -i -H \
'If-Match: *' -H 'X-Personium-Credential:password' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H \
'Accept: application/json' -d '{"Name":"target_account","Status":"passwordChangeRequired"}'
```
