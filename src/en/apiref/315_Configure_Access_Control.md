# Box Level Access Control Configuration

## Overview

Provides box level access control functions

### Required Privileges

write-acl

### Restrictions

* When ACL setting is done, the existing ACL setting is overwritten and updated
* The function to deny ACL configuration (deny)
* Acquisition of a list of privileges configurable by the ACL


## Request

### Request URL

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

ACL

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML  
The body is XML and follows the following schema.  
See acl\_model ([access control model](006_Access_Control.md)) for the contents of privilege setting under the privilege tag.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|acl|D:|Element|Denotes the root of the ACL (Access Control List); one or more ace nodes will be its child||
|base|xml:|Attributes|Href Represents the base of the URL described in the tag and sets an arbitrary value as the attribute value. This attribute is optional.||
|ace|D:|Element|Denotes the privilege configuration target; href or all will be its child|"invert", "deny", "protected", and "inherited" are not supported in V 1.1 systems|
|principal|D:|Element|Denotes the privilege configuration target; href or all will be its child||
|grant|D:|Element|Denotes the privilege grant setting; one or more privilege nodes will be its child node||
|href|D:|Element|Denotes the privilege configuration target role and is the text node to input the role resource URL|Specify resource URL of privilege setting target role<br>It is possible to shorten the URL using the xml:base attribute setting in the acl element|
|all|D:|Element|All access entity privilege setting||
|privilege|D:|Element|Denotes the privilege setting; one of the following elements will be its child||
|read|D:|Element|Reference authority||
|write|D:|Element|Edit permission||
|read-properties|D:|Element|Property reference authority||
|write-properties|D:|Element|Edit property authority||
|read-acl|D:|Element|ACL setting reference authority||
|write-acl|D:|Element|ACL setting edit permission||
|bind|D:|Element|Member URL addition authority|Not supported|
|unbind|D:|Element|Member URL deletion authority|Not supported|
|exec|D:|Element|Service execution authority||

DTD notation

namespace D:

```dtd
<!ELEMENT acl (ace*) >
<!ELEMENT ace ((principal or invert), (grant or deny), protected?,inherited?)>
<!ELEMENT principal (href or all)>
<!ELEMENT principal (privilege*)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT all EMPTY>
<!ELEMENT privilege (all or read or write or read-properties or write-properties or read-acl or write-acl or exec or bind or unbind)>
<!ELEMENT read EMPTY>
<!ELEMENT write EMPTY>
<!ELEMENT read-properties EMPTY>
<!ELEMENT write-properties EMPTY>
<!ELEMENT read-acl EMPTY>
<!ELEMENT write-acl EMPTY>
<!ELEMENT bind EMPTY>
<!ELEMENT unbind EMPTY>
<!ELEMENT exec EMPTY>
```

namespace p:

```dtd
<!ATTLIST acl requireSchemaAuthz (none or public or confidential) #IMPLIED>
<!ELEMENT exec EMPTY>   
```

namespace xml:

```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

### Request Sample

```xml
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns"
       xml:base="https://cell1.unit1.example/__role/box1/"
       p:requireSchemaAuthz="public">
  <D:ace>
    <D:principal>
      <D:all/>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>role</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
      <D:privilege><D:write/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|200|OK|Success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|Only when it failed at the time of update / creation, return it|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/box1/collection1" -X ACL -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8" ?><D:acl xmlns:D="DAV:" \
xml:base="https://cell1.unit1.example/__role/box1/" xmlns:p="urn:x-personium:xmlns" \
p:requireSchemaAuthz="none"><D:ace><D:principal><D:href>role1</D:href></D:principal><D:grant>\
<D:privilege><D:read/></D:privilege><D:privilege><D:write/></D:privilege></D:grant></D:ace></D:acl>'
```


