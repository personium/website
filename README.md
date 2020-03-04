# Personium Documentation

Website: https://personium.io

Builded website repository: https://github.com/personium/personium.github.io

## Directories and files

|path|content|
|----|-------|
|src/|en docs source|
|website/blog/|blog source|
|website/build/|build output|
|website/i18n/ja.json|ja translation for title, sidebar_label and others|
|website/static/|static files for website|
|website/translated_docs/ja/|ja docs source|
|website/siteConfig.js|Docusaurus config file|
|website/sidebars.json|Sidebars config file|

## How to update

Personium docs are using [Docusaurus](https://docusaurus.io/en/). Before update, see it's docs.
Install and configure your local environment.  
Only need to perfrom this once.  

1. Install [node.js](https://nodejs.org/) and [yarn](https://yarnpkg.com/)  
2. Clone this repository to your local environment  
3. If you are behind company proxy, follow instructions from [this site](https://www.jhipster.tech/configuring-a-corporate-proxy/) to configure your lcoal environment properly.  
4. Configure the environment using pre-defined configurations.  

```shell
$ cd website
$ npm install
```

Modify files and launch local web server to verify the changes.  

1. Modify source files
2. Check Website locally

```shell
$ cd website
$ yarn start
```

Until making stable version, updated docs can be seen in `next` version like

https://localhost:3000/new-docs/en/next/README/

3. Git commit & git push to your forked repository
4. Make a pull request

### Website (https://personium.io)  

Update `website/static/`

### News (https://personium.io/blog/)  

Update `website/blog/`

### Documentation

Update following.

Main contents:

|language|path|
|--------|----|
|en|`src/`|
|ja|`website/translated_docs/ja/`|

Sidebars:

`website/sidebars.json`

Sidebars label and title:

|language|path|
|--------|----|
|en|`src/*.md` header's title & sidebar_label|
|ja|`website/i18n/ja.json`|

### API Reference

Update following.

|language|path|
|--------|----|
|en|`src/apiref/`|
|ja|`website/translated_docs/ja/apiref/`|
