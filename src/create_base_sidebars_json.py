import json
import os
from os import path

sidebars_dict = {
  'ja': {
    "README": ["ja/README"]
  },
  'en': {
    "README": ["en/README"]
  }
}

def add_info(locale, target_dir, filename):
  value = '/'.join([locale, target_dir, filename[:-3]])
  if target_dir in sidebars_dict[locale]:
    if filename.startswith('README'):
      sidebars_dict[locale][target_dir] = [value] + sidebars_dict[locale][target_dir]
    else:
      sidebars_dict[locale][target_dir].append(value)
  else:
    sidebars_dict[locale][target_dir] = [value]

def main():
  for locale in ('ja', 'en'):
    for dirname in os.listdir(locale):
      if not dirname.endswith('.md') and dirname != 'apiref':
        for filename in os.listdir(path.join(locale, dirname)):
          if filename.endswith('.md'):
            # print((locale, dirname, filename))
            add_info(locale, dirname, filename)
  sidebars_json = json.dumps(sidebars_dict, indent=2)
  print(sidebars_json)

if __name__ == "__main__":
    main()