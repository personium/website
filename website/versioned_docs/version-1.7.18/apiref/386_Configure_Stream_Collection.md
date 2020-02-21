---
id: version-1.7.18-386_Configure_Stream_Collection
title: Change settings Stream collection source
sidebar_label: Change settings Stream collection source
original_id: 386_Configure_Stream_Collection
---

## Overview
Change stream collection source settings

### Required Privileges
write-properties

## Request
### Request URL
```
{CellURL}{BoxName}/{CollectionName}
```

### Request Method
PROPPATCH

### Request Query
|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header
|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/xml|No||
|Accept|Specify acceptable media types in response|application/xml|No||

### Request Body

Namespace

|URI|Overview|Notes (prefix)|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML  
The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|propertyupdate|D:|Element|Represents the root of propertyupdate, with set and remove as children||
|set|D:|Element|Represents property settings and one or more props are children||
|remove|D:|Element|Represents property deletion settings, and one or more props become children||
|prop|D:|Element|Represents a property value, and one or more arbitrary elements are children|When set: Child node name is key<br>When remove: Remove using child node as name key|

DTD notation
```dtd
<!ELEMENT propertyupdate (set, remove)
<!ELEMENT set (prop*) >
<!ELEMENT remove (prop*) >
<!ELEMENT prop ANY>
```

### Stream collection setting specific definition
|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|queues|p:|Element|Represents a queue configuration, and has one or more queue elements as children||
|queue|p:|Element|Represents the setting of queue name.||
|topics|p:|Element|Represents a topic setting and has one or more topic elements as children||
|topic|p:|Element|Represents the setting of the topic name.||

DTD notation
```dtd
<!ELEMENT queues (queue*)>
<!ELEMENT queue (#PCDATA)>
<!ELEMENT topics (topic*)>
<!ELEMENT topic (#PCDATA)>
```
### Request Sample
```xml
<D:propertyupdate xmlns:D="DAV:"
    xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:queues>
        <p:queue>queueName</p:queue>
      </p:queues>
      <p:topics>
        <p:topic>topicName</p:topic>
      </p:topics>
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
    <href>https://cell1.unit1.example/box1/stream-collection1</href>
    <propstat>
      <prop>
        <p:queues xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">
          <p:queue>queueName</p:queue>
        </p:queues>
        <p:topics xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">
          <p:topic>topicName</p:topic>
        </p:topics>
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
curl "https://cell1.unit1.example/box1/stream-collection1" -X PROPPATCH -i -H \
"Authorization:Bearer AA~PBDc...(snip)...FrTjA" -H "Accept:application/xml" -d "<?xml version=\"1.0\" \
encoding=\"utf-8\" ?><D:propertyupdate xmlns:D=\"DAV:\" xmlns:p=\"urn:x-personium:xmlns\"><D:set>\
<D:prop><p:queues><p:queue>queueName</p:queue></p:queues><p:topics><p:topic>topicName</p:topic></p:topics>\
</D:prop></D:set></D:propertyupdate>"
```
