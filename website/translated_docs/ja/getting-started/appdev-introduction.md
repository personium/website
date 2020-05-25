---
id: appdev-introduction
title: アプリを開発する
sidebar_label: はじめに
---

本章ではサンプルアプリの開発を通して、Personiumを使ったアプリ開発のやり方を学びます。

## サンプルアプリの開発

開発するサンプルアプリは自分の健康データをPersoniumに格納して、そのデーターの一部を特定の人に共有するもので、ブラウザ上で稼働するWebアプリケーションです。以下は完成したサンプルアプリのスクリーンショットとなります。

TODO: アプリのスクリーンショットを掲載

## 事前知識

以下の事前知識があることを想定しています。

* 基本的なWebアプリケーション開発
* フロントエンド開発 (Html, JavaScript, CSS)
* REST API

## 事前準備

Getting Startedを進める前に、2つのCellとCellに関連するAccount, Role, ACL設定を事前に準備してください。準備方法は[前章チュートリアル](../unit-administrator/tutorial.md)を参考にしてください。  

2つのCellの用途と詳細の設定は以下の表の通りとなります。それぞれのCell, Account, Roleの名前は任意なので表の通りでなくてもかまいません。

|用途|Cell例|Account例|AccountにリンクするRole例|RoleのACL設定|
|----|---|---------|-----------------------|--------------|
|ユーザー用Cell|user|me|admin|root|
|アプリ用Cell|sample-app|app|admin|root|

事前準備ができましたら、サンプルアプリ開発を始めましょう。
