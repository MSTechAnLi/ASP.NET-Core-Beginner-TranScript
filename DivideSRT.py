# 使用时将所需分割的srt文件路径作为参数
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

lines_en = [line for i, line in enumerate(lines) if i % 5 == 2]
lines_zh = [line for i, line in enumerate(lines) if i % 5 == 3]

txt_en = ''.join(lines_en)
txt_zh = ''.join(lines_zh)

f_en = open('en.txt', 'w', encoding='utf-8-sig')
f_en.write(txt_en)
f_en.close()

f_zh = open('zh.txt', 'w', encoding='utf-8-sig')
f_zh.write(txt_zh)
f_zh.close()

print('已分离中英文字幕，请重命名当前目录下的en.txt和zh.txt文件。')