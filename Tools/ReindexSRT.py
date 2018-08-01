# 使用时将需要重编号的srt文件路径作为参数
import sys

path = sys.argv[1]
try:
    f = open(path, 'r')
    lines = f.readlines()
except UnicodeDecodeError:
    f = open(path, 'r', encoding='utf-8')
    lines = f.readlines()
finally:
    f.close()

srt = ''
for i,line in enumerate(lines):
    if i % 5 == 0:
        srt += str(i // 5 + 1) + '\n'
    else:
        srt += line

f_en = open('new.srt', 'w', encoding='utf-8-sig')
f_en.write(srt)
f_en.close()

print('已重新排序SRT，请重命名当前目录下的new.srt文件。')