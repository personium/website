---
id: version-1.7.21-277_Event_Summary
title: イベントの概要
sidebar_label: イベントの概要
---
## イベントモデル
[イベント受付API](278_Event_Reception.md)にて定義された外部イベント、およびPersonium内部で定義された内部イベントから構成されます。

![イベントモデル](assets/eventmodel.png "イベントモデル")


### 外部イベント
[イベント受付API](278_Event_Reception.md) にて、受け付けるイベントを表します。  
イベント受付APIによって受け付けたイベントは、イベントバスに出力されます。
### 内部イベント
Personium内部で保持する管理データ（OData/WebDAV/Service等）の状態をもとに実行される処理のことを表します。  
代表的な内部イベントとして、Personium APIのリクエストがあり、Personium APIのレスポンス返却時に実行結果をイベントとしてイベントバスに出力します。

## イベントフォーマット
イベントは以下の項目から構成されます。

| 項目名 | 説明 |
|:--|:--|
| Subject | Authorizationヘッダのトークンにより設定されます |
| Schema | Authorizationヘッダのトークンにより設定されます |
| RequestKey | X-Personium-RequestKeyヘッダにより設定されます |
| External | 外部イベントか内部イベントかを表します |
| Type | イベントのタイプを表します |
| Object | イベントの対象を表します |
| Info | イベントの情報を表します |

### 内部イベント詳細
Typeは、操作に対して定義されています。
リンクおよびリンク解除では、エンティティ名の順序を昇順に正規化します。以下に例を示します。

|| 正規化 |
|:--|:--|
| cellctl.Role.links.Box.create | cellctl.Box.links.Role.create |
| cellctl.Relation.links.ExtCell.delete | cellctl.ExtCell.links.Relation.delete |

Objectは、基本的には、URLもしくは、キーを含めたURLが設定されます。
URLは、personium-localcellスキームによるURLであり、キーを含めたURLは、作成後のキーを付与したURLになります。
例えば、\_\_idが0123のentityを作成した場合、リクエストURLとキーを含めたURLは以下のようになります。

| リクエストURL | キーを含めたURL |
|:--|:--|
| http&#58;//cell1.unit1.example/box/col/entity | personium-localcell:/box/col/entity('0123') |

Objectにおけるキーは、正規化されています。正規化の例を以下に示します。

| | 正規化 |
|:--|:--|
| Role(’role’) | Role(Name=’role’, \_Box.Name=null) |
| Role(\_Box.Name=null, Name=’role’) | Role(Name=’role’, \_Box.Name=null) |
| Account(Name=’hoge’) | Account(’hoge’) |

Infoは、基本的には、リクエストのレスポンスコードとリクエストURLが設定されます。リクエストURLは、リクエストされたときのURLであり、引数も含みます。
更新操作では、変更後のキーが設定されます。変更後のアクセス先を得るためにInfoに設定しています。

| Type | Object | Info |
|:--|:--|:--|
| celctl.Role.update | personium-localcell:/\_\_ctl/Role(Name='role1', \_Box.Name=null) | 204,(Name='role2', \_Box.Name=null) |

変更後のオブジェクトにアクセスするには、変更後のキーを使用して以下のURLにする必要があります。
```
personium-localcell:/__ctl/Role(Name='role2', _Box.Name=null)
```

#### Cell Level API
##### Cell制御オブジェクト

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| 基本操作 | 作成 | cellctl.xxx.create | キーを含めたURL | 201,リクエストURL ||
|| 取得 | cellctl.xxx.get | URL | 200,リクエストURL ||
|| 一覧取得 | cellctl.xxx.list | URL | 200,リクエストURL ||
|| 更新 | cellctl.xxx.update | URL | 204,変更後のキー ||
|| 削除 | cellctl.xxx.delete | URL | 204 ||
| 他オブジェクトとのリンク | リンク | cellctl.xxx.links.yyy.create | キーを含めたURL | 204 ||
|| リンク解除 | cellctl.xxx.links.yyy.delete | URL | 204 ||
|| リンク一覧取得 | cellctl.xxx.links.yyy.list | URL | 200,リクエストURL ||
| 紐づく他オブジェクト操作 | 作成 | cellctl.xxx.navprop.yyy.create | キーを含めたURL | 201,リクエストURL ||
|| 一覧取得 | cellctl.xxx.navprop.yyy.list | URL | 200,リクエストURL ||

xxxやyyyには、Cell制御オブジェクト名が入ります。
* Account
* Role
* ExtCell
* Relation
* ExtRole
* Box
* SentMessage
* ReceivedMessage
* Rule

##### アクセス制御

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| Cell | ACL設定 | cell.acl | personium-localcell:/ | 200 ||
|| プロパティ取得 | cell.propfind | personium-localcell:/ | 207 ||
|| プロパティ変更 | cell.proppatch | personium-localcell:/ | 207 ||
| Box | ACL設定 | box.acl | URL | 200 ||
|| プロパティ取得 | box.propfind | URL | 207 ||
|| プロパティ変更 | box.proppatch | URL | 207 ||

##### Boxインストール

| 状態 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|
| Boxインストール受付 | boxinstall | URL | 202など | Boxインストールの受付が失敗するとInfoの値は変わります |
| Boxインストール処理中 | PL-BI-1000 | URL | Bar installation started. ||
|| PL-BI-1001 | Barファイル内のエントリパス | Installation started. ||
|| PL-BI-1003 | Barファイル内のエントリパス | Installation completed. ||
|| PL-BI-1004 | Barファイル内のエントリパス | Installation failed({原因}). ||
|| PL-BI-1005 || Unknown error({原因}). ||
| Boxインストール完了 | PL-BI-0000 | URL | Bar installation completed. ||
|| PL-BI-0001 | URL | Bar installation failed({原因}). ||

BoxインストールによりCell制御オブジェクトの作成が実行されることがあります。そのイベントは以下になります。

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| 基本操作 | 作成 | cellctl.xxx.create | キーを含めたURL | box install | |
| 他オブジェクトとのリンク | リンク | cellctl.xxx.links.yyy.create | キーを含めたURL | box install | |

##### Box再帰削除

| Type | Object | Info | 備考 |
|:--|:--|:--|:--|
| box.delete | URL | 204 ||

##### Cell間のメッセージ交換

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| メッセージ送信 | 送信 | message.send | 送信メッセージ取得用URL | 201 ||
|| 受信 | message.receive | 受信メッセージ取得用URL | 201 | メッセージを受信したCellにてイベント化 |
| 状態変更 | 既読 | message.read | 受信メッセージ取得用URL | 204 ||
|| 未読 | message.unread | 受信メッセージ取得用URL | 204 ||
|| 承認 | message.approve | 受信メッセージ取得用URL | 204 ||
|| 拒否 | message.reject | 受信メッセージ取得用URL | 204 ||

送信メッセージ取得用URLと受信メッセージ取得用URLの例を以下に示します。

|| URL |
|:--|:--|
| 送信メッセージ取得用URL | personium-localcell:/\_\_ctl/SentMessage(’12345’) |
| 受信メッセージ取得用URL | personium-localcell:/\_\_ctl/ReceivedMessage(’12345’) |

メッセージ承認によりCell制御オブジェクトの作成と削除が実行されることがあります。そのイベントは以下になります。

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| 基本操作 | 作成 | cellctl.ExtCell.create | キーを含めたURL | approved for message 12345 | 12345はメッセージidです |
|| 作成 | cellctl.Rule.create | キーを含めたURL | approved for message 12345 | 12345はメッセージidです |
|| 削除 | cellctl.Rule.delete | URL | approved for message 12345 | 12345はメッセージidです |
| 他オブジェクトとのリンク | リンク | cellctl.ExtCell.links.Relation.create | キーを含めたURL | approved for message 12345 | 12345はメッセージidです |
|| リンク | cellctl.ExtCell.links.Role.create | キーを含めたURL | approved for message 12345 | 12345はメッセージidです |
|| リンク解除 | cellctl.ExtCell.links.Relation.delete | URL | approved for message 12345 | 12345はメッセージidです |
|| リンク解除 | cellctl.ExtCell.links.Relation.delete | URL | approved for message 12345 | 12345はメッセージidです |

##### その他機能

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| エクスポート | 実行 | cell.export | personium-localcell:/\_\_export |||
| インポート | 実行 | cell.import | personium-localcell:/\_\_import |||

#### Box Level API
##### WebDAV基本操作

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| WebDav Collection | 作成 | webdavcol.mkcol | URL | 201 ||
|| ACL設定 | webdavcol.acl | URL | 200 ||
|| プロパティ取得 | webdavcol.propfind | URL | 207 ||
|| プロパティ変更 | webdavcol.proppatch | URL | 207 ||
|| 削除 | webdavcol.delete | URL | 204 ||
| OData Service Collection | 作成 | odatacol.mkcol | URL | 201 ||
|| ACL設定 | odatacol.acl | URL | 200 ||
|| プロパティ取得 | odatacol.propfind | URL | 207 ||
|| プロパティ変更 | odatacol.proppatch | URL | 207 ||
|| 削除 | odatacol.delete | URL | 204 ||
| Engine Service Collection | 作成 | servicecol.mkcol | URL | 201 ||
|| ACL設定 | servicecol.acl | URL | 200 ||
|| プロパティ取得 | servicecol.propfind | URL | 207 ||
|| プロパティ変更 | servicecol.proppatch | URL | 207 ||
|| 削除 | servicecol.delete | URL | 204 ||
| Stream Collection | 作成 | streamcol.mkcol | URL | 201 ||
|| ACL設定 | streamcol.acl | URL | 200 ||
|| プロパティ取得 | streamcol.propfind | URL | 207 ||
|| プロパティ変更 | streamcol.proppatch | URL | 207 ||
|| 削除 | streamcol.delete | URL | 204 ||
| ファイル | 登録 | davfile.create | URL | 201 ||
|| 更新 | davfile.update | URL | 204 ||
|| 取得 | davfile.get | URL | 200 ||
|| ACL設定 | davfile.acl | URL | 200 ||
|| プロパティ取得 | davfile.propfind | URL | 207 ||
|| プロパティ変更 | davfile.proppatch | URL | 207 ||
|| 削除 | davfile.delete | URL | 204 ||

##### ODataサービスコレクション
###### データ操作

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| 基本操作 | 作成 | odata.create | キーを含めたURL | 201,リクエストURL ||
|| 取得 | odata.get | URL | 200,リクエストURL ||
|| 一覧取得 | odata.list | URL | 200,リクエストURL ||
|| 更新 | odata.update | URL | 204,変更後のキー ||
|| 部分更新 | odata.patch | URL | 204,変更後のキー ||
|| 削除 | odata.delete | URL | 204 ||
| 他EntitySetのEntityとのリンク | リンク | odata.links.create | キーを含めたURL | 204 ||
|| リンク解除 | odata.links.delete | URL | 204 ||
|| リンク一覧取得 | odata.links.list | URL | 200,リクエストURL ||
| 紐づく他EntitySet操作 | 作成 | odata.navprop.create | キーを含めたURL | 201,リクエストURL ||
|| 一覧取得 | odata.navprop.list | URL | 200,リクエストURL ||

###### スキーマ定義

|| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|:--|
| 基本操作 | 作成 | odata.xxx.create | キーを含めたURL | 201,リクエストURL ||
|| 取得 | odata.xxx.get | URL | 200,リクエストURL ||
|| 一覧取得 | odata.xxx.list | URL | 200,リクエストURL ||
|| 更新 | odata.xxx.update | URL | 204,変更後のキー ||
|| 部分更新 | odata.xxx.patch | URL | 204,変更後のキー ||
|| 削除 | odata.xxx.delete | URL | 204 ||
| EntityTypeや他のAssociationEndとのリンク | リンク | odata.xxx.links.yyy.create | キーを含めたURL | 204 ||
|| リンク解除 | odata.xxx.links.yyy.delete | URL | 204 ||
|| リンク一覧取得 | odata.xxx.links.yyy.list | URL | 200,リクエストURL ||

xxxやyyyには、スキーマ定義用EntitySet名が入ります。

##### Engineサービスコレクション

| 操作 | Type | Object | Info | 備考 |
|:--|:--|:--|:--|:--|
| サービス実行 | service.exec | URL | 200など | スクリプトの実行結果によりInfoの値は変わます |


## イベントの処理
イベントバスに出力されたイベントは、[ルール](2A0_Create_Rule.md)の条件と合致するか判定され、合致した場合は、ルールに記述されたアクションを実行される。
アクションには、以下が指定可能。
* ログ出力
* スクリプト実行
* 中継
* イベント中継
* データ中継

### ルールとのマッチング
下記表の通りに項目毎に判定を行い、すべての項目が合致した場合に、ルールに合致したと判定する。

| イベント | ルール | 判定 | 備考 |
|:--|:--|:--|:--|
| Subject | EventSubject | 完全一致 | EventSubjectがnullのときは合致と判定 |
| Schema | \_Box.NameのBoxのSchema | 完全一致 | \_Box.Nameがnullのときは合致と判定 |
| RequestKey || 判定に使用しません ||
| External | EventExternal | 完全一致 ||
| Type | EventType | 前方一致もしくは後方一致 | .で始まるEventTypeのときは後方一致で、それ以外は前方一致。<br>EventTypeがnullのときは合致と判定 |
| Object | EventObject | 前方一致 | EventObjectがnullのときは合致と判定 |
| Info | EventInfo | 前方一致 | EventInfoがnullのときは合致と判定 |


### ログ出力アクション
ログ出力アクションは、イベントの内容をイベントログとして出力します。
ログ出力アクションには、以下の種類があります。

| アクション | 説明 |
|:--|:--|
| log<br>log.info | INFOレベルでログを出力します |
| log.warn | WARNレベルでログを出力します |
| log.error | ERRORレベルでログを出力します |

イベントにはログ出力レベルはなく、アクションにてレベルを指定します。

#### ルール例
Cell制御オブジェクトのRole操作をログ出力する例

| 項目名 | 設定 | 備考 |
|:--|:--|:--|
| \_Box.Name | null ||
| Name | output\_cellctlRole | 設定しなくてもよいです |
| EventType | cellctl.Role. ||
| EventSubject | null ||
| EventObject | personium-localcell:/\_\_ctl/Role | EventTypeで限定されるので実際には冗長です |
| EventInfo | null ||
| EventExternal | false ||
| Action | log ||
| TargetUrl | null ||

Roleを操作するとログがINFOレベルで出力されます。

#### イベントログフォーマット
出力形式は以下の通り。
```
{dateTime},[{level}],{RequestKey},{External},{Schema},{Subject},{Type},{Object},{Info}
```

#### イベントログアクセス方法
イベントログは、WebDAV上で管理するため、イベントログファイルへのアクセスはWebDAV用のAPIで行う。
* [ログファイル一覧取得](284_Retrieve_Log_File_list.md)
* [ログファイル取得](285_Retrieve_Log_File.md)
* [ログファイル削除](286_Delete_Log_File.md)

#### イベントログ保管期間
イベント量に応じてイベントログファイルのサイズが増大するため、一定量にてイベントログファイルをローテートする。  
ローテートされたイベントログファイルの保持世代数は、最大12世代とする。  
なお、ローテート時の最大サイズは、デフォルト50MBとし、ログ設定更新APIにて設定可能とする。

#### 出力例
##### 外部イベントの出力例
```
2013-04-18T14:52:39.778Z,[ERROR],"Req_animal-access_1001","true",
"https://app-cell1.unit1.example/","https://unitadmin.unit1.example/#admin","actionData",
"/svc/token_keeper","resultData"
2013-04-18T14:52:40.688Z,[INFO ],"Req_animal-access_2001","true",
"https://app-cell1.unit1.example/","https://unitadmin.unit1.example/#admin","action",
"/svc/token_keeper","result"
2013-04-18T15:01:46.994Z,[INFO ],"Req_animal-access_2001","true",
"https://app-cell1.unit1.example/","https://unitadmin.unit1.example/#admin","action",
"/svc/token_keeper","result"
2013-04-18T15:06:19.294Z,[ERROR],"Req_animal-access_1001","true",
"https://app-cell1.unit1.example/","https://unitadmin.unit1.example/#admin","actionData",
"/svc/token_keeper","resultData"
2013-04-18T15:06:23.360Z,[INFO ],"Req_animal-access_2001","true",
"https://app-cell1.unit1.example/","https://unitadmin.unit1.example/#admin","action",
"/svc/token_keeper","result"
2013-04-18T15:09:18.073Z,[ERROR],"Req_animal-access_1001","true",
"https://app-cell1.unit1.example/","https://unitadmin.unit1.example/#admin","actionData",
"/svc/token_keeper","resultData"
```
##### 内部イベントの出力例
```
2013-04-18T14:52:39.779Z,[INFO ],"Req_animal-access_1001","false",
"https://app-cell1.unit1.example/","https://app-cell1.unit1.example/#staff","odata.update",
"https://homeClinic.unit1.example/box/col/put_blog","204"
2013-04-18T14:52:39.780Z,[INFO ],"Req_animal-access_1001","false",
"https://app-cell1.unit1.example/","https://app-cell1.unit1.example/#staff","odata.get",
"https://homeClinic.unit1.example/box/col/blog_20130418","200"
```

### スクリプト実行アクション
スクリプト実行アクションは、イベントの内容を渡して自Cellのサービスを実行します。
アクションは、execです。

#### ルール例
メッセージ受信でサービスを実行する例

| 項目名 | 設定 | 備考 |
|:--|:--|:--|
| \_Box.Name | null ||
| Name | exec\_messagereceive | 設定しなくてもよいです |
| EventType | message.receive ||
| EventSubject | null ||
| EventObject | null ||
| EventInfo | null ||
| EventExternal | false ||
| Action | exec ||
| TargetUrl | personium-localcell:/box/col/srv ||

メッセージを受信したとき、TargetUrlのサービスが実行されます。サービスにて受信メッセージを確認して必要に応じて承認することができます。

#### サービスへのパラメータ
JSON形式のBodyとリクエストヘッダでイベントの内容を渡します。

| 項目名 | データソース | 備考 |
|:--|:--|:--|
| Subject | JSON ||
| Schema | JSON ||
| External | JSON ||
| Type | JSON ||
| Object | JSON | httpやhttpsスキームに変換されたURL |
| Info | JSON ||
| RequestKey | ヘッダ | x-personium-requestkey |

JSONは、サービス実行において、引数のinputフィールドから取得します。
```
function(request) {
  var bodyAsString = request["input"].readAll();
  var params = JSON.parse(bodyAsString);
```
ヘッダは、サービス実行において、引数のheadersフィールドから取得します。
```
function(request) {
  var reqHeaders = request["headers"];
  var requestKey = reqHeaders['x-personium-requestkey'];
```

#### スクリプト実行時のトークン
Authorizationヘッダにアクセストークンが設定されます。

| 項目名 | 設定値 |
|:--|:--|
| Subject | イベントのSubjectと同じ |
| Schema | イベントのSchemaと同じ |

#### 事前設定
スクリプトが実行できるように権限を設定しておく必要があります。

### 中継アクション
中継アクションは、イベントの内容を渡して他Cellのサービスを実行します。
アクションは、relayです。

#### ルール例
OData作成操作で中継する例

| 項目名 | 設定 | 備考 |
|:--|:--|:--|
| \_Box.Name | null ||
| Name | relay\_odatacreate | 設定しなくてもよいです |
| EventType | odata.create ||
| EventSubject | null ||
| EventObject | personium-localcell:/box/odatacol/entity ||
| EventInfo | null ||
| EventExternal | false ||
| Action | relay ||
| TargetUrl | personium-localunit:/otherCell/box/col/srv ||

TypeおよびObjectが合致する内部イベントのとき、TargetUrlへイベントを中継します。

#### スクリプトへのパラメータ
スクリプト実行アクションと同じです。

#### スクリプト実行時のトークン
Authorizationヘッダには、サービスを実行するためにトランスセルトークンが設定されています。

| 項目名 | 設定値 |
|:--|:--|
| Subject | イベントのSubjectと同じ |
| Schema | イベントのSchemaと同じ |

#### 事前設定
スクリプトが実行できるように権限を設定しておく必要があります。

### イベント中継アクション
イベント中継アクションは、イベントの内容を他Cellの外部イベント受付に中継します。
アクションは、relay.eventです。

#### ルール例
外部イベント受付で中継する例

| 項目名 | 設定 | 備考 |
|:--|:--|:--|
| \_Box.Name | null ||
| Name | relayevent\_eventreceipt | 設定しなくてもよいです |
| EventType | null ||
| EventSubject | https&#58;//cell1.unit1.example/#account ||
| EventObject | null ||
| EventInfo | null ||
| EventExternal | true ||
| Action | relay.event ||
| TargetUrl | https&#58;//cell2.unit1.example/ ||

Subjectが合致する外部イベントのとき、イベント中継を行います。

#### リクエスト
##### リクエストヘッダ

| ヘッダ名 | 設定値 | 備考 |
|:--|:--|:--|
| X-Personium-RequestKey | イベントのRequestKey ||
| Authorization | トランスセルトークン<br>イベントのSubjcetとSchemaを設定<br>中継元のRoleリストを設定 ||

##### リクエストボディ

| 項目名 | 設定値 | 備考 |
|:--|:--|:--|
| Type | 以下の表のように変換された値 ||
| Object | イベントのObject ||
| Info | イベントのInfo ||

Typeの変換

| External | Type |
|:--|:--|
| true | relay.ext. を先頭に追加 |
| false | relay. を先頭に追加 |

既にTypeがrelay.で始まっていれば、Typeの変換は行われません。

#### イベント中継によるイベント伝播の例
cell1で起きたイベントをcell2を経由してcell3にイベント中継する例

##### 内部イベントの場合

###### ルール
| 項目名 | cell1 | cell2 |
|:--|:--|:--|
| \_Box.Name | null | null |
| Name | relayevent | relayevent |
| EventType | cellctl | null |
| EventSubject | null | https&#58;//cell1.unit1.example/#account |
| EventObject | null | null |
| EventInfo | null | null |
| EventExternal | false | true |
| Action | relay.event | relay.event |
| TargetUrl | https&#58;//cell2.unit1.example/ | https&#58;//cell3.unit1.example/ |

###### 伝播されるイベント
| 項目名 | cell1 | cell2 | cell3 |
|:--|:--|:--|:--|
| Subject | https&#58;//cell1.unit1.example/#account | <- | <- |
| Schema | https&#58;//app-cell1.unit1.example/ | <- | <- |
| External | false | true | true |
| Type | cellctl.Role.create | relay.cellctl.Role.create | <- |
| Object | https&#58;//cell1.unit1.example/\_\_ctl/Role('role') | <- | <- |
| Info | 201,https&#58;//cell1.unit1.example/\_\_ctl/Role | <- | <- |

##### 外部イベントの場合

###### ルール
| 項目名 | cell1 | cell2 |
|:--|:--|:--|
| \_Box.Name | null | box2 |
| Name | relayevent | relayevent |
| EventType | null | null |
| EventSubject | null | https&#58;//cell1.unit1.example/#account |
| EventObject | object | null |
| EventInfo | null | null |
| EventExternal | true | true |
| Action | relay.event | relay.event |
| TargetUrl | https&#58;//cell2.unit2.example/ | https&#58;//cell3.unit3.example/ |

cell2のbox2のSchemaは、https&#58;//app-cell1.unit1.example/とします。

###### 伝播されるイベント
| 項目名 | cell1 | cell2 | cell3 |
|:--|:--|:--|:--|
| Subject | https&#58;//cell1.unit1.example/#account | <- | <- |
| Schema | https&#58;//app-cell1.unit1.example/ | <- | <- |
| External | true | true | true |
| Type | type | relay.ext.type | <- |
| Object | object | <- | <- |
| Info | info | <- | <- |

#### 事前設定
外部イベント受付へのアクセスに必要な権限を設定しておく必要があります。

### データ中継アクション
データ中継アクションは、ODataとして書き込まれた内容をTargetUrlに書き込みます。
アクションは、relay.dataです。

イベントのTypeがodata.createのときは、TargetUrlにPOSTし、イベントのTypeがodata.update、odata.patchのときは、TargetUrlにPUTします。
PUTのときの{EntityID}は、イベントのObjectの{EntityID}を使用します。

#### ルール例
OData作成操作でデータ中継する例

| 項目名 | 設定 | 備考 |
|:--|:--|:--|
| \_Box.Name | null ||
| Name | relaydata\_odatacreate | 設定しなくてもよいです |
| EventType | odata.create ||
| EventSubject | null ||
| EventObject | personium-localcell:/box/odatacol/entity ||
| EventInfo | null ||
| EventExternal | false ||
| Action | relay.data ||
| TargetUrl | personium-localunit:/otherCell/box/col/queue/name ||

TypeおよびObjectが合致する内部イベントのとき、ODataとして書かれた内容をTargetUrlへ書き込みます。

#### TargetUrlへのパラメータ
ODataのレスポンスのresultsから、\_\_metadata、\_\_published、\_\_updatedを削除したJSON Stringを渡します。\_\_idは、JSON Stringに含まれます。

PUT時のTargetUrlは、イベントのObjectが以下であった場合、
```
    personium-localcell:/box/odatacol/entity('id1')
```
上記ルール例では、
```
    personium-localunit:/otherCell/box/col/queue/name('id1')
```
としてアクセスを行います。

#### TargetUrlへのトークン
Authorizationヘッダには、アクセストークンもしくはトランスセルトークンが設定されています。

| 項目名 | 設定値 |
|:--|:--|
| Subject | イベントのSubjectと同じ |
| Schema | イベントのSchemaと同じ |

#### 事前設定
ODataのread権限、およびTargetUrlへの書き込み権限(writeやstream-send)を設定しておく必要があります。
