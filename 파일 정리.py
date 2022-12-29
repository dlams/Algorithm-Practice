from os import getcwd, mkdir, walk, system
from os.path import isdir
from shutil import move
from datetime import datetime

current_path = getcwd()  # 현재 위치
dir_path = current_path + '/Backjoon/'

for i in range(1, 25 + 1):
    if not isdir(dir_path + str(i * 1000)):
        mkdir(dir_path + str(i * 1000))

for (root, dir, files) in walk(dir_path):
    for f in files:
        if root.split("/")[-1].isnumeric():
            continue
        elif root.split("/")[-1] == "NOT_SOLVED":
            continue
        else:
            num, *name = f.split()
            num = int(num)
            move(dir_path + '/' + f, dir_path + '/' + str(num // 1000 * 1000) + '/' + f)
            print(num, "번 문제 : ", *name, " 이동 완료", sep="")

_TODAY = datetime.today()
system('git add .')
system(f'git commit -m "solve until {_TODAY.year % 100}.{_TODAY.month}.{_TODAY.day}"')
system('git push')
