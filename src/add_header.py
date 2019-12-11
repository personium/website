from os import path

def add_header(dirpath, filename):
  fullpath = path.join(dirpath, filename)
  print(fullpath)

  with open(fullpath, encoding='utf-8') as f:
    line = f.readline()
    if not line.startswith('# '):
      print('Not start # ')
      return
    title = line[2:-1]
    print(title)
    with open('temp.md', encoding='utf-8', mode='w') as writer:
      header = [
        '---',
        'id: %s' % filename[:-3],
        'title: %s' % title,
        'sidebar_label: %s' % title,
        '---',
        ''
      ]
      writer.write('\n'.join(header))
      writer.write(f.read())

def main():
  add_header('.', '001_Personium_Architecture.md')

if __name__ == "__main__":
    main()