---
id: 301_Bar_File
title: barファイル
sidebar_label: barファイル
---
barファイルはBoxインストールAPIのリクエストボディとして指定するファイル形式である。  
barファイルは、Box配下に定義するOdata/WebDAV/Serviceの各データを格納しており、ZIPファイル形式でアーカイブされる。  
通常は、[BoxエクスポートAPI](385_Box_Export.md)にて、PersoniumからアーカイブされたBox配下のデータ定義がエクスポートされる。

### Specifications
ファイルフォーマットはZIP形式とし、ZIP64形式も許容する。  
また、ZIPファイルの暗号化は対応しない。

#### Directory Structure
barファイル内のディレクトリ構成を以下に示す。  
Boxインストール時に「★必須」となっているディレクトリ、及びファイルが存在しない場合は、必須のディレクトリ/ファイルがない旨のエラー（400 Bad Request）を返却する。  
```
/
 |
 +-- 00_meta/  ★ 必須
 |    |
 |    +-- 00_manifest.json  ★ 必須
 |    +-- 10_relations.json
 |    +-- 20_roles.json
 |    +-- 30_extroles.json
 |    +-- 50_rules.json
 |    +-- 70_$links.json
 |    +-- 90_rootprops.xml  ★ 必須
 |
 +-- 90_contents/     ★ 配下のディレクトリ名はコレクション名と同じ
      |
      +-- {OData}/    ★ rootprops.xmlでODataコレクションの場合、必須
      |    |
      |    +-- 00_$metadata.xml    ★ 必須
      |    +-- 10_odatarelations.json
      |    |
      |    +-- 90_data/
      |         |
      |         +-- {EntityType}/
      |              |
      |              +-- {1.json}
      |
      +-- {Service}/
      |    |
      |    +-- {src.js}
      |
      +-- {dir1}/
           |
           +-- {dir1-1}/
                |
                +-- {userdata1-2.jpg}
                |
                +-- {dir2}/
                     |
                     +-- [userdata1-2.jpg}
```


#### Bar File Version Control
エンハンス等によってデータ構造が変更となり、後方互換が確保できなくなった場合にbarファイルのバージョンアップを行う。
* ファイルの追加レベルではバージョンアップしない
* ファイルのフォーマットやファイル名などを変更・削除した場合にバージョンアップする

### File List
#### 00_manifest.json
インストールする対象となるBoxの情報を記述したファイル

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|bar_version|barファイルのバージョン|有効なバージョン<br>barファイル形式の変更ごとにバージョンが変わる|○|現状は"2"|
|box_version|Boxのバージョン|有効なバージョン<br>Box形式の変更ごとにバージョンが変わる|○|任意の文字列で良いが"1"を推奨（Box改版機能提供に向けて）|
|default_path|barファイル内でのBox名|桁数：1&#65374;128<br>文字種:半角英数字と-(半角ハイフン)と_(半角アンダーバー)<br>ただし、先頭文字に-(半角ハイフン)と_(半角アンダーバー)は指定不可<br>nullは不可|○||
|schema|Schema名|桁数：1&#65374;1024<br>URIの形式に従う（scheme：http / https / urn）|○||

##### サンプル
```JSON
{
  "bar_version": "2",
  "box_version": "1",
  "default_path": "box1",
  "schema": "http://app-cell1.unit1.example"
}
```
#### 10_relations.json
インストール対象とするRelationの情報を記述したファイル  
※「有効値」欄が『&#65293;』となっている項目項目は、Relationのリクエストボディを参照

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Relations|Relationのリスト||○||
|Relations/Name|Relation名|-|○||


##### サンプル
```JSON
{
  "Relations": [
    {
      "Name": "relation1"
    }
  ]
}
```
#### 20_roles.json
インストール対象とするRoleの情報を記述したファイル  
※「有効値」欄が『&#65293;』となっている項目は、、Roleのリクエストボディを参照

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Roles|Roleのリスト||○||
|Roles/Name|Role名|-|○||

##### サンプル
```JSON
{
  "Roles": [
    {
      "Name": "role1"
    }
  ]
}
```
#### 30_extroles.json
インストール対象とするExtRoleの情報を記述したファイル  
※「有効値」欄が『&#65293;』となっている項目は、ExtRoleのリクエストボディを参照

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|ExtRoles|ExtRoleのリスト||○||
|ExtRoles/ExtRole|参照先RoleのURI|&#65293;|○|nullは不可 ※1|
|ExtRoles/_Relation.Name|Relation名|&#65293;|○|nullは不可|

(※ 1) エクスポート時にロールクラスURLへ変換  
https&#58;//cell1.unit1.example/__role/box/staff → https&#58;//cell1.unit1.example/\_\_role/\_\_/staff  

##### サンプル
```JSON
{
  "ExtRoles": [
    {
      "ExtRole": "https://cell1.unit1.example/__role/__/role2",
      "_Relation.Name": "Relation1"
    }
  ]
}
```
#### 50_rules.json
インストール対象とするRuleの情報を記述したファイル  
※「有効値」欄が『&#65293;』となっている項目は、、Ruleのリクエストボディを参照

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Rules|Ruleのリスト||○||
|Rules/EventExternal|マッチするイベントの外部イベントフラグ|-|×||
|Rules/EventSubject|マッチするイベントのSubject|-|×||
|Rules/EventType|マッチするイベントの型|-|×||
|Rules/EventObject|マッチするイベントのObject|-|×||
|Rules/EventInfo|マッチするイベントの情報|-|×||
|Rules/Action|イベントマッチ時のアクション|-|○||
|Rules/TargetUrl|アクションの処理対象となるUrl|-|×||

##### サンプル
```JSON
{
  "Rules": [
    {
      "Action": "exec",
      "TargetUrl": "personium-localbox:/col/srv"
    }
  ]
}
```
#### 70_$links.json
インストール対象とする$linksのデータ関連情報を記述したファイル

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Links|$linksのリスト||○||
|Links/FromType|参照元データの種類|"Relation"<br>"Role"<br>"ExtRole"|○|nullは不可|
|Links/FromName|参照元データの名前|&#65293;(配列形式 ※1)|○|nullは不可<br> （例:{"Name":"relation1"}]）|
|Links/ToType|参照先データの種類|"Relation"<br>"Role"<br>"ExtRole"|○|nullは不可|
|Links/ToName|参照先データの名前|&#65293;(配列形式 ※1)|○|nullは不可<br>（例:{"Name":"role"}]）|
※1 ExtRoleではRelation情報も必要のため、リスト形式とする。ただし、指定するJSONデータのキー名は、"Name" 固定とする。（制限）

##### サンプル
```JSON
{
  "Links": [
    {
      "FromType": "Relation",
      "FromName":
        {
          "Name": "relation1"
        },
      "ToType": "Role",
      "ToName":
        {
          "Name": "role1"
        }
    },
    {
      "FromType": "Role",
      "FromName":
        {
          "Name": "role1"
        },
      "ToType": "ExtRole",
      "ToName": {
          "ExtRole": "https://cell1.unit1.example/__role/__/role2",
          "_Relation.Name": "Relation1"
        }
    }
  ]
}
```
#### 90_rootprops.xml
barファイルにエクスポートする対象のBox配下の全階層に対して、PROPFINDメソッドで取得したXMLデータを示す。  
XMLデータの詳細は、[ファイル設定取得（PROPFIND）](307_Get_Property.md)を参照。  
インストール対象BoxのURLは、「personium-localbox:/」と記述する。  
barファイルのインストール時には、下記サンプルの<prop>配下にある creationdate及び、getlastmodifiedを除いた全てのデータをインストール対象とする。
* resourcetype: コレクションの種類を設定
* acl: 権限を設定
* Other: PROPPATCHで設定

##### サンプル
```xml
<multistatus xmlns="DAV:">
  <response>
    <href>personium-localbox:/</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns">
          <ace>
            <principal>
              <href>admin</href>
            </principal>
            <grant>
              <privilege>
                <all/>
              </privilege>
            </grant>
          </ace>
        </acl>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/odata</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
          <p:service xmlns:p="urn:x-personium:xmlns"/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns">
          <ace>
            <principal>
              <href>user</href>
            </principal>
            <grant>
              <privilege>
                <read/>
              </privilege>
              <privilege>
                <write/>
              </privilege>
              <privilege>
                <read-properties/>
              </privilege>
            </grant>
          </ace>
        </acl>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/dav</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns">
          <ace>
            <principal>
              <href>user</href>
            </principal>
            <grant>
              <privilege>
                <read/>
              </privilege>
              <privilege>
                <write/>
              </privilege>
              <privilege>
                <read-properties/>
              </privilege>
            </grant>
          </ace>
        </acl>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/dav/testdavfile.txt</href>
    <propstat>
      <prop>
        <getcontenttype>text/plain</getcontenttype>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
          <p:service xmlns:p="urn:x-personium:xmlns"/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
        <p:service language="JavaScript" xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
          <p:path name="ehr" src="ehr.js"/>
          <p:path name="ehr_connector" src="ehr_connector.js"/>
        </p:service>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr_connector.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
</multistatus>
```
#### contents/{OData}/
##### 00_$metadata.xml
ユーザODataのスキーマ定義を示す。barファイルにエクスポートする時に、Odata用コレクションに対して$metadataにて取得したXMLデータ。  
XMLデータの詳細は、[スキーマ取得（$metadata）](316_User_Defined_Data_Schema.md)を参照。  
Boxインストール時には、Schemaタグの配下をインストール対象とする。  
ユーザODataのスキーマ定義が存在しない場合でもファイル自体は存在する。

スキーマ定義がない場合のサンプル
```xml
<Edmx:Edmx Version = '1 .0' xmlns:edmx =' http://schemas.microsoft.com/ado/2007/06/edmx' 
xmlns:d =' http://schemas.microsoft.com/ado/2007 / 08/dataservices' 
xmlns:m = 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata' 
xmlns:p = 'urn: x-personium: xmlns'>
  <edmx:DataServices m:DataServiceVersion='1.0'>
    <Schema Xmlns='http://schemas.microsoft.com/ado/2006/04/edm' Namespace='UserData'>
      <EntityContainer Name='UserData' m:IsDefaultEntityContainer='true'/>
    </Schema>
  </Edmx:DataServices>
</Edmx:Edmx>
```

##### 10_odatarelations.json
インストール対象ユーザデータの$linksのデータ関連情報を記述したファイル
ユーザODataのスキーマレベルでは、00_$metadata.xml にてAssociationEndの関連を定義しているが、本ファイルではユーザデータの実体に対する関連を定義する。

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Links|$linksのリスト||○||
|Links/FromType|参照元データの種類|&#65293;|○|nullは不可|
|Links/FromId|参照元ユーザデータのID|&#65293;(配列形式 ※1)|○|nullは不可<br> （例:{&quot;FromId&quot;:&quot;tanaka_taro&quot;} ）|
|Links/ToType|参照先データの種類|&#65293;|○|nullは不可|
|Links/ToId|参照先ユーザデータのID|&#65293;(配列形式 ※1)|○|nullは不可<br>（例:{"ToId":"tanaka_hanako"} ）|
※1 将来的に複合主キーへ対応した場合の対応を考慮して配列形式とする。

##### サンプル
```JSON
{
  "Links": [
    {
      "FromType": "Keeper",
      "FromId": {
        "usercode": "001",
        "Name": "Peru_Taro"
      },
      "ToType": "Animal",
      "ToId": {
        "shopcode": "001",
        "Name": "pochi"
      }
    },
    {
      "FromType": "Keeper",
      "FromId": {
        "usercode": "002",
        "Name": "Peru_Hanako"
      },
      "ToType": "Animal",
      "ToId": {
        "shopcode": "002",
        "Name": "tama"
      }
    }
  ]
}
```
#### 90_data / {EntityType} / {1.json}
ユーザデータを1件ずつJSON形式で格納する。

```JSON
{
  "__id": "entity1",
  "name": "pochi",
  "address": {
    "country": "japan",
    "city": "tokyo"
  }
}
```

#### contents/Service/{src.js}
bar/90_contents/{Service}/{src.js}に格納されたソースファイルを、インストール先Box配下の{Service}/\__src/{src.js}に登録する。
* bar/00_meta/90_rootprops.xmlにコレクション{Service}の定義（PROPPATCH）が無い場合は、サービスとして実行できない
* bar/00_meta/90_rootprops.xmlに{Service}/\__srcの定義が無い場合は、{src.js}は登録できない
* bar/00_meta/90_rootprops.xmlの{Service}/\__src/{src.js}の定義に従い、{src.js}のContent-Typeを設定する

サービス登録用90_rootprops.xmlのサンプル
```xml
<multistatus xmlns="DAV:">
  <response>
    <href>personium-localbox:/service</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
          <p:service xmlns:p="urn:x-personium:xmlns"/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
        <p:service language="JavaScript" xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns">
          <p:path name="ehr" src="ehr.js"/>
          <p:path name="ehr_connector" src="ehr_connector.js"/>
        </p:service>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src</href>
    <propstat>
      <prop>
        <resourcetype>
          <collection/>
        </resourcetype>
        <acl xml:base="https://cell1.unit1.example/__role/__/" xmlns:p="urn:x-personium:xmlns"/>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
  <response>
    <href>personium-localbox:/service/__src/ehr_connector.js</href>
    <propstat>
      <prop>
        <getcontenttype>text/javascript</getcontenttype>
      </prop>
    </propstat>
  </response>
</multistatus>
```
