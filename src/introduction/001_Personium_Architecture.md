---
id: 001_Personium_Architecture
title: Personium Architecture  
sidebar_label: Personium Architecture  
---

## Basic three-layered objects
Personium defines the following three layered basic objects in order to achieve a new ICT model centered around data subjects.
![3LayerObject](assets/3LayerStructure.png "3LayerObject")  

|Name|Overview|URL example|
|:--|:--|:--|
|**Unit**|A server to host multiple Cells. What you get by server installation|https&#58;//personium.example/|
|**Cell**|A datastore for a data subject|https&#58;//john.personium.example/|
|**Box**|Per-app datastores installed on each Cell|https&#58;//john.personium.example/schedule/|

### Unit  
* A unit is a system infrastructure which runs Personium which have a unique FQDN.
* Since Personium adopts unique distributed architecture, it is possible to create a relationship between units and give privilege based on it.
* In a unit, it is possible to create multiple Cell.

### Cell  

* Cell is a data store for each data subject. For personal use, it will be PDS (Personal Data Store).
* In Personium, the concept of data subject is extended to not only people but also organizations and objects, so it can be used as a data store for a NGO or a car.
* Each Cells are independent as if they are different tenant in multi-tenancy model.
* A Cell provides following feature  
    * Authentication and authorization
    * Access Control
    * Data Store for Applications (Box)
    * Event Processing, Messaging, Script Execution


### Box  

* A box is data store for application.
* A box can store following data.  
    * Directory
    * File Object
    * OData Data Service

## Based on Open Standards  

Personium's API is build on open standards.  

* OAuth2.0 for Authorization
* WebDAV for File operation
* OData for relational data

![Personium specifications](assets/interface.png)
