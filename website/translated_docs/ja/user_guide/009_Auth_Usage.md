---
id: 009_Auth_Usage
title: 認証/認可の使い方
sidebar_label: 認証/認可の使い方
---

## ユースケース

- パスワードクレデンシャルを使ってアクセスする場合
  - 自分のCellにアクセス
  - 他者のCellにアクセス (トランスセルトークン)
  - 他者のCellにアクセス (トークンの交換)
- 認可コードフローを使ってアプリを通す場合
  - 自分のCellのBoxにアクセス
  - 他者のCellのBoxにアクセス
  - 自分のCellの他アプリのBoxにアクセス
  - SSOを実現する場合
- トークンをリフレッシュする場合
- Unit管理系トークンを使用する場合

## 具体的な使い方 (アプリを通さない場合)

### 自分Cellへのアクセス

### 他者のCellにアクセス (トランスセルトークン)

### 他者のCellにアクセス (トークンの交換)

## 具体的な使い方 (アプリを通す場合)

### 自分のCell全体にアクセス

ROPC

### 自分のCellのBoxにアクセス

Code flow

### 認可コードフロー+SSO

各アプリで認可コードフローを取った場合、各アプリごとにデータ主体のCell URLを入力し、認証することになります。このCell URLの入力と認証を1度で行い、SSOを実現することもできます。Personiumコミュニティで提供している[ホームアプリ](https://github.com/personium/app-cc-home)と、ホームアプリでの認証後に起動される[app-myboard](https://github.com/personium/app-myboard)はこれらを実現するサンプルアプリとなっています。

ホームアプリを経由した場合次のフローを取ります。

![Authorization Code Flow on home app](assets/auth/personium-authz-code-flow-home-app/personium-authz-code-flow.png)

### 他者のCellのBoxにアクセス

### 自分のCellの他アプリのBoxにアクセス

## 具体的な使い方 (Unit管理系トークンを使用する場合)
