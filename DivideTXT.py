# 使用时将所需分割的txt文件路径作为参数
import sys

path = sys.argv[1]
with open(path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

lines_en = [line for i, line in enumerate(lines) if i % 2 == 0]
lines_zh = [line for i, line in enumerate(lines) if i % 2 == 1]

with open('en.txt', 'w', encoding='utf-8-sig') as f:
    f.writelines(lines_en)

with open('zh.txt', 'w', encoding='utf-8-sig') as f:
    f.writelines(lines_zh)

print('已分离中英文字幕，请重命名当前目录下的en.txt和zh.txt文件。')