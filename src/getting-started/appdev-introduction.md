---
id: appdev-introduction
title: Develop an app
sidebar_label: Introduction
---

In this chapter, we will explain how to develop an application using Personium API through the flow of sample application development.

## Sample app development

Sample application (Personium Trails) is to store the movement history data accumulated on Google in Personium and share a part of the data with others. The type of application is a web application that runs on a browser.

Below is a screenshot of the completed sample app.

![Movement history data list](assets/getting-started/trails_locations_public.png)

The code of the completed sample app can be found at the link below.

[app-personium-trails](https://github.com/personium/app-personium-trails)

## Prior knowledge

It is assumed that you have the following prior knowledge.

* Basic web application development
* Front-end development (Html, JavaScript, CSS)
* REST API

## Advance preparation

In the sample application, 2 Cell creation and Account, Role, ACL settings related to Cell are done in advance. When developing an app that uses Personium, do the same thing. Refer to [Previous Chapter Tutorial](../unit-administrator/tutorial.md) for the setting method related to cell creation.

The usage and details of the two cells in the sample app are shown in the table below.

|Use|Cell name|Account name|Role name linked to Account|Role permission settings|
|----|---|---------|-----------------------|--------------|
|Data subject Cell|alice.example|me|admin|root|
|App Cell|app-personium-trails.example|app|admin|root|

When developing your own application, the names of each Cell, Account, and Role do not have to be as shown in the table because they are arbitrary.
