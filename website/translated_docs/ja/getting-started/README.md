---
id: README
title: Getting Started
sidebar_label: はじめに
---

## はじめに

本ドキュメントはPersoniumを初めて使ってみる方を対象とした入門記事です。本ドキュメントを読むことで、Personiumの基本を理解し、使えるようにすることを目的としています。

## 前提知識

Personiumの共通となる前提知識として、[Personiumのアーキテクチャー](../user_guide/001_Personium_Architecture.md)を読んでいない場合、読むことを推奨します。

## 章構成

Getting Startedは大きく分けるとPersonium運用者向けの「1. Personiumの準備」の章とアプリ開発者向けの 「2. アプリ開発」の章から構成されています。各章の位置付けは以下の図の通りとなります。

![Getting Started 2 steps](assets/users-for-getting-started.png)

章構成の詳細は以下の通りとなります。

1. Personiumの準備 (Personium 運用者向け)
    1. [Personium Unitの構築](./setup-unit.md)
    2. [Personium Unitの管理](../unit-administrator/tutorial.md)
    3. [サンプルアプリの構築](./setup-sample-apps.md)
2. アプリ開発 (アプリ開発者向け)
    1. [はじめに](./appdev-introduction.md)
    2. [管理ツール (Unit Manager)](./appdev-management-tool.md)
    3. [アプリCellとユーザーCell上のBox](./appdev-appcell-and-box.md)
    4. [アプリテンプレート](./appdev-template.md)
    5. アプリの実装
        1. [認証・認可 (OAuth2 ROPCフロー)](./appdev-impl-auth.md)
        2. [ファイル (WebDAV)](./appdev-impl-webdav.md)
        3. [リレーショナルデータ (OData)](./appdev-impl-odata.md)
        4. [データ共有](./appdev-impl-data-shareing.md)
        5. [エンジンスクリプト](./appdev-impl-engine-script.md)
        6. [OAuth2 認可コードフロー](./appdev-impl-oauth2-code-flow.md)
    6. アプリの配布
        1. [Barファイル](./appdev-dist-bar.md)
        2. [スタンドアローンアプリ](./appdev-dist-stand-alone-app.md)
        3. [Single Sign Onアプリ](./appdev-dist-SSO-launch-app.md)

> もし構築済みのPersoniumを利用できる場合、「1. Personiumの準備」の章をスキップして「2. アプリ開発」の章から読むこともできます。

それではまずは[Personium Unitの構築](./setup-unit.md)から始めましょう。
