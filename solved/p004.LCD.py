# -*- coding: utf-8 -*-

file = 'p004.LCD.in'
f = open(file, 'r')

lcd = []
lcd.append([1,1,1,0,1,1,1])
lcd.append([0,0,1,0,0,1,0])
lcd.append([1,0,1,1,1,0,1])
lcd.append([1,0,1,1,0,1,1])
lcd.append([0,1,1,1,0,1,0])
lcd.append([1,1,0,1,0,1,1])
lcd.append([1,1,0,1,1,1,1])
lcd.append([1,0,1,0,0,1,0])
lcd.append([1,1,1,1,1,1,1])
lcd.append([1,1,1,1,0,1,1])


while True:
    s, n = [int(x) for x in f.readline().split()]
    if n == 0 and n == 0 :
        break
    nums = list(str(n))
    print nums
    # 상단
    p = " "
    for num in nums:
        num = int(num)
        if lcd[num][0] == 1:
            p += "-" * s
        else:
            p += " " * s
        p += " " * 3 # 공백추가
    print p

    # 상단 좌우
    for i in xrange(s):
        p = ""
        for num in nums:
            num = int(num)
            # 좌상
            if lcd[num][1] == 1:
                p += "|"
            else:
                p += " "
            p += " " * s# 공백추가
            # 우상
            if lcd[num][2] == 1:
                p += "|"
            else:
                p += " "
            p += " "
        print p

    # 중간
    p = " "
    for num in nums:
        num = int(num)
        if lcd[num][3] == 1:
            p += "-" * s
        else:
            p += " " * s
        p += " " * 3 # 공백추가
    print p

    # 하단 좌우
    for i in xrange(s):
        p = ""
        for num in nums:
            num = int(num)
            # 좌상
            if lcd[num][4] == 1:
                p += "|"
            else:
                p += " "
            p += " " * s# 공백추가
            # 우상
            if lcd[num][5] == 1:
                p += "|"
            else:
                p += " "
            p += " "
        print p
    # 하단
    p = " "
    for num in nums:
        num = int(num)
        if lcd[num][6] == 1:
            p += "-" * s
        else:
            p += " " * s
        p += " " * 3 # 공백추가
    print p

""" INPUT
2 12345
3 67890
0 0
"""

""" OUTPUT
['1', '2', '3', '4', '5']
      --   --        --
   |    |    | |  | |
   |    |    | |  | |
      --   --   --   --
   | |       |    |    |
   | |       |    |    |
      --   --        --
['6', '7', '8', '9', '0']
 ---   ---   ---   ---   ---
|         | |   | |   | |   |
|         | |   | |   | |   |
|         | |   | |   | |   |
 ---         ---   ---
|   |     | |   |     | |   |
|   |     | |   |     | |   |
|   |     | |   |     | |   |
 ---         ---   ---   ---
"""