---
id: 305_Get_Property
title: Retrieve of collection settings
sidebar_label: Retrieve of collection settings
---

## Overview

Get collection settings

### Required Privileges

read-properties

* When acquiring ACL setting status, read-acl is required together

### Restrictions

Restriction on V1.0 series

* Function to specify properties to be returned in the response body (it becomes current allprop)


## Request

### Request URL

```
{CellURL}{BoxName}
```

or

```
{CellURL}{BoxName}/{CollectionName}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{CollectionName}|Collection Name|Valid values Number of digits:1-256|

### Request Method

PROPFIND

### Request Query

#### Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

#### WebDav Common Request Query

None

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

#### Individual Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Depth|Resource hierarchy to be acquired|0: Resource itself itself <br> 1: Resource of interest and resource right under it|Yes||

### Request Body

Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|propfind|D:|Element|Represents the root element of propfind and allprop is a child||
|allprop|D:|Element|Obtain all properties Get|Allprop... get all properties<br>Even if the request body is empty, treat it as allprop<br>Elements other than allprop are not supported for v1.2 series, v1.1 series|

DTD notation

```dtd
<!ELEMENT propfind (allprop) >
<!ELEMENT allprop ENPTY >
```

### Request Sample

```xml
<?xml version="1.0" encoding="utf-8"?>
<D:propfind xmlns:D="DAV:">
  <D:allprop/>
</D:propfind>
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|207|Multi-Status|Success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData version information|Return only when Entity can be successfully acquired|

### Response Body

Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|multistatus|D:|Element|Represents the route of multistatus and one or more responses are children||
|response|D:|Element|Represents a response to resource acquisition, href and propstat are children||
|href|D:|Element|Resource url||
|propstat|D:|Element|Represents property information of a resource, status and prop are children||
|status|D:|Element|Represents the response code of resource acquisition||
|prop|D:|Element|Property detailed information, creationdate, resourcetype, acl, and proppatch setting values are children||
|creationdate|D:|Element|Resource creation time||
|getcontentlength|D:|Element|Resource size|Only when the resource is a file|
|getcontenttype|D:|Element|Resource contenttype|Only when the resource is a file|
|getlastmodified|D:|Element|Resource update time||
|resourcetype|D:|Element|Represents the type of resource. <br> collection, either odata or service is a child, or the child is empty||
|collection|D:|Element|Represents that the resource type is a collection|If the resource is WebDAV, only this element is displayed|
|odata|p:|Element|Represents that the resource type is an OData collection|For OData collection display|
|service|p:|Element|Represents that the resource type is a service collection|For Service collection Display|
|acl|D:|Element|ACL setting set for resource|In order to acquire the ACL setting, acl-read authority for the target resource is required. <br> ACL element For content below, see the [cell level access control setting API](289_Cell_ACL.md)|
|base|xml:|Attributes|ACL Privilege BaseURL|In the case of PROPFIND to Cell, the resource URL of the default box ("__")|

DTD notation

namespace D:

```dtd
<!ELEMENT multistatus (response*)>
<!ELEMENT response (href, propstat)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT propstat (status, prop)>
<!ELEMENT status (#PCDATA)>
<!ELEMENT prop (creationdate, resourcetype, acl, ANY)>
<!ELEMENT creationdate (#PCDATA)>
<!ELEMENT getcontentlength (#PCDATA)>
<!ELEMENT getcontenttype (#PCDATA)>
<!ELEMENT getlastmodified (#PCDATA)>
<!ELEMENT resourcetype ((collection, (odata or service) or EMPTY))>
<!ELEMENT collection EMPTY>
<!ELEMENT acl (ace*)>
```

namespace p:

```dtd
<!ELEMENT odata EMPTY>
<!ELEMENT service EMPTY>
```

namespace xml:

```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```xml
<multistatus xmlns="DAV:">
  <response>
     <href>https://cell1.unit1.example/box1/collection1</href>
    <propstat>
      <prop>
        <creationdate>2017-02-15T01:52:34.635+0000</creationdate>
        <getlastmodified>Wed, 15 Feb 2017 01:52:34 GMT</getlastmodified>
        <resourcetype>
          <collection/>
        </resourcetype>
        <acl xmlns:p="urn:x-personium:xmlns"/>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/collection1" -X PROPFIND -i  -H 'Depth:1' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8"?><D:propfind xmlns:D="DAV:"><D:allprop/></D:propfind>'
```

