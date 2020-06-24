---
id: appdev-process
title: アプリ開発の流れ
sidebar_label: アプリ開発の流れ
---

本節ではアプリ開発の流れについて説明します。

## データ主体CellとアプリCell

アプリ開発の流れ説明の前に、データ主体CellとアプリCellという2種類のCellについて説明します。

Personiumを使用したアプリの場合、アプリからのデータアクセスはデータ主体ごとのCellに対してREST APIを通じて行います。この時、アプリに対してのOAuthによるデータアクセスの認可を行う時、アプリ用のCellを使用します。OAuthにおけるクライアント登録は、PersoniumではアプリCellの作成になります。

また、必須ではありませんがアプリCell上にHTML, JavaScript, CSSといったファイルを格納し、アクセス設定を誰でも参照できるようにすることで、静的Websiteのホスティングを行えます。本節のJavaScriptによるサンプルアプリはアプリCell上でホスティングします。

データ主体CellとアプリCellの関係を表すと次の図の通りとなります。

![Cell Relation](assets/getting-started/cell_relation.png)

アプリの開発はデータ主体Cell部分とアプリCell部分に対して行います。

## テンプレートアプリ



## アプリ開発の流れ

1. 初期構築
    1. personium-blank-appのclone
    1. 設定ファイルの編集
    1. アプリCellの同期
    1. Barファイルのビルド
    1. 開発用データ主体CellへのBarインストール
1. アプリの開発
    1. Box上の開発
    1. アプリCell上の開発

## サンプルアプリでの開発

### personium-blank-appのclone


### 設定ファイルの編集


### アプリCellの同期


### Barファイルのビルド


### 開発用データ主体CellへのBarインストール


### Box上の開発


### アプリCell上の開発
