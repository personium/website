---
id: version-1.7.21-004_Error_Messages
title: Error Messages
sidebar_label: Error Messages
original_id: 004_Error_Messages
---

## Authentication API

|Response code|OAUTH error code|Message code|Message|
|:--|:--|:--|:--|
|400|unsupported_grant_type|PR400-AN-0001|Unsupported grant type.|
|400|invalid_request|PR400-AN-0002|Invalid p_target.|
|400|invalid_client|PR400-AN-0003|Failed to parse client secret.|
|400|invalid_client|PR400-AN-0004|Client secret is expired and invalid.|
|400|invalid_client|PR400-AN-0005|Client secret dsig is invalid.|
|400|invalid_client|PR400-AN-0006|Client secret issuer does not match the client_id.|
|400|invalid_client|PR400-AN-0007|Client secret target is wrong.|
|400|invalid_grant|PR400-AN-0008|Trans-Cell access can not represent owner.|
|400|invalid_grant|PR400-AN-0009|Token parse error.|
|400|invalid_grant|PR400-AN-0010|Token expired or invalid.|
|400|invalid_grant|PR400-AN-0011|Token dsig is invalid.|
|400|invalid_grant|PR400-AN-0012|Token target is wrong. target=[{0}]|
|400|invalid_grant|PR400-AN-0013|Not a refresh token.|
|400|invalid_grant|PR400-AN-0014|Not allowed to represent owner.|
|400|invalid_grant|PR400-AN-0015|Cell owner does not exist.|
|400|invalid_request|PR400-AN-0016|Required parameter [{0}] missing.|
|400|invalid_grant|PR400-AN-0017|Authentication failed.|
|400|invalid_client|PR400-AN-0018|Authorization header is invalid.|
|400|invalid_grant|PR400-AN-0019|Invalid grant code.|
|400|invalid_client|PR400-AN-0020|Client mismatch for refresh token. [{0}]|
|400|invalid_client|PR400-AN-0021|Client Authentication is required.|
|400|invalid_client|PR400-AN-0022|Invalid Client Assertion Type. Acceptable Value is [{0}].|
|401|invalid_grant|PR401-AN-0023|The password should be changed.|
|400|invalid_grant|PR400-AN-0030|Wrong IDToken Audience [{0}].|
|400|invalid_grant|PR400-AN-0031|OpenID Connect Authentication failed.|
|400|invalid_grant|PR400-AN-0032|OpenID Connect Invalid Token. ({0})|
|400|invalid_grant|PR400-AN-0033|OpenID Connect ID Token Expired (at UnixTime: {0}).|

## Other Resource API

|Response code|Message code|Message|Details|
|:--|:--|:--|:--|
|400|PR400-OD-0001|JSON parse error.||
|400|PR400-OD-0002|OData Query parse error.||
|400|PR400-OD-0003|OData $filter Parse Error.||
|400|PR400-OD-0004|OData EntityKey Parse error.||
|400|PR400-OD-0005|$format value [{0}] is invalid.||
|400|PR400-OD-0006|request body format error. field [{0}]||
|400|PR400-OD-0007|[{0}]||
|400|PR400-OD-0008|No such association.||
|400|PR400-OD-0009|[{0}] is required.||
|400|PR400-OD-0010|Key for Navigation Property should not be specified in $links POST.||
|400|PR400-OD-0011|Key for Navigation Property should be specified in $links.||
|400|PR400-OD-0012|Specifying the type of [{0}] is invalid.||
|400|PR400-OD-0013|$inlinecount value [{0}] is invalid.||
|400|PR400-OD-0014|Unknown property was appointed.||
|400|PR400-OD-0015|Odata $orderby parse error.||
|400|PR400-OD-0016|Single key should not be null.||
|400|PR400-OD-0017|OData $select Parse error.||
|400|PR400-OD-0018|Number of properties exceeds the limit [{0}].||
|400|PR400-OD-0019|AssociationEnd do not put request.||
|400|PR400-OD-0020|Schema mismatch.||
|400|PR400-OD-0021|$batch body format is invalid. Request header format is invalid [{0}].||
|400|PR400-OD-0022|$batch body format is invalid. Changeset should not have other changeset.||
|400|PR400-OD-0023|$batch body parse error.||
|400|PR400-OD-0024|[{0}] does not exist.||
|400|PR400-OD-0025|[{0}] does not exist.||
|400|PR400-OD-0026|OData $expand parse error.||
|400|PR400-OD-0027|The index definition of another type already exists.||
|400|PR400-OD-0028|OData EntityKey for $links parse error.||
|400|PR400-OD-0029|Query value [{0}]=[{1}] is invalid.||
|400|PR400-OD-0030|$batch body format is invalid. Too many requests. [{0}]||
|400|PR400-OD-0031|Cannot create $links because multiplicity is [1:1].||
|400|PR400-OD-0032|EntityType structure hierarchy exceeds the limit or number of properties exceeds the limit.||
|400|PR400-OD-0033|EntityType count exceeds the limit.||
|400|PR400-OD-0034|$batch body format is invalid. Request path format is invalid [{0}].||
|400|PR400-OD-0035|$batch body format is invalid. Request Method not allowed [{0}].||
|400|PR400-OD-0036|OData Query [{0}] parse error.||
|400|PR400-OD-0037|Total of the specified value of $top exceeds the limit.||
|400|PR400-OD-0038|$links count exceeds the limit.||
|400|PR400-OD-0039|Total of the specified value of $expand exceeds the limit.||
|400|PR400-OD-0040|Cannot specify the list type to $orderby.||
|400|PR400-OD-0041|Request header {0} value is invalid [{1}].||
|400|PR400-OD-0042|Operation is not supported: {0}||
|400|PR400-OD-0043|Unsupported operator specified in query.||
|400|PR400-OD-0044|Unsupported function specified in query.||
|400|PR400-OD-0045|An unknown property with name ''{0}'' was found.||
|400|PR400-OD-0046|Mismatched operand/argument is specified for ''{0}''.||
|400|PR400-OD-0047|Operand or argument for ''{0}'' has unsupported/invalid format.||
|400|PR400-OD-0048|Unable to parse operand or argument. ''{0}''||
|400|PR400-OD-0049|[{0}] field format error. Cell URL should be normalized URL with http(s) scheme and trailing slash.||
|400|PR400-OD-0050|[{0}] field format error. Schema URI should be either normalized URL with http(s) scheme and trailing slash, or URN.||
|400|PR400-OD-0051|Query value is invalid.||
|404|PR404-OD-0000|Not found.||
|404|PR404-OD-0001|No such entity set.||
|404|PR404-OD-0002|No such entity.||
|404|PR404-OD-0003|No such Navigation Property.||
|409|PR409-OD-0001|This entity has related data.||
|409|PR409-OD-0002|Links exists already.||
|409|PR409-OD-0003|The entity already exists.||
|409|PR409-OD-0004|The entity already exists. [{0}]||
|409|PR409-OD-0005|The entity already exists. [{0}]||
|409|PR409-OD-0006|Relation between EntityTypes already exists.||
|412|PR412-OD-0001|If-Match header is required.||
|412|PR412-OD-0002|ETag does not match.||
|412|PR412-OD-0003|Conflict.||
|415|PR415-OD-0001|Unsupported media type:[{0}].||
|500|PR500-OD-0001|Detected a duplicate of the property name:[{0}].||
|500|PR500-OD-0002|Internal data inconsistency detected.||
|400|PR400-DV-0001|XML parse error.||
|400|PR400-DV-0002|XML content error.||
|400|PR400-DV-0003|Invalid depth header value:[{0}].||
|400|PR400-DV-0004|Role not found.||
|400|PR400-DV-0005|Box not found url:[{0}].||
|400|PR400-DV-0006|XML validate error.||
|400|PR400-DV-0007|Cannot add any more child resources.||
|400|PR400-DV-0008|Hierarchy of the collection is too deep.||
|400|PR400-DV-0009|Request header {0} value is invalid [{1}].||
|400|PR400-DV-0010|Header {0} is required.||
|400|PR400-DV-0011|Prohibited to move service source collection.||
|400|PR400-DV-0012|Prohibited to overwrite collection resource.||
|400|PR400-DV-0013|Prohibited to move resource to OData collection.||
|400|PR400-DV-0014|Prohibited to move resource to file.||
|400|PR400-DV-0015|Prohibited to move box.||
|400|PR400-DV-0016|Prohibited to move resource to service collection.||
|400|PR400-DV-0017|Prohibited to overwrite service source collection.||
|400|PR400-DV-0018|Prohibited to create collection under service source collection.||
|403|PR403-DV-0001|Infinite depth is not supported.||
|403|PR403-DV-0003|Cannot delete collection if it has any child resources.||
|403|PR403-DV-0004|Resource name is invalid [{0}].||
|403|PR403-DV-0005|Destination header value [{0}] equals request URL.||
|404|PR404-DV-0001|Resource not found. [{0}].||
|404|PR404-DV-0002|Box not found at [{0}].||
|404|PR404-DV-0003|Cell not found.||
|405|PR405-DV-0001|Method not allowed. MKCOL can only be executed on a deleted/non-existent resource.||
|409|PR409-DV-0001|intermediate collection [{0}] should be created first.||
|409|PR409-DV-0002|File [{0}] already exists.||
|412|PR412-DV-0001|ETag does not match.||
|412|PR412-DV-0002|Overwrite header is "F" and the destination URL is already mapped to a resource.||
|416|PR416-DV-0001|Requested range not satisfiable.||
|500|PR500-DV-0001|File system inconsistency detected.||
|500|PR500-DV-0002|Dav system inconsistency detected.||
|503|PR503-DV-0001|Failed to access the target resource due to concurrent update/delete operation by another process.||
|400|PR400-SM-0001|ToRelation [{0}] does not exist.||
|400|PR400-SM-0002|ToRelation [{0}] does not have related ExtCell.||
|400|PR400-SM-0003|The maximum number of destinations was exceeded.||
|400|PR400-SM-0004|Box corresponding to the schema can not be found from the schema-authenticated token. Schema[{0}].||
|500|PR500-SM-0001|Sent Message connection error.||
|500|PR500-SM-0002|Sent Message body parse error.||
|400|PR400-RM-0001|Requested relation already exists.||
|400|PR400-RM-0002|Box corresponding to the schema can not be found. Schema [{0}].||
|400|PR400-RM-0003|Box corresponding to the RelationClassURL can not be found. RelationClassURL [{0}].||
|409|PR409-RM-0002|Requested relation does not exists. Type [{0}]. Keys [{1}].||
|409|PR409-RM-0004|Request relation target does not exist. Type [{0}]. Keys [{1}].||
|409|PR409-RM-0005|RequestRelation and RequestRelationTarget is not related. [Type [{0}]. Keys[{1}]] - [Type {2}. Keys[{3}]].||
|500|PR500-SC-0001|Engine connection error.||
|500|PR500-SC-0002|File open error.||
|500|PR500-SC-0003|File close error.||
|500|PR500-SC-0004|IO error.||
|500|PR500-SC-0005|Unknown error at Engine.||
|500|PR500-SC-0006|Invalid HTTP response was returned from a service.||
|400|PR400-AU-0001|Password format is invalid.||
|400|PR400-AU-0002|Request parameter is invalid [{0}].||
|400|PR400-AU-0003|Personium credential required.||
|401|PR401-AU-0001|Authorization required.||
|401|PR401-AU-0002|Access token expired.||
|401|PR401-AU-0003|Invalid authentication scheme.||
|401|PR401-AU-0004|Basic auth format error.||
|401|PR401-AU-0005|Authentication failed.||
|401|PR401-AU-0006|Token parse error.||
|401|PR401-AU-0007|Can not access with refresh token.||
|401|[PR401-AU-0008](./error/PR401-AU-0008.md)|Token dsig error.||
|401|PR401-AU-0009|Authentication failed.||
|401|PR401-AU-0010|Authentication failed.||
|401|PR401-AU-0011|Authentication failed.||
|401|PR401-AU-0012|Can not access with password change access token.||
|403|PR403-AU-0001|Unit user access required.||
|403|PR403-AU-0002|Necessary privilege is lacking.||
|403|PR403-AU-0003|This resource can not be accessed by the Unit User specified in authorization header.||
|403|PR403-AU-0004|Schema authentication is required to access this resource.||
|403|PR403-AU-0005|This resource can not be accessed with the schema that has been authenticated.||
|403|PR403-AU-0006|Insufficient schema authorization level.||
|400|PR400-AZ-0001|Unsupported response_type.||
|400|PR400-AZ-0002|Request parameter is invalid [client_id].||
|400|PR400-AZ-0003|Request parameter is invalid [redirect_uri].||
|400|PR400-AZ-0004|Request parameter is invalid [response_type].||
|400|PR400-AZ-0005|JSON parse error. {0}||
|400|PR400-AZ-0006|ID Token encoded invalid. {0}||
|400|PR400-AZ-0007|Box not installed.||
|400|PR400-AZ-0008|Authorization failed.||
|401|PR401-AZ-0001|User cancel.||
|401|PR401-AZ-0002|Token authorization error.||
|400|PR400-EV-0001|JSON parse error.||
|400|PR400-EV-0002|Request header is invalid [X-Personium-RequestKey].||
|400|PR400-EV-0003|[{0}] is required.||
|400|PR400-EV-0004|[{0}] field format error.||
|400|PR400-EV-0005|Cannot delete current eventLog file.||
|500|PR500-EV-0001|Failed to output http response.||
|500|PR500-EV-0002|Cannot open archive eventLog file.||
|500|PR500-EV-0003|Delete eventLog failed.||
|500|PR500-SV-0000|Unknown error.||
|500|PR500-SV-0001|Datastore connection error.||
|500|PR500-SV-0002|Datastore unknown error.||
|500|PR500-SV-0003|Elasticsearch request retry over [{0}].||
|500|PR500-SV-0004|File system access error [{0}].||
|500|PR500-SV-0005|Failed to search from datastore.||
|500|PR500-SV-0006|Failed to update data store, and failed to rollback.||
|500|PR500-SV-0007|Failed to update data store, and completed to rollback.||
|503|[PR503-SV-0001](./error/PR503-SV-0001.md)|Too many concurrent requests.||
|503|PR503-SV-0002|Server connection error.||
|503|PR503-SV-0003|Server error. (Lock Manager) Data lock state unknown.||
|503|PR503-SV-0004|Service is under maintenance [restoring].||
|503|PR503-SV-0005|Operation is prohibited as one or more disks are almost full.||
|503|PR503-SV-0006|Server connection error. (Datastore)||
|400|PR400-MC-0001|[{0}] does not exist in the snapshot file.||
|404|PR404-MC-0001|URI is not recognized.||
|405|PR405-MC-0001|Method not allowed.||
|408|PR408-MC-0001|Request timeout in server.||
|409|PR409-MC-0001|Cell to be deleted is being accessed by other requests.||
|412|PR412-MC-0001|Precondition failed [Header: {0}].||
|501|PR501-MC-0001|Method not implemented.||
|501|PR501-MC-0002|Not implemented. [{0}].||
|400|PR400-CM-0001|Required key [{0}] missing.||
|400|PR400-CM-0002|Field [{0}] format error. Must be [{1}].||
|400|PR400-CM-0003|Unknown key [{0}] specified.||
|400|PR400-CM-0004|JSON parse error. [{0}].||
|409|PR409-CM-0001|Cell status is [import failed]. Only Unit Level's APIs, CellImport and GetToken are executable.||
|409|PR409-CM-0002|Because [{0}] is being executed, writing to cell can not be done.||
|500|PR500-CM-0001|Failed to load the request body for some reason.||
|500|PR500-CM-0002|Files I/O error caused [{0}] to fail.||
|400|PR400-BI-0001|Request header is not defined or invalid [{0}].||
|400|PR400-BI-0002|Bar file size too large [{0}B].||
|400|PR400-BI-0003|Bar file entry size too large [{0}, {1}B].||
|400|PR400-BI-0004|Install target box is already registered as Box Schema[{0}].||
|400|PR400-BI-0005|Bar file size invalid[{0}, {1}B].||
|400|PR400-BI-0006|[{0}] file format error.||
|400|PR400-BI-0007|Cannot open bar file [{0}].||
|400|PR400-BI-0008|Cannot read bar file [{0}].||
|400|PR400-BI-0009|Invalid bar file structures [{0}].||
|405|PR405-BI-0001|Install target box is already registered [{0}].||
|500|PR500-BI-0001|Failed to output http response.||
|500|PR500-NW-0000|Network error. {0}||
|500|PR500-NW-0001|HTTP {0} request to {1} failed. Response code : {2}.||
|500|PR500-NW-0002|Unexpected response from {0}, where {1} expected.||
|500|PR500-NW-0003|Unexpected value from key={0}, where "{1}" value expected.||
|500|PR500-SV-9999|Unknown Exception [{0}] {1}||
|500|PR500-AN-0001|Root ca certificate setting error.||
|412|-|["{0}","{1}","{2}"...]|Return available Personium<br>version number|

