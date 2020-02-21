---
id: version-1.7.18-313_Change_Property
title: Change file setting
sidebar_label: Change file setting
original_id: 313_Change_Property
---

## Overview

Change properties

### Required Privileges

write-properties

## Request

### Request URL

```
{CellURL}
```

or

```
{CellURL}{BoxName}
```

or

```
{CellURL}{BoxName}/{ResourcePath}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{ResourcePath}|Path to resource|Valid values Number of digits:1-256|

### Request Method

PROPPATCH

### Request Query

#### Common Request Query

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

#### Individual Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Content-Type|Specify content format|application/xml|No||
|Accept|Specify acceptable media types in response|application/xml|No||

### Request Body

#### Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

#### Structure of XML

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|propertyupdate|D:|Element|It represents the root of propertyupdate, and set and remove are children||
|set|D:|Element|Represents a property setting, and one or more props are children||
|remove|D:|Element|Represents a property deletion setting, and one or more props are children||
|prop|D:|Element|Represents a property value, and one or more arbitrary elements are children|When set: Child node name is key<br>When remove: Delete with child node name as key|

#### DTD notation

```dtd
<!ELEMENT propertyupdate (set, remove) >
<!ELEMENT set (prop*) >
<!ELEMENT remove (prop*) >
<!ELEMENT prop ANY>
```

### Request Sample

```xml
<D:propertyupdate xmlns:D="DAV:"
    xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:property-key1>property-value1</p:property-key1>
    </D:prop>
  </D:set>
  <D:remove>
    <D:prop>
      <p:property-key2/>
    </D:prop>
  </D:remove>
</D:propertyupdate>
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|207|Multi-Status|Success|

### Response Body

#### Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

#### Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|multistatus|D:|Element|Represents the route of multistatus and one or more responses are children||
|response|D:|Element|Represents the contents of multistatus, and href and propstat are children||
|href|D:|Element|URL of the resource that executed PROPPATCH||
|propstat|D:|Element|Represents property setting result, prop and status are children||
|prop|D:|Element|Represents property setting contentsbr|Display the result of resource setting as follows <br> Setting Succeeded: Set Key and Value <br> Deleted Successful: Deleted Key|
|status|D:|Element|Property setting status code|In the case of setting success 200 (OK) is returned|

#### DTD notation

#### namespace D:

```dtd
<!ELEMENT multistatus (response*)>
<!ELEMENT response (href, propstat)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT propstat (prop, status)>
<!ELEMENT prop ANY>
<!ELEMENT status (#PCDATA)   
```

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/box1/{ResourcePath}</href>
    <propstat>
      <prop>
        <p:property-key1 xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">
          property-value1
        </p:property-key1>
        <p:property-key2 xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:"/>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/{ResourcePath}" -X PROPPATCH -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8" ?><D:propertyupdate xmlns:D="DAV:" \
xmlns:p="urn:x-personium:xmlns"><D:set><D:prop><p:property-key1>property-value1</p:property-key1>\
</D:prop></D:set><D:remove><D:prop><p:property-key2/></D:prop></D:remove></D:propertyupdate>'
```

