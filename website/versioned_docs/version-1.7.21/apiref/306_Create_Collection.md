---
id: version-1.7.21-306_Create_Collection
title: Create Collection
sidebar_label: Create Collection
original_id: 306_Create_Collection
---

## Overview

Create a collection

### Required Privileges

write

## Request

### Request URL

```
{CellURL}{BoxName}/{CollectionName}
```

|Path|Overview|Notes|
|:--|:--|:--|
|{CellName}|Cell Name||
|{BoxName}|Box Name||
|{CollectionName}|Collection Name|Valid values Number of digits:1-256<br>Specify a percent-encoded character string(character code:UTF-8)|

### Request Method

MKCOL

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

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

### Request Body

#### Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

#### Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|mkcol|D:|Element|Represents the root element of mkcol, set is a child||
|set|D:|Element|Property setting, prop is a child||
|prop|D:|Element|It represents a property setting value, and resourcetype is a child||
|resourcetype|D:|Element|It represents a resource type setting, and one of collection / odata / service is a child||
|collection|D:|Element|Represent a collection|If only the collection node is specified WebDAV collection creation becomes|
|odata|p:|Element|Represents an OData collection|If collection node and odata node are specified OData collection creation|
|service|p:|Element|Represents a Service collection|If collection node and service node are specified Service collection creation|

#### DTD notation

#### Namespace D:

```dtd
<!ELEMENT mkcol (set) >
<!ELEMENT set (prop) >
<!ELEMENT prop (resourcetype) >
<!ELEMENT resourcetype (collection or odata or service) >
<!ELEMENT collection EMPTY>   
```

#### Namespace p:

```dtd
<!ELEMENT odata EMPTY>
<!ELEMENT service EMPTY>
```

### Request Sample

Create WebDAV collection

```xml
<?xml version="1.0" encoding="utf-8"?>
<D:mkcol xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <D:resourcetype>
        <D:collection/>
      </D:resourcetype>
    </D:prop>
  </D:set>
</D:mkcol>
```

Create OData collection

```xml
<?xml version="1.0" encoding="utf-8"?>
<D:mkcol xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <D:resourcetype>
        <D:collection/>
        <p:odata/>
      </D:resourcetype>
    </D:prop>
  </D:set>
</D:mkcol>
```

Create Service Collection

```xml
<?xml version="1.0" encoding="utf-8"?>
<D:mkcol xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <D:resourcetype>
        <D:collection/>
        <p:service/>
      </D:resourcetype>
    </D:prop>
  </D:set>
</D:mkcol>
```


## Response

### Response Code

201

### Response Header

#### Common Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

#### WebDAVCommon Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|ETag|Resource version information|Return only when collection can be created successfully|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

Create WebDAV collection

```sh
curl "https://cell1.unit1.example/box1/collection1" -X MKCOL -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8"?><D:mkcol xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">\
<D:set><D:prop><D:resourcetype><D:collection/></D:resourcetype></D:prop></D:set></D:mkcol>'
```

Create OData collection

```sh
curl "https://cell1.unit1.example/box1/collection1" -X MKCOL -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8"?><D:mkcol xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">\
<D:set><D:prop><D:resourcetype><D:collection/><p:odata/>\
</D:resourcetype></D:prop></D:set></D:mkcol>'
```

Create Service Collection

```sh
curl "https://cell1.unit1.example/box1/collection1" -X MKCOL -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8"?><D:mkcol xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">\
<D:set><D:prop><D:resourcetype><D:collection/><p:service/></D:resourcetype></D:prop></D:set>\
</D:mkcol>'
```

