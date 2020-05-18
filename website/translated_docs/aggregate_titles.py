import json
import os
from os import path
from collections import OrderedDict

sidebars_dict = {}

def add_info(locale, target_dir, filename, versions):
  file_path = '/'.join([locale, target_dir, filename])
  with open(file_path, encoding='utf-8') as f:
    for line in f:
      if line.startswith('title: '):
        title = ' '.join(line.split(' ')[1:]).rstrip()
        break
  sidebars_dict['%s/%s' % (target_dir, filename[:-3])] = {'title': title, 'sidebar_label': title}
  for version in versions:
    sidebars_dict['%s-%s/%s' % (version, target_dir, filename[:-3])] = {'title': title, 'sidebar_label': title}

def main():
  for locale in ('ja',):
    versions = []
    for dirname in os.listdir(locale):
      if dirname.startswith('version-'):
        versions.append(dirname)

    for dirname in os.listdir(locale):
      if not dirname.endswith('.md'):
        for filename in os.listdir(path.join(locale, dirname)):
          if filename.endswith('.md'):
            # print((locale, dirname, filename))
            add_info(locale, dirname, filename, versions)
    add_info(locale, '', 'README.md', versions)
  keys = sorted(sidebars_dict.keys())
  sorted_dict = OrderedDict()
  for key in keys:
    sorted_dict[key] = sidebars_dict[key]
  sidebars_json = json.dumps(sorted_dict, indent=2, ensure_ascii=False)
  print(sidebars_json)

if __name__ == "__main__":
    main()
