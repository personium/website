#!/bin/bash -xe
BUILD_DIR='./build/personium.github.io/'

sed -i \
  -e 's|<title>[^<>]*</title>|<title>News - Personium</title>|g' \
  ${BUILD_DIR}blog/{index.html,atom.xml,feed.xml}

sed -i \
  -e 's|<meta property="og:title" content="[^\"]*"|<meta property="og:title" content="News - Personium" |g' \
  ${BUILD_DIR}blog/index.html
