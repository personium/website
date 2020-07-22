---
id: version-1.7.21-appdev-introduction
title: Develop an app
sidebar_label: Introduction
original_id: appdev-introduction
---

In this chapter, we will explain how to develop an app using Personium APIs through the flow of sample app development.

## Sample app development

This sample app (Personium Trails) is a web application that runs on a browser. It allows the user to store the location history data accumulated from Google onto Personium and share selected data with third parties.

Below is a screenshot of the sample app.

![Movement history data list](assets/getting-started/trails_locations_public.png)

The source code of the sample app is available on GitHub ([app-personium-trails](https://github.com/personium/app-personium-trails)).


## Prior knowledge

The following knowledges are required before you continue reading.

* Basic web application development
* Front-end development (Html, JavaScript, CSS)
* REST API

## Advance preparation

In the sample app, the following operations are performed in advance.

* create two Cells  
* configure account, role and ACL settings in each Cell  

When developing an app that uses Personium, please perform the same operations. Refer to [Previous Chapter Tutorial](../unit-administrator/tutorial.md) for the APIs relevant to Cell creation.

The descriptions of the two cells used in the sample app are shown in the table below.

|Cell type|Cell name|Account name|Role name linked to Account|Role permission settings|
|----|---|---------|-----------------------|--------------|
|Data subject Cell|alice.example|me|admin|root|
|App Cell|app-personium-trails.example|app|admin|root|

When developing your own app, you do not have to use the same names as the sample's.
