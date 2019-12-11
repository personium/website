# Personium API Reference
Welcome to the Personium API Reference.  This reference describes technical detailed specifications related to all of the APIs provided by Personium.
Please refer to [Request URL variable list](005_Variable_of_Request_URL.md) for the variable of the request URL in this reference.

## Unit Level API
The Unit Level API's belong to the unit that hosts a group of cells and provide functions such as creating cells or managing a group of created cells. In principle, Unit Level API's cannot be accessed using the access tokens issued by normal cells and can only be accessed with Unit User Tokens.

#### Unit Root URL

```
https://{UnitFQDN}/
```

#### Unit Control Objects
Most of the Unit Level API's are implemented in the form of Unit Control Objects.
Since they conform with the OData standard, their manipulation can be made in
a RESTful and standardized manner.

|Cell|Operations|
|:--|:--|
|Basic Operations|[Create](100_Create_Cell.md) &nbsp; &nbsp; [Retrieve List](101_List_Cell.md) &nbsp; &nbsp; [Retrieve](102_Retrieve_Cell.md) &nbsp; &nbsp; [Update](103_Update_Cell.md) &nbsp; &nbsp; [Delete](104_Delete_Cell.md)|

#### Other API's

*  [Get Unit Metadata](107_Get_Unit_Metadata.md)
*  [Cell Recursive Deletion](105_Cell_Recursive_Delete.md)

## Cell Level API

Cell Level API's are deployed under the following root URL.

#### Cell Root URL
```
{CellURL}
```

Cell Level API's provides the following features:

*  User and application Authentication
*  Access control
*  Networking Cells
*  Box creation and management
*  Message exchange between Cells
*  Event processing
*  Other features

Most of these functions are implemented in the form of Cell Control Objects that can be operated with the OData protocol, which is a standard for performing relational data manipulation based on REST.


### User and application Authentication

#### Authentication

* [OAuth2.0 Authorization Endpoint](292_OAuth2_Authorization_Endpoint.md)
* [OAuth2.0 Token Endpoint](293_OAuth2_Token_Endpoint.md)
* [Change Password](294_Password_Change.md)
* [OAuth2.0 Token Introspection](297_OAtuh2_Token_Introspection_Endpoint.md)
* [Get Cell Certs](298_Get_Cell_Certs.md)

#### Account (Cell Control Object)

|Account|Operations|
|:--|:--|
|Basic Operations|[Create](212_Create_Account.md) &nbsp; &nbsp; [Retrieve](213_Retrieve_Account.md) &nbsp; &nbsp; [Retrieve List](214_List_Account.md) &nbsp; &nbsp; [Update](215_Update_Account.md) &nbsp; &nbsp; [Partial Update](2AC_Partial_Update_Account.md) &nbsp; &nbsp; [Delete](216_Delete_Account.md)|
|&nbsp; &nbsp; Linking with other objects|[Link](217_Link_Account.md) &nbsp; &nbsp; [Unlink](220_Unlink_Account.md) &nbsp; &nbsp; [List Links](218_List_Account_links.md) <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](221_Create_Obj_Via_Account_NP.md) &nbsp; &nbsp; [Retrieve List](222_List_Obj_Via_Account_NP.md)|

### Access control

Personium Cells employ Role-Based Access Control. A role can be defined in the form of Cell Control Object "Role".
Cell-level ACL can be configured with the following API, where multiple pairs of role and granted privileges can be defined.

* [Cell-level ACL Configuralion](289_Cell_ACL.md)

Configured ACL can be retrieved together with other properties, by sending regular WebDAV PROPFIND request to the root URL of the Cell.

* [Retrieve Properties](290_Cell_Get_Property.md)
* [Change Properties](291_Cell_Change_Property.md)


#### Cell Control Object

|Role|Operations|
|:--|:--|
|Basic Operations|[Create](201_Create_Role.md) &nbsp; &nbsp; [Retrieve](203_Retrieve_Role.md) &nbsp; &nbsp; [Retrieve List](202_List_Role.md) &nbsp; &nbsp; [Update](204_Update_Role.md) &nbsp; &nbsp; [Partial Update](2AB_Partial_Update_Role.md) &nbsp; &nbsp; [Delete](205_Delete_Role.md)|
|&nbsp; &nbsp; Linking with other objects|[Link](206_Link_Role.md) &nbsp; &nbsp; [Unlink](209_Unlink_Role.md) &nbsp; &nbsp; [List Links](207_List_Role_links.md) <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](210_Create_Obj_Via_Role_NP.md) &nbsp; &nbsp; [Retrieve List](211_List_Obj_Via_Role_NP.md)|


### Networking Cells

#### External Cell (Cell Control Object)

|ExtCell|Operations|
|:--|:--|
|Basic Operations|[Create](223_Create_External_Cell.md) &nbsp; &nbsp; [Retrieve](225_Retrieve_External_Cell.md) &nbsp; &nbsp; [Retrieve List](224_List_External_Cell.md) &nbsp; &nbsp; [Update](226_Update_External_Cell.md) &nbsp; &nbsp; [Partial Update](2AD_Partial_Update_External_Cell.md) &nbsp; &nbsp; [Delete](227_Delete_External_Cell.md)|
|&nbsp; &nbsp; Linking with other objects|[Link](228_Link_External_Cell.md) &nbsp; &nbsp; [Unlink](231_Unlink_External_Cell.md) &nbsp; &nbsp; [List Links](229_List_External_Cell_links.md) <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](232_Create_Obj_Via_External_Cell_NP.md) &nbsp; &nbsp; [Retrieve List](233_List_Obj_Via_External_Cell_NP.md)|

#### Relation (Cell Control Object)

|Relation|Operations|
|:--|:--|
|Basic Operations|[Create](234_Create_Relation.md) &nbsp; &nbsp; [Retrieve](236_Retrieve_Relation.md) &nbsp; &nbsp; [Retrieve List](235_List_Relation.md) &nbsp; &nbsp; [Update](237_Update_Relation.md) &nbsp; &nbsp; [Partial Update](2AE_Partial_Update_Relation.md) &nbsp; &nbsp; [Delete](238_Delete_Relation.md)|
|&nbsp; &nbsp; Linking with other objects|[Link](239_Link_Relation.md) &nbsp; &nbsp; [Unlink](242_Unlink_Relation.md) &nbsp; &nbsp; [List Links](240_List_Relation_links.md) <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](243_Create_Obj_Via_Relation_NP.md) &nbsp; &nbsp; [Retrieve List](244_List_Obj_Via_Relation_NP.md)|


#### ExtRole (Cell Control Object)

|ExtRole|Operations|
|:--|:--|
|Basic Operations|[Create](245_Create_External_Role.md) &nbsp; &nbsp; [Retrieve](247_Retrieve_External_Role.md) &nbsp; &nbsp; [Retrieve List](246_List_External_Role.md) &nbsp; &nbsp; [Update](248_Update_External_Role.md) &nbsp; &nbsp; [Partial Update](2AF_Partial_Update_External_Role.md) &nbsp; &nbsp; [Delete](249_Delete_External_Role.md)|
|&nbsp; &nbsp; Linking with other objects|[Link](250_Link_External_Role.md) &nbsp; &nbsp; [Unlink](253_Unlink_External_Role.md) &nbsp; &nbsp; [List Links](251_List_External_Role_links.md) <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](254_Create_Obj_Via_External_Role_NP.md) &nbsp; &nbsp; [Retrieve List](255_List_Obj_Via_External_Role_NP.md)|

### Box creation and management inside the Cell

* [Export Box](385_Box_Export.md)
* [Install Box](302_Box_Installation.md)
* [Retrieve Box Meta Data](303_Progress_of_Bar_File_Installation.md)
* [Retrieve URL](304_Get_Box_URL.md)
* [Recursive Delete](295_Box_Recursive_Delete.md)

#### Box (Cell Control Object)

|Box|Operations|
|:--|:--|
|Basic Operations|[Create](256_Create_Box.md) &nbsp; &nbsp; [Retrieve](258_Retrieve_Box.md) &nbsp; &nbsp; [Retrieve List](257_List_Box.md) &nbsp; &nbsp; [Update](259_Update_Box.md) &nbsp; &nbsp; [Partial Update](2B0_Partial_Update_Box.md) &nbsp; &nbsp; [Delete](260_Delete_Box.md)|
|&nbsp; &nbsp; Linking with other objects|[Link](261_Link_Box.md) &nbsp; &nbsp; [Unlink](264_Unlink_Box.md) &nbsp; &nbsp; [List Links](262_List_Box_links.md) <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](265_Create_Obj_Via_Box_NP.md) &nbsp; &nbsp; [Retrieve List](266_List_Obj_Via_Box_NP.md)|

### Message Exchange between Cells

#### Message Manipulation

* [Send Message](271_Send_Message.md)
* [Change Status](267_Received_Message_Approval.md) (Approve / Decline, etc.)

|Cell Control Object|Operations|
|:--|:--|
|**Sent Message**|[Retrieve](272_Retrieve_Sent_Message.md) &nbsp; &nbsp; [Retrieve List](273_List_Sent_Messages.md) &nbsp; &nbsp; [Delete](274_Delete_Sent_Message.md)|
|**Received Message**|[Retrieve](269_Retrieve_Received_Message.md) &nbsp; &nbsp; [Retrieve List](268_List_Received_Messages.md) &nbsp; &nbsp; [Delete](270_Delete_Received_Message.md)|

### Event processing

* [Events Overview](277_Event_Summary.md)
* [Accept External Events](278_Event_Reception.md)
* [Web Socket connection to Event Bus](279_Event_Bus_Connect.md)

#### Event Processing Rule (Cell Control Object)

|Rule|Operations|
|:--|:--|
|Basic Operations|[Create](2A0_Create_Rule.md) &nbsp; &nbsp; [Retrieve](2A1_Retrieve_Rule.md) &nbsp; &nbsp; [Retrieve List](2A2_List_Rule.md) &nbsp; &nbsp; [Update](2A3_Update_Rule.md) &nbsp; &nbsp; [Delete](2A4_Delete_Rule.md) |
|&nbsp; &nbsp; Linking with other objects|[Link](2A5_Link_Rule.md) &nbsp; &nbsp; [Unlink](2A7_Unlink_Rule.md) &nbsp; &nbsp; [List Links](2A6_List_Rule_links.md) &nbsp; &nbsp; <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](2A8_Create_Obj_Via_Rule_NP.md) &nbsp; &nbsp; [Retrieve List](2A9_List_Obj_Via_Rule_NP.md)|

* [Retrieve List of Internal Rule information](2AA_List_Internal_Rule.md)

#### Event Log

* [Retrieve Log File](285_Retrieve_Log_File.md)
* [List of Log Files](284_Retrieve_Log_File_list.md)
* [Retrieve Log File Information](283_Log_File_Information_Acquisition.md)
* [Delete Log File](286_Delete_Log_File.md)

### Other functions
#### Cell root access

* [Retrieve Cell Root](./200_Cell_Root.md)
* [Retrieve Cell Metadata](./296_Get_Cell_Metadata.md)

#### Exporting / Importing the contents inside the Cell

Snapshot file of Cell is created by export execution.  
Import imports the contents of the snapshot file into Cell.  
Snapshot file can be operated with WebDAV interface.  

||Operations|
|:--|:--|
|**Export**|[Execute](501_Export_Cell.md) &nbsp; &nbsp; [Retrieve progress](502_Progress_of_Export_Cell.md)|
|**Import**|[Execute](507_Import_Cell.md) &nbsp; &nbsp; [Retrieve progress](508_Progress_of_Import_Cell.md)|
|**Snapshot**|[Create/Update](503_Register_and_Update_Snapshot_Cell.md) &nbsp; &nbsp; [Retrieve](504_Get_Snapshot_Cell.md) &nbsp; &nbsp; [Retrieve Properties](505_Get_Property_Snapshot_Cell.md) &nbsp; &nbsp; [Delete](506_Delete_Snapshot_Cell.md)|

## Box Level API

The Box Level API is a group of API's that reside on the following Box Root URL and serve for applications and others to manipulate their data.

#### Box Root URL

```
{CellURL}{BoxName}/
```

Box Level API's are based on an idea of WebDAV file system.  Like ordinary file systems, it is possible to arrange / retrieve files, create / manage folders (collection), get list of files and folders, set / refer to access control, etc.

Also, because it supports the following special collections, it can handle not only file-like data but also various forms of data.  
These special collections can be created in any path on the WebDAV space provided by Box.

|Special collection|Use|Notes|
|:--|:--|:--|
|OData Service Collection|Relational data||
|Engine Service Collection|Run customized logic||
|CALDAV Collection|Calendar data|Unimplemented|
|Link Collection|Aliases to specific areas of other cells or other Box|Unimplemented|



### Basic WebDAV Operations

|Target|Operations|
|:--|:--|
|Collection|[Create](306_Create_Collection.md) &nbsp; &nbsp; [Retrieve Settings](305_Get_Property.md) &nbsp; &nbsp; [Change Settings](308_Change_Property.md) &nbsp; &nbsp; [Move/Rename](309_Update_Move_Collection.md) &nbsp; &nbsp; [Delete](310_Delete_Collection.md)|
|File|[Create/Update](312_Register_and_Update_WebDAV.md) &nbsp; &nbsp; [Retrieve](311_Get_WebDav.md) &nbsp; &nbsp; [Retrieve Settings](307_Get_Property.md) &nbsp; &nbsp; [Change Settings](313_Change_Property.md) &nbsp; &nbsp; [Delete](314_Delete_WebDAV.md)|
|Common|[Configure Access Control](315_Configure_Access_Control.md)|

\* ACL setting (access control setting) is possible for all files and collections (including special collections).  
\* ACL setting can be acquired with the PROPFIND method.

### OData Service Collection

#### Viewing Schema

||Operations|
|:--|:--|
|Schema Retrieval|[ATOM Service Document](317_Document_Acquisition_Service.md) &nbsp; &nbsp; [EDMX Schema](316_User_Defined_Data_Schema.md)|


#### Schema Definition

||Create|Retrieve|Update|Delete|Other|
|:--|:--|:--|:--|:--|:--|
|**EntityType**|[Create](345_Create_EntityType.md)|[Retrieve](347_Retrieve_EntityType.md)<br>[Retrieve List](346_List_EntityType.md)|[Update](348_Update_EntityType.md)|[Delete](349_Delete_EntityType.md)||
|_$links|Create|List|Update|Delete||
|_via NavProp||List||||
|**Property**|[Create](355_Create_Property.md)|[Retrieve](357_Retrieve_Property.md)<br>[Retrieve List](356_List_Property.md)|Update|[Delete](359_Delete_Property.md)||
|_$links|Create|List|Update|Delete||
|**AssociationEnd**|[Create](318_Create_AssociationEnd.md)|[Retrieve](320_Retrieve_AssociationEnd.md)<br>[Retrieve List](319_List_AssociationEnd.md)|[Update](321_Update_AssociationEnd.md)|[Delete](322_Delete_AssociationEnd.md)||
|_$links|[Create](323_Link_AssociationEnd.md)|[List Links](324_List_AssociationEnd_links.md)||[Delete](325_Unlink_AssociationEnd.md)||
|_via NavProp||List||||
|**ComplexType**|[Create](327_Create_ComplexType.md)|[Retrieve](329_Retrieve_ComplexType.md)<br>[Retrieve List](328_List_ComplexType.md)|Update|[Delete](331_Delete_ComplexType.md)||
|_$links|Create|List|Update|Delete||
|**ComplexTypeProperty**|[Create](336_Create_ComplexTypeProperty.md)|[Retrieve](338_Retrieve_ComplexTypeProperty.md)<br>[Retrieve List](337_List_ComplexTypeProperty.md)|[Update](339_Update_ComplexTypeProperty.md)|[Delete](340_Delete_ComplexTypeProperty.md)||
|_$links|Create|List|Update|Delete||


#### Data Manipulation

|User-defined Entity Set|Operations|
|:--|:--|
|Basic Operations|[Create](364_Create_Entity.md) &nbsp; &nbsp; [Retrieve](366_Retrieve_Entity.md) &nbsp; &nbsp; [Retrieve List](365_List_Entity.md) &nbsp; &nbsp; [Update](367_Update_Entity.md) &nbsp; &nbsp; [Partial Update](369_Partial_Update_Entity.md) &nbsp; &nbsp; [Delete](370_Delete_Entity.md) |
|&nbsp; &nbsp; Linking with other objects|[Link](373_Link_User_Data.md) &nbsp; &nbsp; [Unlink](376_Unlink_User_Data.md) &nbsp; &nbsp; [List Links](374_List_User_Data_links.md) &nbsp; &nbsp; <br> There is no link update. If you want to update, delete it and recreate it.|
|&nbsp; &nbsp; Bound Object Manipulation|[Create](377_Create_Entity_Via_NP.md) &nbsp; &nbsp; [Retrieve List](378_List_Entity_Via_NP.md)|

* [Batch Operation](368_Entity_Bulk_Operations.md)


### Engine Service Collection
Personium applications and Cell users can create server-side logics and run them on each Cell. It is enabled with a special collection called Engine Service Collection (ESC). Each ESC has its source directory where user logic can be registered as script files. After script files are registered in the directory and the routing from any paths under ESC to the registered script files can be configured, HTTP request to the configured path will be handled with the registered script.

||Operations|
|:--|:--|
|Script files|[Create](381_Create_Service_Collection_Source.md) &nbsp; &nbsp; [Retrieve](382_List_Service_Collection_Source.md)  &nbsp; &nbsp; [Delete](383_Delete_Service_Collection_Source.md)|
|Configure / Execute|[Apply Settings](380_Configure_Service_Collection.md)  &nbsp; &nbsp; [Execute Service](384_Service_Execution.md)|

### Stream Collection
A collection that allows you to send and receive messages. By setting the queue and topic used for sending and receiving message queues, It is possible to send and receive for the set queue and send for the topic. Reception of topic is possible by WebSocket connection.

||Operation|Send/Receive|
|:--|:--|:--|
|Stream Collection|[Change settings](386_Configure_Stream_Collection.md) &nbsp; &nbsp; [OPTIONS](390_Options_Stream_Collection.md)|[Send](387_Stream_Collection_Send.md) &nbsp; &nbsp; [Receive](388_Stream_Collection_Receive.md) &nbsp; &nbsp; [WebSocket connection](389_Stream_Collection_Connect.md)|

## Common Information

### OData Acquisition Common Queries

|Query|Single Acquisition|List Acquisition|
|:--|:--|:--|
|[$format Query](404_Format_Query.md)|Yes|Yes|
|[$expand Query](405_Expand_Query.md)|Yes|Yes|
|[$select Query](406_Select_Query.md)|Yes|Yes|
|[$orderby Query](400_Orderby_Query.md)|No|Yes|
|[$top Query](401_Top_Query.md)|No|Yes|
|[$skip Query](402_Skip_Query.md)|No|Yes|
|[$filter Query](403_Filter_Query.md)|No|Yes|
|[$inlinecount](407_Inlinecount_Query.md)|No|Yes|
|[Full-text Search (q) Query](408_Full_Text_Search_Query.md)|No|Yes|

#### [Error Messages](004_Error_Messages.md)

#### [Restrictions on Personium HTTP Implementation](003_Common_Limitations_on_HTTP_Implementation.md)

#### [CORS Support](002_CORS_Support.md)

#### [Retrieve Cross Domain Policy File](001_Cross_Domain_Policy_File.md)
