# 使用时将需要合并的两个文件做完参数传入
import sys
from itertools import chain

path_en = sys.argv[1]
path_zh = sys.argv[2]

# 姑且默认文件为utf-8-sig格式
with open(path_en, 'r', encoding='utf-8-sig') as f:
    lines_en = f.readlines()
with open(path_zh, 'r', encoding='utf-8-sig') as f:
    lines_zh = f.readlines()

with open('merged.txt', 'w', encoding='utf-8-sig') as f:
    f.writelines(chain(*zip(lines_en, lines_zh)))

print('已合并中英文字幕，请重命名当前目录下的merged.txt文件。')