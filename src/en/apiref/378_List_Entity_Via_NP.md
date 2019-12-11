# Retrieve other objects list via Entity's Navigation Property

## Overview

Get Entity list of user data via Navigation Property.

### Required Privileges

read


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/{EntityTypeName}('{EntityID}')/{NavigationPropertyName}
```

|Path|Overview|
|:--|:--|
|{CellName}|Cell Name|
|{BoxName}|Box Name|
|{ODataCollecitonName}|Collection Name|
|{EntityTypeName}|EntityTypeName|
|{EntityID}|EntityID|
|{NavigationPropertyName}|NavigationProperty name|

NavigationProperty name that can be specified is limited to those having the following relation with EntitySet.

|From|To|
|:--|:--|
|0 .. 1|0 .. 1|
|0 .. 1|1|
|0 .. 1|*|
|1|0 .. 1|
|1|1|
|1|*|
|*|0 .. 1|
|*|1|
|*|*|

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
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

None


## Response

### Response Code

200

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData version information|Return only when Entity can be created successfully|

### Response Body

The response is a JSON object, the correspondence between the key (name) and type defined in the object (subobject) and the value is as follows

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{3}|type|string|EntityType name|
|{2}|__id|string|EntityID(__id)|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{2}|{NP name}|string|Object{4}<br>It is returned only when Link is connected. {NP name}: NavigationPropert name|
|{4}|__deferred|object|Object{5}|
|{5}|uri|string|uri of the resource that has the relationship|
|{1}|__count|string|Get number of results in $inlinecount query|

In addition to the above, return the schema-set item or the dynamic item specified at the time of registration

#### Numerical treatment

#### Decimal value(Edm.Single)

* The handling when acquiring UserOData in JSON format is as follows
    * The value that the decimal part such as 10.0 becomes 0 is returned as an integer value

#### Numerical value(Edm.Double)

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
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')",
          "etag": "W/\"2-1487645572476\"",
          "type": "UserData.entity-type1"
        },
        "__id": "100-1_20101108-111352093",
        "__published": "/Date(1487645572476)/",
        "__updated": "/Date(1487645572476)/",
        "TestProperty": null,
        "_TestEntity": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('100-1_20101108-111352093')/navigation-property1"
          }
        }
      }
    ]
  }
}

```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('100-1_20101108-111352093')\
/navigation-property1" -X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H \
'Accept: application/json'
```


