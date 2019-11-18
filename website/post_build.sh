#!/bin/bash -xe
BUILD_DIR='./build/personium/'

sed -i \
  -e 's|<title>[^<>]*</title>|<title>News - Personium</title>|g' \
  -e 's|<meta property="og:title" content=".*" |<meta property="og:title" content="News - Personium" |g' \
  ${BUILD_DIR}blog/{index.html,atom.xml,feed.xml}
