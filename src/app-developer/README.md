---
id: README
title: Application Developer's Guide
sidebar_label: Application Developer's Guide
---

## App development



## App種類

- Server side app
- Client side app
- Desktop app
- Native app

## Box

アプリはBoxとやり取りを行うので、Boxを使う。

## As WEB and API Server

Cellは基本ユーザー。アプリ用のCellを用意することで、Webサーバ・APIサーバとして使える。

Webサーバ・APIサーバとしてのアプリCellは必須ではなく、別サーバの使用も可能。

## Client side app

アプリの例。

```
user -----> WEB Server
app ------> UserCell data
app ------> API Server -----> UserCell data
app ------> API Server -----> DB
```

アプリ用のCellを使う場合。

```
user -----> AppCell data
app ------> UserCell (EngineScript) --> UserCell Data
app ------> AppCell
app ------> AppCell (EngineScript) --> AppCell Data
```

## 構成

- 認証認可
  - 全体像
  - Role/ACL詳細
  - アプリ認証詳細
  - Single Sign On
- Box
  - 概要
  - BarファイルとBoxインストール
- コレクション
  - WebDAV
  - OData
  - EngineScript
  - Stream
- CellGUIカスタマイズ

## サンプルアプリ

## 開発者ツール

UnitManager
