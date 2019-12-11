# Update Entity

## Overview

Update Entity of user data.

### Required Privileges

write

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error
* User data restrictions
    * Property scope of Edm.DateTime type is not properly checked
    * Array of Edm.DateTime type is not supported
    * If SYSUTCDATETIME () is specified as the property of Edm.DateTime type, the set system time may be different
    * When setting in request body and setting with DefaultValue (\_\_published, \_\_ updated is the latter timing)
    * For EntityType, you can create up to 400 DynamicProperty / DeclaredProperty / ComplexTypeProperty


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}({EntityID})}
```

|Path|Overview|
|:--|:--|
|{CellName}|Cell Name|
|{BoxName}|Box Name|
|{ODataCollecitonName}|Collection Name|
|{EntityTypeName}|EntityType name|
|{EntityID}|ID of Entity to update|

### Request Method

PUT

### Request Query

#### Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

#### OData Common Request Query

None

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

#### OData Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

#### OData Update Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Contents-Type|Specifies authentication information in the OAuth 2.0 format|application/json|No|When omitted, treat it as [application/json]|
|Accept|Specifies the response body format|application/json|No|When omitted, treat it as [application/json]|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

#### Property

Set up schema-defined properties and dynamic (schema undefined) properties, up to 400 properties in total  
Contains the number of properties defined by ComplexType in the above

#### Schema defined properties

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Property associated with EntityType|User defined item|Based on DefaultValue of default value Property|Based on Property Nullable||

#### Valid value of value of schema-defined property

|Data type|Effective Value|
|:--|:--|
|String|Number of digits: 0-51200 byte<br>Character type: When a control code is used as a value of a character string, return it in an escaped state at the time of acquisition<br>When "\\" is used, it must be specified with "\\\\"<br>When an integer value, a decimal value, a boolean value, or a date type value is set in a property of a character string type, it is converted into a character string type and registered|
|Integer value|-2147483648 - 2147483647|
|Decimal point|Number of digits in integer part: 1-5 digits<br>Number of digits in decimal part: 1-5 digits|
|Boolean value|true / false / null(treat null as false)|
|Date|It is specified as a character string in the format of Date ([time of long type])<br>The valid value of [time of long type] is -6847804800000(1753-01-01T00:00:00.000Z)-253402300799999(9999-12-31T23:59:59.999Z)<br>In addition, you can specify the following as reserved words<br>SYSUTCDATETIME (): server time|

#### Dynamic (schema undefined) property

Set up schema-defined properties and dynamic (schema-undefined) properties, up to 400 properties in total  
Contains the number of properties defined by ComplexType in the above

#### Valid value of dynamic property's key

|Data type|Effective Value|
|:--|:--|
|String|Number of digits: 1-128 :<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_")<br>However, - (hyphen) and _ (underscore) can not be specified as the first character <br>_published, _updated is a reserved word, so it is not possible to specify the request body|

#### Valid value of value of dynamic property

Same as valid value of value of schema-defined property  
Array, associative array can not be specified

### Request Sample

```JSON
{"animalId": "100-2","name": "episode2","startedAt": "2016-02-21","episodeType": "care2","endedAt": "",
"outcome": "Treated"}
```


## Response

### Response Code

204

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|ETag|Resource version information||
|DataServiceVersion|OData version||

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('100-1_20101108-111352093')" \
-X PUT -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' -d \
'{"animalId": "100-2","name": "episode2","startedAt":"2016-02-21","episodeType": "care2","endedAt": \
"","outcome":  "Treated"}'
```


