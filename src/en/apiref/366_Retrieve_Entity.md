# Retrieve Entity

## Overview

We acquire one entity Entity of user data.

### Required Privileges

read

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
|{EntityID}|ID of the Entity to acquire|

### Request Method

GET

### Request Query

The following query parameters are available

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only when no Authorization header is specified Specify when using authentication information of cookie|

[$select  Query](406_Select_Query.md)

[$expand  Query](405_Expand_Query.md)

[$format  Query](404_Format_Query.md)

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

#### OData Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Specify the format of the response body|application/json|No|When omitted, treat it as [application/json]|
|If-None-Match|Specify the value of ETag, if there is no change, 304, if it is changed return the latest resource||No|Specified when acquiring Entity not matching ETag<br>Not compatible|

### Request Body

None


## Response

### Response Code

200

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData version information|Return only when Entity can be successfully acquired|

### Response Body

The response is a JSON object, the correspondence between the key (name) and type defined in the object (subobject) and the value is as follows

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{3}|type|string|UserData.{EntityTypeName}|
|{2}|__id|string|EntityID(__id)|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{2}|_{NP name}|string|Object{4}<br>It is returned only when Link is connected. {NP name}: NavigationPropert name|
|{4}|__deferred|object|Object{5}|
|{5}|uri|string|uri of the resource that has the relationship<br>Not tested|
|{1}|__count|string|Get number of results in $inlinecount query|

Return items that were schema-set other than the above, or dynamic items specified at registration

#### Numerical treatment

#### Decimal value (Edm.Single type)

* The handling when acquiring UserOData in JSON format is as follows
    * The value that the decimal part such as 10.0 becomes 0 is returned as an integer value

#### Numerical value (Edm.Double type)

\*Double type handling in Personium follows the Java Double specification

* The handling when acquiring UserOData in JSON format is as follows
    * The value that the decimal part such as 10.0 becomes 0 is returned as an integer value
* About the value to be returned
    * When the input value at the time of registration is a number having accuracy of double precision or more, data is registered by being rounded to double precision
        * Internally, it is managed as a floating point number, but at the time of output, it converts it to fixed point number representation within the range where no information drop occurs and outputs it  
            When output fixed-point number is used for input, the same number of inputs and original number is guaranteed

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('{EntityID}')",
        "etag": "W/\"1-1487662179733\"",
        "type": "UserData.entity-type1"
      },
      "__id": "100-1_20101108-111352093",
      "__published": "/Date(1487662179733)/",
      "__updated": "/Date(1487662179733)/",
      "PetName": null,
      "animalId": "100-1",
      "endedAt": "",
      "episodeType": "care",
      "name": "episode",
      "outcome": "During treatment",
      "startedAt": "2010-11-08"
    }
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('{100-1_20101108-111352093}')" \
-X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


