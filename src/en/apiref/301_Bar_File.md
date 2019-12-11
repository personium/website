# bar File

bar is the file format specified as the request body of the box installation API.  
The bar file stores various data located in Odata/WebDAV/Service defined under the box and is archived in the ZIP format.  
Normally, archived data definitions under the archived box are exported from Personium through the [box export API](385_Box_Export.md).

### Specifications

The file format shall be ZIP, including the ZIP64 format.  
ZIP file encryption is not supported.

#### Directory Structure

The following example shows the directory structure in the bar file.  
If directories and files indicated as "Required" do not exist when the box is installed, an error of no required directory/file (400 Bad Request) is returned.  
```
/
 |
 +-- 00_meta/  *Required
 |    |
 |    +-- 00_manifest.json  *Required
 |    +-- 10_relations.json
 |    +-- 20_roles.json
 |    +-- 30_extroles.json
 |    +-- 50_rules.json
 |    +-- 70_$links.json
 |    +-- 90_rootprops.xml  *Required
 |
 +-- 90_contents/     *The directory name under the same as the collection name
      |
      +-- {OData}/    *Required for OData collection in rootprops.xml
      |    |
      |    +-- 00_$metadata.xml    *Required
      |    +-- 10_odatarelations.json
      |    |
      |    +-- 90_data/
      |         |
      |         +-- {EntityType}/
      |              |
      |              +-- {1.json}
      |
      +-- {Service}/
      |    |
      |    +-- {src.js}
      |
      +-- {dir1}/
           |
           +-- {dir1-1}/
                |
                +-- {userdata1-2.jpg}
                |
                +-- {dir2}/
                     |
                     +-- [userdata1-2.jpg}
```

#### Bar File Version Control

The bar file is upgraded if the data structure is changed in response to enhancement etc., and backward compatibility can no longer be ensured.

* Not upgraded at the level of file addition
* Upgraded if the file format or file name is changed or deleted

### File List

#### 00\_manifest.json

The file describing the information of the box to be installed

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|bar_version|bar file version|Valid version<br>Revised every time the bar file format is changed|Yes|Currently "2"|
|box_version|Box version|Valid version<br>Revised every time the box format is changed|Yes|Any string can be specified but "1" is recommended (for the provision of the box revision function)|
|default_path|Box name in the bar file|Number of digits: 1 to 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_")<br>However, the string cannot start with a single-byte hyphen ("-") or underscore ("\_")<br>null is invalid|Yes||
|schema|Schema name|Number of digits: 1 to 1024<br>Conforming to the URI format (schema: http / https / urn)|Yes||

##### Samples

```JSON
{
  "bar_version": "2",
  "box_version": "1",
  "default_path": "box1",
  "schema": "http://app-cell1.unit1.example"
}
```

#### 10\_relations.json

The file describing the information of the relations to be installed<br>\* For items whose "Effective Value" column shows "-", refer to the Relation request body

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Relations|Relation list||Yes||
|Relations/Name|Relation name|-|Yes||

##### Samples

```JSON
{
  "Relations": [
    {
      "Name": "relation1"
    }
  ]
}
```

#### 20\_roles.json

The file describing the information of the roles to be installed<br>\* For items whose "Effective Value" column shows "-", refer to the Role request body

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Roles|Role list||Yes||
|Roles/Name|Role name|-|Yes||

##### Samples

```JSON
{
  "Roles": [
    {
      "Name": "role1"
    }
  ]
}
```

#### 30\_extroles.json

The file describing the information of the ExtRoles to be installed<br>\* For items whose "Effective Value" column shows "-", refer to the ExtRole request body

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|ExtRoles|ExtRole list||Yes||
|ExtRoles/ExtRole|Reference destination role URI|-|Yes|null is invalid *1|
|ExtRoles/_Relation.Name|Relation name|-|Yes|null is invalid|

(*1) Converted to the role class URL during export  
https&#58;//{UnitFQDN}/cell1/__role/box/staff → https&#58;//{UnitFQDN}/cell1/__role/__/staff  

##### Samples

```JSON
{
  "ExtRoles": [
    {
      "ExtRole": "https://cell1.unit1.example/__role/__/role2",
      "_Relation.Name": "Relation1"
    }
  ]
}
```
#### 50_rules.json
The file described thr Rule information for install.
* For items whose "valid value" column is "-", refer to the request body of Rule

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Rules|Rules list||Yes||
|Rules/EventExternal| External event flag of matching event|-|No||
|Rules/EventSubject|Subject of matching event|-|No||
|Rules/EventType|Type of event to match|-|No||
|Rules/EventObject|Object of matching event|-|No||
|Rules/EventInfo|Information on matching events|-|No||
|Rules/Action|Action when matching an event|-|Yes||
|Rules/TargetUrl|Url to be processed for action|-|No||

##### Samples

```JSON
{
  "Rules": [
    {
      "Action": "exec",
      "TargetUrl": "personium-localbox:/col/srv"
    }
  ]
}
```

#### 70\_$links.json

The file describing the data relation information of the $links to be installed

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Links|$links list||Yes||
|Links/FromType|Reference source data type|"Relation"<br>"Role"<br>"ExtRole"|Yes|null is invalid|
|Links/FromName|Reference source data name|- (Array format *1)|Yes|null is invalid<br> (Example: {"Name":"relation1"}])|
|Links/ToType|Reference destination data type|"Relation"<br>"Role"<br>"ExtRole"|Yes|null is invalid|
|Links/ToName|Reference destination data name|- (Array format *1)|Yes|null is invalid<br> (Example: {"Name":"role"}])|

\*1 The list format is applied for ExtRoles because relation information is also required. However, the key name of the specified JSON data is fixed to "Name". (Restriction)

##### Samples

```JSON
{
  "Links": [
    {
      "FromType": "Relation",
      "FromName":
        {
          "Name": "relation1"
        },
      "ToType": "Role",
      "ToName":
        {
          "Name": "role1"
        }
    },
    {
      "FromType": "Role",
      "FromName":
        {
          "Name": "role1"
        },
      "ToType": "ExtRole",
      "ToName": {
          "ExtRole": "https://cell1.unit1.example/__role/__/role2",
          "_Relation.Name": "Relation1"
        }
    }
  ]
}
```

#### 90\_rootprops.xml

Shows the XML data acquired with the PROPFIND method for all hierarchical levels under the box to be export to the bar file. <br>For details on XML data, refer to [get file setting API(PROPFIND)](307_Get_Property.md). <br>The URL of the box to be installed is described as "personium-localbox:/". <br>When the bar file is installed, the installation targets include all data excluding creationdate and astmodified under the following sample.

* resourcetype: Sets the collection type
* acl: Sets privileges
* Other: Set in PROPPATCH

##### Samples

```xml
<multistatus xmlns="DAV:">
  <response>
    <href>personium-localbox:/</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
        </resourcetype>
         <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns">
          <ace>
            <principal>
              <href>admin</href>
            </principal>
            <grant>
              <privilege>
                <all/>
              </privilege>
            </grant>
          </ace>
        </acl>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/odata</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
          <p:service xmlns:p="urn:x-personium:xmlns"/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns">
          <ace>
            <principal>
              <href>user</href>
            </principal>
            <grant>
              <privilege>
                <read/>
              </privilege>
              <privilege>
                <write/>
              </privilege>
              <privilege>
                <read-properties/>
              </privilege>
            </grant>
          </ace>
        </acl>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/dav</href>
    <propstat>
      <prop>
        <resourcetype>
                  <collection/>
        </resourcetype>
         <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns">
          <ace>
            <principal>
              <href>user</href>
            </principal>
            <grant>
              <privilege>
                <read/>
              </privilege>
              <privilege>
                <write/>
              </privilege>
              <privilege>
                <read-properties/>
              </privilege>
            </grant>
          </ace>
        </acl>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/dav/testdavfile.txt</href>
    <propstat>
      <prop>
        <getcontenttype>text/plain</getcontenttype>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
          <p:service xmlns:p="urn:x-personium:xmlns"/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
        <p:service language="JavaScript" xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
          <p:path name="ehr" src="ehr.js"/>
          <p:path name="ehr_connector" src="ehr_connector.js"/>
        </p:service>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr_connector.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
</multistatus>
```

#### contents/{OData}/

Details not contributed yet for the following files

* 90_data / {EntityType}/1.json

##### 00\_$metadata.xml

Shows user OData schema definitions. This data is the XML data acquired by $metadata for the collection for Odata during the export to the bar file. <br>For details on XML data, refer to [schema acquisition ($metadata)](316_User_Defined_Data_Schema.md). <br>When the box is installed, the installation targets include the contents under the Schema tag. <br>Even if user OData schema definitions do not exist, the file itself exists.

Sample in the case of no schema definitions

```xml
<Edmx: Edmx Version = '1 .0 'xmlns: edmx =' http://schemas.microsoft.com/ado/2007/06/edmx \
'xmlns: d =' http://schemas.microsoft.com/ado/2007 / 08/dataservices' xmlns:\
 m = 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata' xmlns: p = 'urn: x-personium: xmlns'>
  <edmx:DataServices m:DataServiceVersion='1.0'>
  <Schema Xmlns='http://schemas.microsoft.com/ado/2006/04/edm' Namespace='UserData'>
      <EntityContainer Name='UserData' m:IsDefaultEntityContainer='true'/>
  </ Schema>
  </ Edmx: DataServices>
</ Edmx: Edmx>
```

##### 10\_odatarelations.json

The file describing the data-related information of $links of the user data to be installed<br>At the user OData schema level, AssociationEnd relations are defined in 00\_$metadata.xml, and in this file, relations to actual user data are defined.

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Links|$links list||Yes||
|Links/FromType|Reference source data type|-|Yes|null is invalid|
|Links/FromId|Reference source user data ID|- (Array format *1)|Yes|null is invalid<br> (Example: {"FromId":"fujitsu_taro"})|
|Links/ToType|Reference destination data type|-|Yes|null is invalid|
|Links/ToId|Reference destination user data ID|- (Array format *1)|Yes|null is invalid<br> (Example: {"ToId":"fujitsu_hanako"})|

\*1 The array format is applied in consideration of the future support for composite primary keys.

##### Samples

```JSON
{
  "Links": [
    {
      "FromType": "Keeper",
      "FromId": {
        "usercode": "001",
        "Name": "Peru_Taro"
      },
      "ToType": "Animal",
      "ToId": {
        "shopcode": "001",
        "Name": "pochi"
      }
    },
    {
      "FromType": "Keeper",
      "FromId": {
        "usercode": "002",
        "Name": "Peru_Hanako"
      },
      "ToType": "Animal",
      "ToId": {
        "shopcode": "002",
        "Name": "tama"
      }
    }
  ]
}
```

#### 90\_data / {EntityType} / {1.json}

Stores user data in the JSON format one by one.

```JSON
{
  "__id": "{EntityName}",
  "name": "pochi",
  "address": {
    "country": "japan",
    "city": "tokyo"
  }
}
```

#### contents / {webdavbcol} /

\* Not contributed yet

#### contents/Service/{src.js}

Registers the source file stored in bar/90\_contents/{Service}/{src.js} with {Service}/\_\_src/{src.js} under the installation destination box.

* Unable to be executed as a service if no collection {Service} definitions (PROPPATCH) exist in bar/00_meta/90_rootprops.xml
* {src.js} cannot be registered if no {Service}/__src definitions exist in bar/00_meta/90_rootprops.xml
* Content-Type in {src.js} to be set according to the {Service}/__src/{src.js} definition in bar/00_meta/90_rootprops.xml

Sample of 90\_rootprops.xml for service registration

```xml
<multistatus xmlns="DAV:">
  <response>
    <href>personium-localbox:/service</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
          <p:service xmlns:p="urn:x-personium:xmlns"/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
        <p:service language="JavaScript" xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
          <p:path name="ehr" src="ehr.js"/>
          <p:path name="ehr_connector" src="ehr_connector.js"/>
        </p:service>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr_connector.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
</multistatus>
```
