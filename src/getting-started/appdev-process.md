---
id: appdev-process
title: Flow of app development
sidebar_label: Flow of app development
---

This section describes the flow of app development.


## OAuth 2.0 authorization code flow

App that uses Personium gains access to scoped data in the data subject Cell by executing the REST APIs for Box. The data access authorization method follows the OAuth 2.0 specifications. There are various types of OAuth 2.0 flows. The sample app adopts the authorization code flow for the ecosystem where PDS and app operators are different.

Please refer to [Authorization model](../user_guide/003_Auth.md#app-authorization) for details about authorization code flow.

## Data subject and app Cells

When implementing with authorization code flow, use two types of Cell, data subject Cell and application Cell. These two types of cells are used as follows.

| Cell type | Description |
|----|----|
|Data Subject Cell | Data management and authorization of the corresponding data subject|
|App Cell|App authorization (OAuth 2.0) and storage/deployment of the corresponding app|

App Cell is used in the following authorization code flow operations.

* Client registration: done by creating the application Cell
* client_id: URL of the app Cell
* client_secret: Token received from authentication of the account in the app Cell

You can also host static website by storing files (HTML, JavaScript and CSS) in the app Cell by configuring public access. The sample app in this section is assumed to be hosted on the app Cell.

The following figure shows the relationship between the data subject and app Cells in the sample app.

![Cell Relation](assets/getting-started/cell_relation.png)

The scope of the app development includes both the data subject and app Cells.

## Box and bar file installation

The app needs to make sure that the same data structure is inside any data subject Cell's Box in order to perform the intended behavior. In Personium, before the user can start using the app, Box installation is required. Bar file is to be installed that defines the app-specific data structure of the box. Please refer to the following documents for details.

* [Box installation](../apiref/007_Box_install.md)
* [bar file](../apiref/301_Bar_File.md)

The app developments involving the data subject Cell are the construction of the Box's data structure and the output of the bar file.

## Template app

The Personium community offers templates and deployment tools for [React](https://reactjs.org/) based JavaScript apps.

[personium-blank-app](https://github.com/personium/personium-blank-app)

By using this tool, you can develop your original app by customizing the data subject and app Cell. The tool also simplifies development work such as building bar files and uploading them to the app Cell.

### Flow of initial construction

The procedures for setting up the environment are as follows.

1. clone personium-blank-app to local development environment
2. Construction of app Cell
   1. Editing the configuration file
   2. Deploy to application Cell (execute `npm run deploy`)
   3. ACL setting of file on application Cell
3. Construction of data subject Cell
   1. Build the bar file (run `npm build-bar`)
   2. Box installation in the development data-based Cell

Please refer to [personium-blank-app](https://github.com/personium/personium-blank-app) for the detailed procedure.

> [Unit Manager explained in the previous section](./appdev-management-tool.md) can be used to perform operations on the Cell such as ACL setting and Box installation.

## Application development flow

After building the template application, you can develop by repeating the following.

* Development on the development data-based Cell
  1. Creation of data structure on Box by Unit Manager
  2. App operation check
  3. Output of bar file by Unit Manager
  4. Commit the bar file to the code repository
* Development on App Cell
  1. File editing in local development environment (HTML/JavaScript/CSS etc.)
  2. Deploy to application Cell (execute `npm run deploy`)
  3. ACL setting of file on application Cell
  4. App operation check
  5. Commit the files on the application Cell to the code repository

> Instead of deploying to the application Cell, you can start the development Web server on the local development environment and check the operation. In that case, run `npm run debug`.

## Create Box data structure

Supplement to "Creating Data Structure on Box with Unit Manager" in the previous section.

Both file data (WebDAV) and relational data (OData) can be used with Personium. There are the following differences between the two.

| Data type | Searchability | ACL setting unit |
|--------|-----|------------|
|WebDAV|❌ Not searchable | ✅ Set per file/collection |
|OData|✅ Searchable by query | ❌ Set per collection |

Therefore, it is recommended to handle the data to be searched with OData and the detailed information data of the unit for ACL setting with WebDAV.

## Box data structure in sample application

For reference, Box data structure is described in the sample application.

### Entire collection

| Path | Type | Content |
|----|----|----|
|/locations/{YYYY}/{MMdd}/s_{start_time}.json|WebDAV|Accommodation Details|
|/locations/{YYYY}/{MMdd}/m_{start_time}.json|WebDAV|Move Details |
|/index/Stay|OData|Accommodation information for search|
|/index/Move|OData|Move information for search|

The movement history data obtained with the original Google Takeout is divided into moving/stay units, and the divided files are stored in WebDAV. When sharing data to others, do it for each WebDAV file. In addition, the data for searching is stored in OData.

### OData Entity Type (Stay)

|Name|Type|Contents|
|----|----|----|
|name|Edm.Int32|name|
|startTime|Edm.DateTime|Start Time|
|endTime|Edm.DateTime|End time|
|latitudeE7|Edm.Int32|Latitude*10^7|
|longitudeE7|Edm.Int32|Longitude*10^7|
|placeId|Edm.String|Place Id|

### OData Entity Type (Move)

|Name|Type|Contents|
|----|----|----|
|name|Edm.Int32|name|
|startTime|Edm.DateTime|Start Time|
|endTime|Edm.DateTime|End time|
|sLatitudeE7|Edm.Int32|Latitude to start moving*10^7|
|sLongitudeE7|Edm.Int32| Start longitude*10^7|
|eLatitudeE7|Edm.Int32|Latitude to move *10^7|
|eLongitudeE7|Edm.Int32| End longitude*10^7|
