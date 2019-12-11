# ULUUT elevation setting PROPPATCH

## Overview

This API changes the UUT (Unit User Token) upgraded settings.

### Required Privileges

Only unit users permitted

## Request

### Request URL

```
{CellURL}
```

|Path|Overview|
|:--|:--|
|{CellName}|Cell Name|

### Request Method

PROPPATCH

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specify content format|application / xml|No||
|Accept|Specify acceptable media types in response|application / xml|No||

### Request Body

|Item Name|Namespace|Overview|Required|Effective Value|Notes|
|:--|:--|:--|:--|:--|:--|
|DAV:||XML namespace setting|Yes|"DAV:"||
|urn: x-personium: xmlns||XML namespace setting|Yes|"Urn: x-personium: xmlns"||
|http://www.w3.com/standards/z39.50/||XML namespace setting|Yes|"http://www.w3.com/standards/z39.50/"||
|propertyupdate|DAV:|propertyupdate (Access Control List) root|Yes|||
|set|DAV:|set property|No|<! ELEMENT set (prop *)>||
|remove|DAV:|remove property|No|<! ELEMENT set (prop *)>||
|prop|DAV:|remove property value|No|<! ELEMENT prop ANY>|Delete using the XML tag specified as ANY as a key|
|prop|DAV:|set property value|No|<! ELEMENT prop ANY>|The XML tag specified as ANY is the key|
|ownerRepresentativeAccounts||Upgrade setting|Yes|<! ELEMENT ownerRepresentativeAccounts (account *)>||
|account||Account setting for upgrade|Yes|<! ELEMENT account ANY>|Specify an account name that allows upgrade as a value|

### Structure of XML

#### The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|propertyupdate|D:|Element|It represents the root of propertyupdate, and set and remove are children||
|set|D:|Element|Represents a property setting, and one or more props are children||
|remove|D:|Element|Represents a property deletion setting, and one or more props are children||
|prop|D:|Element|Represents a property value, and one or more arbitrary elements are children|When set: Child node name is key<br>When remove: Delete with child node name as key|

### DTD notation

```dtd
<!ELEMENT propertyupdate (set, remove) >
<!ELEMENT set (prop*) >
<!ELEMENT remove (prop*) >
<!ELEMENT prop ANY>
```

### ULUUT elevation setting factor

#### The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|ownerRepresentativeAccounts|p:|Element|Represents an elevation setting list, one or more account elements are children||
|account|p:|Element|Describe account setting for promotion and describe account name to be promoted||

### DTD notation

```dtd
<!ELEMENT ownerRepresentativeAccounts (account*)>
<!ELEMENT account (#PCDATA)>
```

### Request Sample

```xml
<D:propertyupdate xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:ownerRepresentativeAccounts><p:account>account1</p:account><p:account>account2</p:account>
</p:ownerRepresentativeAccounts>
    </D:prop>
  </D:set>
</D:propertyupdate>
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|207|MULTI_STATUS|Success|

### Response Body

Namespace

|URI|Overview|Notes (prefix)|
|:--|:--|:--|
|multistatus|WebDAV Namespace|D:|

### Structure of XML

#### The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|multistatus|D:|Element|Represents the route of multistatus and one or more responses are children||
|response|D:|Element|Represents the contents of multistatus, and href and propstat are children||
|href|D:|Element|URL of the resource that executed PROPPATCH||
|propstat|D:|Element|Represents property setting result, prop and status are children||
|prop|D:|Element|Represents property setting contents|Display the result of resource setting as follows Setting Successful: Set key and value Deleted Successful: Deleted key|
|status|D:|Element|Property setting status code|In the case of setting success 200 (OK) is returned|

### DTD notation

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
    <href>http://localhost:9998/testcell1/box1/patchcol</href>
    <propstat>
      <prop>
        <Z:Author xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:" xmlns:Z=
"http://www.w3.com/standards/z39.50/">Author1 update</Z:Author>
        <p:hoge xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" xmlns:Z=
"http://www.w3.com/standards/z39.50/">fuga</p:hoge>
        <Z:Author xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:" xmlns:Z=
"http://www.w3.com/standards/z39.50/"/>
        <p:hoge xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" xmlns:Z=
"http://www.w3.com/standards/z39.50/"/>
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
curl "https://cell1.unit1.example/ -X PROPPATCH" \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-d '<?xml version="1.0" encoding="utf-8" ?>\
<D:propertyupdate xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" \
xmlns:Z="http://www.w3.com/standards/z39.50/">\
<D:set><D:prop><p:requireSchemaAuthz>confidential</p:requireSchemaAuthz></D:prop></D:set>\
</D:propertyupdate>'
```


