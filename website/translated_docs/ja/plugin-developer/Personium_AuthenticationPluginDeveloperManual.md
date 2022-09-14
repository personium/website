---
id: Personium_AuthenticationPluginDeveloperManual
title: Personium認証Plugin開発ガイド
sidebar_label: Personium認証Plugin開発ガイド
---

この文書はPersonium認証Pluginの開発マニュアルです。

## この文書について

Personiumの認証Pluginを開発する上で必要となる情報を記述しています。  
認証Pluginの詳細は[認証Pluginのセットアップ](../server-operator/setup_authentication_plugins.md)をご参照ください。  
このドキュメントでは、認証Pluginの作成手順を説明します。  

## 認証Pluginの概要

本章では、認証Pluginの概要を説明します。

### クラス構造

google版の認証Pluginを例に認証Pluginのクラス構造図を以下に示します。

![クラス構造図](assets/plugin_01.png "Pluginクラス構造図")

> **注意:**  認証処理の戻り値
> - 認証に成功した場合は、AuthenticatedIdentityが返却されます。
> - 認証に失敗した場合は、PluginExceptionまたはnullが返却されます。

### 動作概要

google版の認証Pluginを例に、認証PluginがPersoniumCoreApplicationによってどのようにロードされ認証プロセスが呼び出されるのかを示します。

![Pluginの動作](assets/plugin_02.png "pluginの動作")

1. Plugin初期化処理  
    PersoniumCoreApplicationクラスでPluginManagerが呼出され、すべてのPluginを読み込みます。  

2. 認証Pluginの選択  
    TokenEndPointResourceクラスで指定されたのGrantTypeのPluginを選択します。  

3. 認証プロセスの呼び出し  
    選択されたPluginのauthenticateメソッドを実行して認証処理を行います。

### 認証結果の取り扱い

認証Pluginのauthenticateメソッドは、TokenEndpointResourceから渡されたパラメタの評価を行い、認証されたアクセス主体を認証済み識別主体情報(AuthenticatedIdentityオブジェクト)として返却します。

PersoniumではAuthenticatedIdentityオブジェクトを以下の観点で評価して、トークン発行の可否判断や、発行トークンの内容決定、トークン発行処理を行います。

- getAccountName()で取得できる文字列をName属性にもつAccountが存在するか
- 存在する場合、getAccountType()で取得できる文字列が、ヒットしたAccountのAccountType値に含まれているか

### セキュリティ上の配慮

認証Plugin作者はTokenEndpointResourceから与えられたパラメタの評価において、アクセス主体が適切な認証プロセスを経るように実装を行う必要があります。  
例えば、入力値を一切チェックせずに本来保護されるべき特定の主体（ゲスト等でない実在の人物など）として認識してしまうような認証Pluginを作成し、これをUnitに配置してしまうことは重大なセキュリティ問題を引き起こします。  
従って認証Plugin作者はセキュアな実装を行うこと、認証Plugin利用者（Unit管理者）はセキュアであると信じられる認証Pluginのみを用いることが必要です。

## 開発の方法

Pluginでは以下の3点を定義します。

1. どのような`AccountType`値に対応すべきか
1. どのような`grant_type`値に対応すべきか
1. パラメタ値をどのように評価して、結果としてどのような主体として認識すべきか

上記3点の情報を決定したのち、`io.personium.plugin.base.auth.AuthPlugin`インタフェースを実装したクラスとして実装します。

### AuthPluginインタフェース

認証PluginはAuthPluginインタフェースを実装し、以下のメソッドを実装してください。

- getType()  
  PluginのTypeを返す。認証Pluginは`auth`を返す。
- getGrantType()  
  対応するgrant_type値を返す。
- getAccountType()  
  対応するAccountのType値を返す。
- authenticate()  
  認証処理を行う。認証結果はAuthenticatedIdentityオブジェクトとして返却する。

## パッケージング・配置

実装したクラスは以下の仕様に従ってjarファイルを作成し、[Unit設定](../server-operator/unit_config_list.md)の`plugin.path`で指定されたディレクトリに配置することで、認証Pluginとして利用可能になります。

### jarファイル仕様

jarファイルには、実装したクラスの他に以下の属性を持つマニフェストを同梱します。

#### Plugin-Class属性

ロードするクラスを以下の例のように指定してください。  
```
Plugin-Class: io.personium.plugin.auth.sample.SampleAuthPlugin
```

この際、指定できるクラスは以下の2種類です。

- 認証Plugin本体
  - 上記仕様に従って実装されたプラグインクラス
  - インタフェース`io.personium.plugin.base.auth.AuthPlugin`を実装したクラス
- 認証Pluginを初期化するクラス
  - 上記仕様に従って実装されたプラグインクラスの初期化方法を定め、インスタンス化するクラス
  - インタフェース`io.personium.plugin.base.auth.AuthPluginLoader`を実装したクラス

**AuthPluginLoaderについて**

Plugin-Class属性に「認証Plugin本体」を指定した場合、クラスのデフォルトコンストラクタが呼ばれインスタンス化されますが、
同一クラスを複数のパラメタで初期化して使用するケースではAuthPluginLoaderインタフェースを実装したクラスを指定してください。

AuthPluginLoaderを実装するクラスには以下のメソッドを実装してください。

- loadInstances()  
  プラグインクラスのインスタンス化を行う。AuthPluginのインスタンスのListを返却する。


---
## サンプル実装

以下にサンプル実装を示します。

- [personium-plugin-sample](https://github.com/personium/personium-plugin-sample)

## Pluginのセットアップ手順

- [認証Pluginのセットアップ](../server-operator/setup_authentication_plugins.md)をご参照ください。  
