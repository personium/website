---
id: README
title: How to participate in Personium document maintenance and improvement
sidebar_label: How to participate in Personium document maintenance and improvement
---

The open source project Personium welcomes not only code but also documentation contributions.
If you can help improve the documentation, please follow the steps below.

> __Please prepare a GitHub account__

## Document improvements pointed out

1. Create improvement issue in issues on GitHub repository
    1. [Personium Documentation Website issues](https://github.com/personium/website/issues)

By performing the above, Personium project members or other participants can correct and publish based on the pointed out.

## Adding and updating documentation

1. Fork the GitHub repository
    1. [Personium Documentation Website](https://github.com/personium/website)
1. Clone to Local repository
1. Update the document by referring to [Repository README](https://github.com/personium/website)
1. Push to Fork's own GitHub repository and issue a Pull Request to the parent repository of the Fork

By performing the above procedure, the Personium project members will review and publish it in an appropriate form.
We look forward to your cooperation.


***

> __Note of the Document description__

 * Line break in sentences 
    If you wish to line break in sentences, do not use `<br>`, enter two space characters and enter a new line.
    However, please use `<br>` if you want line break in the table.
   For example)  
       abcdefg  (two space characters)  
       hijklmn

 * How to disable the automatic conversion of URL to hyperlink during the MD to HTML conversion  
    If you make an entry like "http&#58;//~" in the MD file, it will be automatically converted to a hyperlink. If you do not want to have a hyperlink in the description. You have to explicitly write "`&#58;`" instead of ":".
    For example)
       `http&#58;//`

 * How to write of the cURL command sample  
    If the cURL command sample is longer than **100 characters**, please make a line feed so that the length per line is less than 100 characters.
    For example) 
    curl "https&#58;//{UnitFQDN}/__ctl/Cell" -X POST -i -H 'Authorization: Bearer {AccessToken}' `\`(Append \ to the line break position)
    -H 'Accept: application/json' -d '{"Name":"{CellName}"}'
