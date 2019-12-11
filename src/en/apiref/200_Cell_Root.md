# Retrieve Cell Root

## Overview

Get the HTML file set as the cell route.

### Precondition

[Unit setting](../../server-operator/unit_config_list.md) or [target cell property setting](./291_Cell_Change_Property.md) is required. When both are set, the property setting of the target cell takes precedence.  

Unit setting  
```
io.personium.core.cell.relayhtmlurl.default={URL that html can obtain}
```

Target cell property setting  
```xml
<p:relayhtmlurl>{URL that html can obtain}</p:relayhtmlurl>
```
The schemes that can be specified as URL are "http", "https", "personium-localunit", "personium-localcell".

### Required Privileges

None


## Request

### Request URL

```
{CellURL}
```

### Request Method

GET

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Specifies the response body format|text/html|No|[text/html] by default|


## Response

### Response Code

200

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|Personium API version|Version of the API used to process the request|

### Response Body

HTML obtained from the URL set in the property of the target cell.

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/" -X GET -i -H 'Accept: text/html'
```
