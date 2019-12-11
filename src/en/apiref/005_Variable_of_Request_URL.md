# Variable list of request URL
## Overview
Descriptions of the variables used in the API reference request URL

## Variable list

| Variable name | Overview | Remarks |
|:-|:-|:-|
| {UnitURL} |URL for accessing Unit|URL:https&#58;//{UnitFQDN}/|
| {UnitFQDN} | FQDN of server running Personium <br> Unit refers to server hosting multiple cells ||
| {CellName} | Cell name <br> Cell refers to Data Strore for each data subject ||
| {CellURL} |URL for accessing Cell<br>CellURL has two kinds of "path based cell URL" and "per cell FQDN URL", and it can be switched by [property](../../server-operator/unit_config_list.md)(pathBasedCellUrl.enabled)|path based cell URL:https&#58;//{UnitFQDN}/{CellName}/<br>per cell FQDN URL:https&#58;//{CellName}.{UnitFQDN}/|
| {BoxName} | Box name <br> Box refers to the area where data used for application is stored ||
| {SchemaURL} | Schema URL <br> Schema refers to Schema stored in Personium ||
| {RoleName} | Role name <br> Role refers to a valid "role" defined for Cell ||
| {AccountName} | Account name <br> Account represents user authentication means in Cell ||
| {ExtCellURL} | URL of ExtCell <br> ExtCell (external cell) refers to other Cell outside when viewed from a Cell ||
| {RelationName} | Relation name <br> Relation refers to the relationship between itself (own cell) and others (external Cell) ||
| {ExtRoleURL} | URL of ExtRole <br> ExtRole (external Role) refers to a user entity given a specific role (Role) in an external Cell group in a specific relationship ||
| {LogName} | Log file name ||
| {MessageID} | ID of Message <br> Message indicates a message that can be transmitted and received between cells ||
| {CollectionName} | Collection name <br> Collection is equivalent to a folder / directory in a regular file system ||
| {ResourcePath} | Path to Resource <br> Collection and files under Box are targeted ||
| {OdataCollectionName} | OdataCollection name <br> OdataCollection refers to a special WebDAV extension collection for users to handle arbitrary relational data with the OData protocol ||
| {EntityTypeName} | EntityType name <br> EntityType refers to a definition field for representing the structure of data by EntityDataModel (EDM) | Entity's superordinate concept |
| {AssociationEndName} | AssociationEnd name <br> AssociationEnd refers to the EntityType that is the endpoint that constitutes the Association ||
| {ComplexTypeName} | ComplexType name <br> ComplexType is a property with an attribute with subordinate attribute | Superordinate concept of ComplexTypeProperty |
| {PropertyName} | Property name <br> Points to the column head value of each EntityType, corresponding to the table item name in RDB ||
| {ComplexTypePropertyName} | ComplexTypeProperty name <br> ComplexTypeProperty is the name of the subordinate attribute of ComplexType | Subordinate attribute of ComplexType |
| {EntityName} | Entity name <br> Entity refers to the data recording structure, and | EntityType subordinate attribute corresponding to one table row in RDB |
| {EntityID} | ID of Entity ||
| {NavigationPropertyName} | NavigationProperty name <br> NavigationProperty refers to a Property representing the navigation from one end of Association to another in the data structure of EntityDataModel or OData ||
| {ServiceSourceName} | ServiceSource name <br> Service refers to user defined server side logic registered in ServiceCollection ||
| {ServiceName} | Service name | ServiceSource name to be used when executing the service minus the extension |
