# Rule作成
## 概要
新規のイベント処理ルールを作成する。

### 必要な権限
rule

### 制限事項
* リクエストヘッダのAcceptは無視される
* リクエストヘッダのContent-Typeは全てapplication/jsonとして扱う
* リクエストボディはJSON形式のみ受け付ける
* レスポンスヘッダのContent-Typeはapplication/jsonのみをサポートし、レスポンスボディはJSON形式とする

## リクエスト
### リクエストURL
```
{CellURL}__ctl/Rule
```

### メソッド
POST

### リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
|Content-Type|リクエストボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|
|Accept|レスポンスボディの形式を指定する|application/json|×|省略時は[application/json]として扱う|

### リクエストボディ
#### Format

JSON

|項目名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|\_Box.Name|ルールが紐づくべきBox名|有効な box名. このキーを指定しなかったりnull値を指定したリクエストは、いかなるBoxにも紐づかないRuleと解釈されます.|×||
|Name|作成するルールを識別するため任意の名前|Boxに紐づく場合はBox内で一意、Boxに紐づかない場合はセルで一意である必要があります。|×|省略時は自動的にuuidが割り当たります|
|EventType|ルールをトリガーするイベントのタイプの一致検査用文字列|Evnet Typeの値は、内部イベントでは[別表](277_Event_Summary.md)のようにTypeが定義されています。外部イベントでは任意のTypeを指定可能です。<br>時刻によってトリガーされるイベントタイプとして、timer.oneshotとtimer.periodicがあります。これらをタイマーイベントと呼びます。 |×|.ではじまる文字列の場合、後方一致でマッチングを行います。それ以外は前方一致でマッチングを行います。|
|EventSubject|ルールをトリガーすべきイベントのEvent Subject一致検査用文字列|Event Subject はアカウントを表すURLになります。有効な値はその完全一致文字列となります。スキームとしては、http、https、personium-localunitが利用可能です。 |×|httpもしくはhttpsのURLの場合、personium-localunitで指定可能なURLの場合はエラーとなります。personium-localunitにて指定してください。|
|EventObject|ルールをトリガーすべきイベントのEvent Object前方一致検査用文字列|Event object の値はイベントのタイプにより異なります。 任意の文字列を設定可能ですが、意味を持つ値はイベントタイプにより異なります。<br>イベントタイプがtimer.oneshotのときは、ルールをトリガーしたい時刻をエポックミリ秒で指定します。その時刻にこのルールがトリガーされます。イベントタイプがtimer.periodicのときは、ルールをトリガーしたい周期を分で指定します。周期的にこのルールがトリガーされます。 |×||
|EventInfo|ルールをトリガーすべきイベントのEvent Info前方一致検査用文字列|Event info の値はイベントのタイプにより異なります。 任意の文字列を設定可能ですが、意味を持つ値はイベントタイプにより異なります。|×||
|EventExternal|ルールをトリガーすべきイベントが外部イベントであるかどうかを表すフラグ|真偽値。外部イベントを検出したいときは true を設定してください。|×|デフォルト値 false|
|Action|イベントがマッチしたときに起動すべきアクション|有効な値は以下の別表|〇||
|TargetUrl|アクションに対する具体的なターゲットURL|Actionの値によって指定すべき値は変わります。規則は以下の別表 |×|フラグメントは設定しても無視されます。|

#### タイマーイベント記述の規則
| EventType | EventObject | EventExternal | 備考 |
|:--|:--|:--|:--|
| timer.oneshot | エポックミリ秒(必須) | falseのみ | 内部では分に切り捨てられます |
| timer.periodic | 分(必須) | falseのみ | |

タイマーイベントは次のようにイベント化されます。

| 項目名 | 値 |
|:--|:--|
| Subject | EventSubject |
| Schema | \_Box.NameのBoxのSchema |
| RequestKey | null |
| External | false |
| Type | EventType |
| Object | EventObject |
| Info | EventInfo |

そのため、このイベントはルールとマッチします。

EventSubjectには、他CellのSubjectを設定することも可能ですが、他Cellの場合は、ルールトリガー後にイベントのSubjectはnullに設定されます。

#### Valid Actions
|Action|説明|TargetUrl|備考|
|:--|:--|:--|:--|
|exec|エンジンscript が起動しPOSTメソッドでイベントデータが渡されます。|エンジンサービスのurl|-|
|relay|イベントをTargetUrlにリレーします。|イベントの情報をリレーすべきリレー先Url|-|
|relay.event|イベントをTargetUrlの外部イベント受付APIにリレーします。|イベントの情報をリレーすべきリレー先Cell URL|-|
|relay.data|EventObjectのurlからデータを読み出しTargetUrlにデータを書込みます。|データを書き込むurl|EventTypeはodata.create、odata.update、odata.patchのみ有効|
|log|Eventを info レベルでログ出力します。|-|-|
|log.info|Eventを info レベルでログ出力します。|-|-|
|log.warn|Eventを warn レベルでログ出力します。|-|-|
|log.error|Eventを error レベルでログ出力します。|-|-|

#### EventObject記述の規則
|EventExternal|\_Box.Name|EventType|EventObject|備考|
|:--|:--|:--|:--|:--|
|false|設定あり||personium-localbox:/...<br>personium-localcell:/\_\_...||
|false|設定なし||personium-localcell:/...||
|false||timer.oneshot<br>timer.periodic|数字のみの文字列||
|true|||任意の文字列|

#### TargetUrl記述の規則
|Action|\_Box.Name|TargetUrl|備考|
|:--|:--|:--|:--|
|exec|設定あり|personium-localbox:/...||
|exec|設定なし|personium-localcell:/...||
|relay|設定あり|スキームがhttp,https,personium-localunit,personium-localcell,personium-localboxのURL|httpもしくはhttpsのURLの場合、personium-localunitで指定可能なURLの場合はエラーとなります。personium-localunitにて指定してください。|
|relay|設定なし|スキームがhttp,https,personium-localunit,personium-localcellのURL|httpもしくはhttpsのURLの場合、personium-localunitで指定可能なURLの場合はエラーとなります。personium-localunitにて指定してください。|
|relay.event||{Cell URL}|httpもしくはhttpsのURLの場合、personium-localunitで指定可能なURLの場合はエラーとなります。personium-localunitにて指定してください。|
|relay.data|設定あり|スキームがhttp,https,personium-localunit,personium-localcell,personium-localboxのURL|httpもしくはhttpsのURLの場合、personium-localunitで指定可能なURLの場合はエラーとなります。personium-localunitにて指定してください。|
|relay.data|設定なし|スキームがhttp,https,personium-localunit,personium-localcellのURL|httpもしくはhttpsのURLの場合、personium-localunitで指定可能なURLの場合はエラーとなります。personium-localunitにて指定してください。|


### リクエストサンプル
```JSON
{"Name":"rule1", "EventExternal":true, "Action":"log"}
```

## レスポンス
### 成功時ステータスコード
201

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|X-Personium-Version|APIの実行バージョン|リクエストが処理されたAPIバージョン|
|Access-Control-Allow-Origin|クロスドメイン通信許可ヘッダ|返却値は"\*"固定|
|Content-Type|返却されるデータの形式||
|Location|作成したリソースへのURL||
|ETag|リソースのバージョン情報||
|DataServiceVersion|ODataのバージョン||

### レスポンスボディ
レスポンスはJSONオブジェクトで、オブジェクト（サブオブジェクト）に定義されるキー(名前)と型、並びに値の対応は以下のとおりです。

|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|ルート|d|object|オブジェクト{1}|
|{1}|results|array|オブジェクト{2}の配列|
|{2}|\_\_metadata|object|オブジェクト{3}|
|{3}|uri|string|作成したリソースへのURL|
|{3}|etag|string|Etag値|
|{2}|\_\_published|string|作成日(UNIX時間)|
|{2}|\_\_updated|string|更新日(UNIX時間)|
|{1}|\_\_count|string|$inlinecountクエリでの取得結果件数|

### Rule固有レスポンスボディ

|オブジェクト|項目名|Data Type|備考|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.Rule|
|{2}|Name|string|Rule名|
|{2}|\_Box.Name|string|関係対象のBox名|
|{2}|EventExternal|boolean||
|{2}|EventSubject|string||
|{2}|EventType|string||
|{2}|EventObject|string||
|{2}|EventInfo|string||
|{2}|Action|string||
|{2}|TargetUrl|string||


### レスポンスボディサンプル
```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/Rule(Name='rule1',_Box.Name='box1')",
        "etag": "W/\"1-1486368212581\"",
        "type": "CellCtl.Rule"
      },
      "Name": "rule1",
      "_Box.Name": "box1",
      "EventExternal": true,
      "EventSubject": null,
      "EventType": null,
      "EventObject": null,
      "EventInfo": null,
      "Action": "log",
      "TargetUrl": null,
      "__published": "/Date(1486368212581)/",
      "__updated": "/Date(1486368212581)/"
    }
  }
}
```
### エラーレスポンス
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル

```sh
curl "https://cell1.unit1.example/__ctl/Rule" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '{"Name":"rule1", "EventExternal":true, "Action":"log"}'
```
