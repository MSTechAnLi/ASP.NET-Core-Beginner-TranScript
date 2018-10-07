# 使用时将所需分割的srt文件路径作为参数
import sys
from datetime import datetime, timedelta

path = sys.argv[1]
try:
    f = open(path, 'r')
    lines = f.readlines()
except UnicodeDecodeError:
    f = open(path, 'r', encoding='utf-8')
    lines = f.readlines()
finally:
    f.close()

lines_time = [line[:-1].split(' --> ') for i, line in enumerate(lines) if i % 5 == 1]

times = {i:(datetime.strptime(item[0], '%H:%M:%S,%f'), datetime.strptime(item[1], '%H:%M:%S,%f')) \
            for i, item in enumerate(lines_time)}

timesChecked = []
delta = timedelta(microseconds=1000)
for i in range(len(times)):
    if i < len(times) - 1 and times[i][1] >= times[i+1][0]:
        time =  datetime.strftime(times[i][0], '%H:%M:%S,%f')[:-3]
        time += ' --> '
        time += datetime.strftime(times[i+1][0] - delta, '%H:%M:%S,%f')[:-3]
        timesChecked.append(time)
    else:
        time =  datetime.strftime(times[i][0], '%H:%M:%S,%f')[:-3]
        time += ' --> '
        time += datetime.strftime(times[i][1], '%H:%M:%S,%f')[:-3]
        timesChecked.append(time)

srt = ''
for i,line in enumerate(lines):
    if i % 5 == 1:
        srt += timesChecked[i // 5] + '\n'
    else:
        srt += line

f_en = open('new.srt', 'w', encoding='utf-8-sig')
f_en.write(srt)
f_en.close()

print('已检查重叠时间轴，请重命名当前目录下的new.srt文件。')