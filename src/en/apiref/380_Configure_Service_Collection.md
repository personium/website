---
id: 380_Configure_Service_Collection
title: Apply Settings Service Collection Source
sidebar_label: Apply Settings Service Collection Source
---

## Overview

Apply service collection source settings

### Required Privileges

write-properties


## Request

### Request URL

```
{CellURL}{BoxName}/{CollectionName}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{CollectionName}|Service Collection Name|Valid values <br>Number of digits:1-256|

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
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

#### Service Collection Settings Specific Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specify content format|application/xml|No||
|Accept|Specify acceptable media types in response|application/xml|No||

### Request Body

Namespace

|URI|Overview|reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium API namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML  
The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|propertyupdate|D:|Element|It represents the root of propertyupdate, and set and remove are children||
|set|D:|Element|Represents a property setting, and one or more props are children||
|remove|D:|Element|Represents a property deletion setting, and one or more props are children||
|prop|D:|Element|Represents a property value, and one or more arbitrary elements are children|When set: Child node name is key<br>When remove: Delete with child node name as key|

DTD notation

```dtd
<!ELEMENT propertyupdate (set, remove)
<!ELEMENT set (prop*) >
<!ELEMENT remove (prop*) >
<!ELEMENT prop ANY>
```

### Service collection setting specific definition

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|service|p:|element|It represents a service setting, and one or more multiple path elements are children||
|language|p:|Attributes|It represents the service source language setting, and "JavaScript" is fixed as attribute value||
|subject|p:|Attributes|It represents the service subject setting and sets the Account name registered in the cell belonging to as the attribute value|Execute with the Role privilege attached to the Account in which the Personium API in the logic is set up|
|path|p:|Element|Represents a service collection setting.||
|name|p:|Attributes|Represents a service call name and an arbitrary character as an attribute value|This setting value becomes the "__src/" path name immediately under the request URL when the service is executed.|
|src|p:|Attributes|Represents the service source file name, and sets the file name deployed under __src as the attribute value||

DTD notation

```dtd
<!ELEMENT service (path*)>
<!ATTLIST service language CDATA "JavaScript">
<!ATTLIST service subject CDATA #IMPLIED>
<!ELEMENT path EMPTY>
<!ATTLIST path name CDATA #REQUIRED>
<!ATTLIST path src CDATA #REQUIRED>
```

### Request Sample

```xml
<D:propertyupdate xmlns:D="DAV:"
    xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:service language="JavaScript">
        <p:path name="${name}" src="${src}"/>
      </p:service>
    </D:prop>
  </D:set>
</D:propertyupdate>
```


## Response

### Response Code

207

### Response Header

None

### Response Body

Namespace

|URI|Overview|reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML  
The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|multistatus|D:|Element|Represents the route of multistatus and one or more responses are children||
|response|D:|Element|Represents the contents of multistatus, and href and propstat are children||
|href|D:|Element|URL of the resource that executed PROPPATCH||
|propstat|D:|Element|Represents property setting result, prop and status are children||
|prop|D:|Element|Represents property setting contents|Display the result of resource setting as follows<br>Successful setting: set key and value<br>Deleted Successful: Deleted key|
|status|D:|Element|Property setting status code|In the case of setting success 200 (OK) is returned|

DTD notation

```dtd
<!ELEMENT multistatus (response*)>
<!ELEMENT response (href, propstat)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT propstat (prop, status)>
<!ELEMENT prop ANY>
<!ELEMENT status (#PCDATA)>
```

### Response Sample

```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/box1/odata-collection1</href>
    <propstat>
      <prop>
        <p:service language="JavaScript" xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">
          <p:path name="sample" src="sample.js"/>
        </p:service>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1" -X PROPPATCH -i -H \
"Authorization:Bearer AA~PBDc...(snip)...FrTjA" -H "Accept:application/json" -d "<?xml version=\"1.0\" \
encoding=\"utf-8\" ?><D:propertyupdate xmlns:D=\"DAV:\" xmlns:p=\"urn:x-personium:xmlns\"><D:set>\
<D:prop><p:service language=\"JavaScript\"><p:path name=\"sample\" src=\"sample.js\"/></p:service>\
</D:prop></D:set></D:propertyupdate>"
```


