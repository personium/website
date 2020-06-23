---
id: README
title: Personium ドキュメント
sidebar_label: Personium ドキュメント
---

本ページでは様々な立場でPersoniumに関心を持っていただけた方に向けた様々なドキュメントを公開しています。  
ご不明な点がございましたら、[Slackコミュニティ](https://personium-io.slack.com/)までお問い合わせください。  
Slackコミュニティへの参加登録は[こちら](https://bit.ly/Join_Personium_Slack)からどうぞ。

## はじめに

* [Personiumとは](./overview/001_Introduction.md)
* [Personiumのアーキテクチャ](./user_guide/001_Personium_Architecture.md)
* [用語集](./user_guide/008_Glossary.md)

## Personiumのユーザー種類

Personiumのユーザーは大きく以下に分けられます。

|ユーザー種類|説明|
|-------------|----|
|Personium運用者|Personiumサーバの構築や運用管理|
|アプリ開発者|PersoniumのAPIを使用したアプリの開発|

以下の図はその関係を表しています。

![Personiumのユーザー種類](assets/personium-users.png)

## Getting Started

Personium運用者とアプリ開発者向けのPersonium入門ドキュメントを以下で提供しています。

* [Getting Started](./getting-started/README.md)

## ユーザガイド

Personiumのユーザー種類ごとのガイドおよびPersoniumプロジェクトへの貢献・参加方法のガイドを提供しています。

### Personium運用者向け

Personium運用者は更にサーバソフトウェア運用者とUnit管理者に分けられます。

#### [サーバソフトウェア運用者向けガイド](./server-operator/README.md)

Personiumのサーバソフトウェアを使ってPersonium Unitを構築する方や、Personiumサーバプログラムをビルド・デプロイ・設定する方、Personiumを使用したPDSサービス環境を提供・運用したい方向けのドキュメントです。

#### [Unit管理者向けガイド](./unit-administrator/README.md)

構築・設定済のPersonium Unitに対してUnitユーザトークンを使ってアクセスして、 Unit管理者の主たる業務、すなわちCellの作成・払出しや、払出したCellの管理等を実施する方のためのドキュメントです。

### アプリ開発者向け

#### [Personiumアプリ開発者向けガイド](./app-developer/README.md)

PersoniumのAPIを使用して、アプリを開発したい人向けのドキュメントです

## コントリビュータガイド

### ドキュメントコントリビュータ

#### [ドキュメント整備への参加方法](./document-writer/README.md)

Personiumプロジェクトの当ドキュメントの整備・改善を行いたい人向けのドキュメントです。

### コードコントリビュータ

#### [サーバ開発者向けガイド](./software-developer/README.md)

PersoniumのOSSの機能を開発したい人、OSSにコミットしたい人向けのドキュメントです。
