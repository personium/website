# Create Account

## Overview

register Account

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
{CellURL}__ctl/Account
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
|X-Personium-Credential|Password|String|No|\* Follow the password restrictions of unit setting<br>The default is as follows<br>Number of character:6 - 32<br>Character type: Half size alphanumeric characters and following half-width symbol<br>-_!$\*=^\`{&#124;}~.@|

### Request Body

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|Account Name|Number of digits: 1 - 128<br>Character type: Half size alphanumeric characters and following half-width symbol<br>-_!$\*=^\`{&#124;}~.@<br>However, the first character cannot be a half-width symbol|Yes||
|Type|Account Type|basic(ID/PW authentication)<br>oidc:google(Google OpenID Connect authentication)<br>or divide upper case by space character|No|default: basic|
|IPAddressRange|IP address range|Specify the IP address range for which authentication is permitted<br>Multiple specification with comma delimited, range specification by prefix notation possible<br>When it is null, authentication is enabled with all IP addresses|No|default: null|
|Status|status|Specify account status<br>See "Status"|No|default: active|

#### Status
|Value|Overview|Notes|
|:--|:--|:--|
|active|Active||
|deactivated|Deactivated|Authentication for the account always fails.<br>It is assumed that the administrator uses it when you want to freeze the account for some reason.|
|passwordChangeRequired|Password change required|When authenticating to the account, the result that the password change is mandatory (authentication failure) and the token that can be used only for the password change are returned.<br>When [Change Password](./294_Password_Change.md) is executed, the Status of the account is automatically updated to "active".<br>It is assumed that it will be used for initial password assignment and password initialization.|

### Request Sample

ID/PWaccount for authentication

```JSON
{
  "Name": "account1"
}
```

Googleaccount for authentication

```JSON
{
  "Name": "account1","Type":"oidc:google"
}
```

ID/PW authentication +Googleaccount for authentication

```JSON
{
  "Name": "account1","Type":"basic oidc:google"
}
```

Set IP address range

```JSON
{
  "Name": "account1","IPAddressRange":"192.127.0.2,192.128.0.0/24"
}
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
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

|Object|Item Name|Type|Notes|
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

ID/PWaccount for authentication

```JSON
{
  "d": {
    "results": {
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
      "__updated": "/Date(1486462510467)/"
    }
  }
}
```

Googleaccount for authentication

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/Account('account1')",
        "etag": "W/\"1-1486462510467\"",
        "type": "CellCtl.Account"
      },
      "Name": "account1",
      "IPAddressRange": null,
      "Status": "active",
      "Type": "oidc:google",
      "Cell": null,
      "__published": "/Date(1486462510467)/",
      "__updated": "/Date(1486462510467)/"
    }
  }
}
```

ID/PW authentication +Googleaccount for authentication

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/Account('account1')",
        "etag": "W/\"1-1486462510467\"",
        "type": "CellCtl.Account"
      },
      "Name": "account1",
      "IPAddressRange": null,
      "Status": "active",
      "Type": "basic oidc:google",
      "Cell": null,
      "__published": "/Date(1486462510467)/",
      "__updated": "/Date(1486462510467)/"
    }
  }
}
```


## cURL Command

ID/PWaccount for authentication

```sh
curl "https://cell1.unit1.example/__ctl/Account" -X POST -i -H \
'X-Personium-Credential:password' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' -d '{"Name":"account1"}'
```

Googleaccount for authentication

```sh
curl "https://cell1.unit1.example/__ctl/Account" -X POST -i -H \
'X-Personium-Credential:password' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' -d '{"Name":"account1","Type":"oidc:google"}'
```

ID/PW authentication +Googleaccount for authentication

```sh
curl "https://cell1.unit1.example/__ctl/Account" -X POST -i -H \
'X-Personium-Credential:password' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' -d '{"Name":"account1","Type":"basic oidc:google"}'
```
