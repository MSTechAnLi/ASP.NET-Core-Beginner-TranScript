import sys
import re

srt_path = sys.argv[1]
en_path  = sys.argv[2]
zh_path  = sys.argv[3]

with open(srt_path, 'r', encoding='utf-8-sig') as f:
    srt = f.readlines()

with open(en_path, 'r', encoding='utf-8-sig') as f:
    en = f.readlines()

with open(zh_path, 'r', encoding='utf-8-sig') as f:
    zh = f.readlines()

txt = ''
for i,line in enumerate(srt):
    if i % 5 == 0:
        txt += str(i // 5 + 1) + '\n'
    elif i % 5 == 2:
        txt += en[i // 5]
    elif i % 5 == 3:
        txt += zh[i // 5]
    else:
        txt += line

f_en = open('new.srt', 'w', encoding='utf-8-sig')
f_en.write(txt)
f_en.close()

print('已替换SRT，请重命名当前目录下的new.srt文件。')