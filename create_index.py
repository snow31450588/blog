#!/usr/bin/env python
#encoding=utf-8


import os
import glob

'''
根据每天日志,生成索引列表.
约定只取第一行内容作为标题,第一行为空的则只打印log,不生成到列表中.
'''


def get_list(fd):
    ls = []

    for sub in os.listdir(fd):
        fd_month = os.path.join(fd, sub)
        if os.path.isdir(fd_month) and sub.isdigit():
            for file_name in glob.glob(os.path.join(fd_month, '*.md')):
                print(file_name)
                title = ''
                with open(file_name, 'rt', encoding='utf8') as fin:
                    lines = fin.read().splitlines()
                    if lines:
                        first_line = lines[0]
                        title = first_line.strip().strip('#').strip()
                if title:
                    print(title)
                else:
                    print('-'*100)
                    title = '-'*20
                ls.append((title, '/'.join((sub, os.path.basename(file_name)))))
    return ls


def write_index(fd, ls):
    with open(os.path.join(fd,'README.md'), 'wt', encoding='utf8') as fout:
        fout.write('# blog')
        fout.write(os.linesep)
        fout.write('----')
        fout.write(os.linesep)
        fout.write('## 文章列表')
        fout.write(os.linesep)
        fout.write('----  ')
        fout.write(os.linesep)
        for title, file_name in ls:
            fout.write('## [%s](%s)' % (title, file_name))
            fout.write(os.linesep)


if __name__ == '__main__':
    fd = os.path.dirname(os.path.abspath(__file__))
    ls = get_list(fd)
    write_index(fd, ls)
