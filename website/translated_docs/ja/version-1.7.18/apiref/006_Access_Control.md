---
id: version-1.7.18-006_Access_Control
title: アクセス制御モデル
sidebar_label: アクセス制御モデル
---

## ACL
ACLによるアクセス主体へアクセス制御は、[WebDAV ACL](https://www.ietf.org/rfc/rfc3744)をロールベースアクセスコントロールに応用したもので行なっている。  
CellやBox・コレクション等にACLメソッドでACL設定をすることで、そのリソースへのアクセス権限を設定出来る。  
基本的にはWebDAV ACLの仕様に準じるが、このページではPersonium独自の仕様について説明を行う。

ACL設定内容はXMLで定義する。

### PersoniumにおけるACL構成要素
PersoniumのACLは、以下の要素で構成される。

|要素名|内容|
|:--|:--|
|ace|ACL設定を行うアクセス主体とその権限付与のセットを表す|
|pricipal|設定されるACLのアクセス主体を定義する|
|grant|principalに付与すべきprivilegeを単数または複数定義する|
|privilege|権限設定を定義する|

### 制限事項
PersoniumV1系では、以下のような制限事項がある。
* ACLは既存設定を上書きする形で更新される
* deny要素による権限の剥奪設定
* 付与出来る権限の一覧取得

### 対象
PersoniumのACL設定の対象はリソースであり、各リソースのURLへのACLメソッドで設定を行う。  
セルのパスの場合 セルレベルACL となり、ボックス配下のパスの場合 ボックスレベルACL となる。  
この２つは設定出来るPrivilege（権限）が異なり、互いに影響することは無い。  

||内容|対象のリソース|
|:--|:--|:--|
|セルレベルACL|セルへの設定や、セル制御オブジェクトのCRUDを制御する|セル|
|ボックスレベルACL|Box配下のリソースへのCRUDを制御する|Box、WebDAVコレクション、ODataコレクション、Serviceコレクション、Streamコレクション<br>WebDAVコレクション配下のディレクトリ・ファイル|

## ace
対象となるアクセス主体はPrincipal要素、権限付与はgrant要素で定義する。ace要素は複数設定が出来る。

### Principal
Principalは、WebDAV ACLには「human or computational actor」とあるが、Personiumではロールであると定義する。  
PersoniumのロールはWebDAV ACLにおける「Group」に近い概念となる。

#### all
WebDAV ACLに定義されている通り、pricipalにall要素を設定すると権限付与設定を、
全てのロールや認証されていないアクセス主体（Authorizationヘッダーなし）にも定義することができる。  
リソースへの全てのアクセス主体に対する権限となるため、利用する場合には注意が必要。

```
principal:all
privilege:all
```

上記の設定で、アクセスしてきた全てのアクセスに全ての操作を開放する事になる。  
**ただし、スキーマ認証レベル設定が行われている場合は、そちらのチェックが有効になる**

##### 設定例
全てのアクセス主体にread権限を付与する。

```
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xml:base="https://cell1.unit1.example/__role/box1/"
    xmlns:p="urn:x-personium:xmlns"
    p:requireSchemaAuthz="none">
  <D:ace>
    <D:principal>
      </D:all>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```

#### ロール
対象となるアクセス主体にロールを定義する場合は、href要素で囲んだ上で、ロールリソースURLを設定する。  
ロールリソースについての仕様は ロール発行を参照。  

なお、設定出来るロールリソースURLはACL設定対象のセルURLと異なるロールリソースURLを指定することは出来ない。  

##### 設定例
Principalに設定するロールリソースURLを全て記述する  
（box1に紐付くdoctorにreadとwriteの権限を与え、box2に紐付くguestにはreadのみを与える場合の例）  

```
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:"
    xmlns:p="urn:x-personium:xmlns"
    p:requireSchemaAuthz="none">
  <D:ace>
    <D:principal>
      <D:href>https://cell1.unit1.example/__role/box1/doctor</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
      <D:privilege><D:write/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>https://cell1.uni1.example/__role/box2/guest</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```

xml:baseによる記述の省略  
acl要素のxml:base属性にボックスまでのロールリソースURLを記述することで、Principalに設定するロールリソースURLの記述を省略することができる。  
（box1に紐付くdoctorにreadとwriteの権限を与え、box2に紐付くguestにはreadのみを与える場合の例）  

```
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xml:base="https://cell1.unit1.example/__role/box1/"
    xmlns:p="urn:x-personium:xmlns"
    p:requireSchemaAuthz="none">
  <D:ace>
    <D:principal>
      <D:href>doctor</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
      <D:privilege><D:write/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>../box2/guest</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```

※guestの様に、xml:baseのボックスと異なるボックスに紐付くロールを設定する場合、上記の様に相対パスを使った記述を行う事が出来る。  

#### PROPFINDでの出力
ACL設定をPROPFINDで出力した際、xml:base属性は以下の様に出力される。
* セルへのPROPFINDの場合、メインボックスのURL
* Box配下へのPROPFINDの場合、そのBoxまでのURL

### grant/Privilege
権限はPersoniumが定義した要素で設定し、grant要素内のPrivilege要素に囲んで設定する。  
また、grant要素の中にはPrivilege要素を複数指定することが出来る。  

#### セルレベルACL Privilege
設定したセルに対して、セル制御オブジェクトの実行権限やメソッドの実行権限を指定する。  
上位に位置する権限が設定されている場合、下位に属する権限を有する。(例:messageは、message-readの権限も有する)  

|権限名|対象セル制御オブジェクト|上位の権限名|実行できるメソッド|備考|
|:--|:--|:--|:--|:--|
|root|以下の全ての権限を有する|-|全て||
|auth|Account,Role,ExtRole|root|PUT,POST,DELETE,GET,OPTIONS||
|auth-read|Account,Role,ExtRole|auth|GET,OPTIONS||
|message|RecievedMessage,SentMessage|root|POST,DELETE,GET,OPTIONS||
|message-read|RecievedMessage,SentMessage|message|GET,OPTIONS||
|event|event|root|PUT,POST,DELETE,GET,OPTIONS||
|event-read|event|event|GET,OPTIONS||
|log|log|root|PUT,POST,DELETE,GET,OPTIONS||
|log-read|log|log|GET,OPTIONS||
|social|Relation,ExtCell|root|PUT,POST,DELETE,GET,OPTIONS||
|social-read|Relation,ExtCell|social|GET,OPTIONS||
|box|Box|root|PUT,POST,DELETE,GET,OPTIONS||
|box-read|Box|box|GET,OPTIONS||
|box-install|Box|box|MKCOL（Barファイルインストール）||
|box-export|Box|root|GET（Barファイルエクスポート）※未サポート||
|acl|Cell|root|ACL||
|acl-read|Cell|acl|PROPFINDのACL設定表示||
|propfind|Cell|root|PROPFIND||
|rule|Rule|root|POST,DELETE,GET,OPTIONS|v1.6.0以降|
|rule-read|Rule|rule|GET,OPTIONS|v1.6.0以降|

##### 設定例

```
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns"
    xml:base="https://cell1.unit1.example/__role/box1/">
  <D:ace>
    <D:principal>
      <D:href>role10</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><p:root/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>../box2/role13</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><p:social/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>role15</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><p:acl/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```

#### ボックスレベルACL Privilege
設定したボックス以下のリソースに対して、メソッドの実行権限を指定する。  
ボックスレベルPrivilegeは基本的にWebDAV ACLに沿って定義されている。  
上位に位置する権限が設定されている場合、下位に属する権限を有する。(例：readは、read-propertiesの権限も有する)  

|権限名|対象セル制御オブジェクト|上位の権限名|実行できるメソッド|
|:--|:--|:--|:--|
|all|以下の全ての権限を有する|p:root|全て|
|read|読み出し権限を有する。read-aclは含まない。|all|GET,OPTIONS|
|write|書き出し権限を有する。write-aclは含まない。|all|PUT,POST,DELETE,MKCOL|
|read-properties|プロパティの読み出し権限を有する。|read|PROPFIND|
|write-properties|プロパティの書き出し権限を有する。|write|PROPPATCH|
|read-acl|ACLの読み出し権限を有する。|all|PROPFINDのACL設定表示|
|write-acl|ACLの書き出し権限を有する。|all|ACL|
|write-content|コンテンツの書き出し権限を有する。bindとunbindは含まない。|write|PUT（対象が存在する）|
|bind|コンテンツの追加権限を有する。write-contentは含まない。|write|PUT（対象が存在しない）,MKCOL|
|unbind|配下リソースの削除権限を有する。write-contentは含まない。|write|DELETE|
|exec|サービス実行権限を有する。※Personium独自実装|all|-|
|stream-send|Streamへの送信権限を有する。※Personium独自実装|all|PUT,POST,OPTIONS|
|stream-receive|Streamからの受信権限を有する。※Personium独自実装|all|GET,OPTIONS|

MOVEは、移動元コレクションのunbind権限と移動先コレクションのbind権限が必要。<br>
移動先に対象リソースが存在する場合は、加えて移動先コレクションのunbind権限が必要。

##### 設定例

```
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xml:base="http://cell1.unit1.example/__role/box1/"
    xmlns:p="urn:x-personium:xmlns"
    p:requireSchemaAuthz="none">
  <D:ace>
    <D:principal>
      <D:href>doctor</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
      <D:privilege><D:write/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>../box2/guest</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```

## ACLの継承
ボックスレベルACLの設定は、アクセスしたリソースの親（上位のディレクトリ）の設定をセルまで遡って適用される。  
アクセス主体に対するACL設定は、親の設定が追加される形で継承される。  
よって、ACLの設定時には以下の点に注意が必要となる。  
* 親にall等の強い権限を設定している場合、子に制限をかけても無効となる

### ACLの継承と適応される権限の例
リソース例  

|リソースのタイプ|リソース名|リソースURL|
|:--|:--|:--|
|セル|cell|https&#58;//cell.unit1.example/|
|ボックス|box|https&#58;//cell.unit1.example/box|
|WebDAVコレクション|webdav|https&#58;//cell.unit1.example/box/webdav|
|ディレクトリ|directory|https&#58;//cell.unit1.example/box/webdav/directory|
|ファイル|file|https&#58;//cell.unit1.example/box/webdav/directory/file|

上記のリソースに下記のACL設定を行った上で、各リソースへのアクセス時に適用される権限は以下のとおり。  

|アクセスするリソース|設定された権限|適用される権限|
|:--|:--|:--|
|セル|auth-read|auth-read|
|ボックス|read-acl|auth-read,read-acl|
|WebDAVコレクション|read|auth-read,read-acl,read|
|ディレクトリ|設定なし|auth-read,read-acl,read|
|ファイル|read-propaties|auth-read,read-acl,read-properties,read|

## スキーマ権限要求レベル
スキーマ権限要求レベルによるアプリケーションへのアクセス制御 は、ACL設定時にACL要素の RequireSchemaAuthz 属性で要求レベルの設定を行う。  
スキーマ認証の仕様については、認証モデルの「スキーマ認証（アプリ認証）」を参照。  

### 設定値
スキーマ権限要求レベル値  

|レベル値|内容|
|:--|:--|
|none（デフォルト）|スキーマ認証無しでアクセス可能|
|public|スキーマ認証結果がOKであればアクセス可能|
|confidential|スキーマ認証結果がOKで、かつ特殊ロールconfidentialClientがあればアクセス可能|

#### 設定例
スキーマ権限要求レベル設定ACLのサンプル  

```
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xml:base="https://cell1.unit1.example/__role/box1/"
    xmlns:p="urn:x-personium:xmlns"
    p:requireSchemaAuthz="none">
  <D:ace>
    <D:principal>
      <D:all/>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
      <D:privilege><D:write/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```

### スキーマ権限要求レベルの設定の継承
スキーマ権限要求レベル設定は、アクセスしたリソースに設定がされていない場合のみ、アクセスしたリソースの親（上位のディレクトリ）の設定をボックスまで遡って適用される。  
スキーマ権限要求レベルが未設定の場合、 none として扱われるが、明示的に none が設定されている場合、継承は行われない。  
継承はBoxまで遡って確認されるが、途中のリソースにスキーマレベル設定が行われていた時点で、その設定値が有効となる。  

#### スキーマ権限要求レベルの継承と適応される権限の例
上記のリソースに下記のスキーマ権限要求レベル設定を行った上で、各リソースへのアクセス時に適用される  
スキーマ権限要求レベルは以下のとおり。  

リソース例  

|リソースのタイプ|リソース名|リソースURL|
|:--|:--|:--|
|セル|cell|https&#58;//cell.unit1.example/|
|ボックス|box|https&#58;//cell.unit1.example/box|
|WebDAVコレクション|webdav|https&#58;//cell.unit1.example/box/webdav|
|ディレクトリ|directory|https&#58;//cell.unit1.example/box/webdav/directory|
|ファイル|file|https&#58;//cell.unit1.example/box/webdav/directory/file|

上記のリソースに下記のACL設定を行った上で、各リソースへのアクセス時に適用される権限は以下のとおり。  

|アクセスするリソース|設定されたレベル|適用されるレベル|
|:--|:--|:--|
|ボックス|confidential|confidential|
|WebDAVコレクション|public|public|
|ディレクトリ|設定なし|public|
|ファイル|none|none|
