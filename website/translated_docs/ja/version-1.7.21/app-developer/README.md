---
id: version-1.7.21-README
title: アプリ開発者向けガイド
sidebar_label: アプリ開発者向けガイド
---

PersoniumのAPIを使用して、アプリを開発する人のためのドキュメントです。

## アプリ開発の入門

アプリ開発の基本を学ぶためにはGetting Startedの以下ドキュメントを参照してください。

1. [はじめに](../getting-stared/appdev-introduction.md)
2. [管理ツール (Unit Manager)](../getting-stared/appdev-management-tool.md)
3. [アプリ開発の流れ](../getting-stared/appdev-process.md)
4. [アプリの実装](../getting-stared/appdev-impl.md)

### OData, WebDAVのデモ

Personiumのデータ操作はOData, WebDAVによって行います。仕様を理解するためにOData, WebDAVのデモを体験することを推奨します。

[OData,WebDAVのデモ](https://baas-demo.demo-jp.personium.io/1/index.html)

## アプリ開発の詳細

アプリ開発の詳細はトピックごとに分かれています。

- 認可
  - [認可モデル](../app-developer/003_Auth.md)
  - [Personiumにおけるロール](./Roles.md)
  - [アクセス制御モデル](../apiref/006_Access_Control.md)
  - [アプリ認証](./app_authn.md)
  - [Single Sign On](./launch_from_homeapp.md)
- Box/barファイル
  - [Boxインストール](../apiref/007_Box_install.md)
  - [barファイル](../apiref/301_Bar_File.md)
- コレクション
  - [WebDAV](../app-developer/007_WebDAV_model.md)
  - [OData](./using_odata.md)
  - [Personium Engine](./Personium-Engine.md)
  - [Engine Script のサンプル](./671_Engine_Script_Samples.md)
- [Cell GUI開発者向けガイド](../cell-gui-developer/README.md)

## サンプルアプリ

Webブラウザ向けのJavaScriptアプリとしてのサンプルアプリがいくつか公開されています。

Getting Startedの[サンプルアプリの構築](../getting-started/setup-sample-apps.md)を参照してください。
