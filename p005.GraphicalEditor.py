# -*- coding: utf-8 -*-

def changeColor(x, y, c, t):
    if x < 0 or x > len(map[0])-1 or y < 0 or y > len(map)-1 :
        return
    color = map[y][x]
    if color == t:
        map[y][x] = c
    else:
        return
    changeColor(x-1, y, c, t)
    changeColor(x+1, y, c, t)
    changeColor(x, y-1, c, t)
    changeColor(x, y+1, c, t)


file = 'p005.GraphicalEditor.in'
f = open(file, 'r')

map = []
while True:
    line = f.readline().strip()
    contents = line.split()
    cmd = contents[0]
    if cmd == "X":
        break
    if cmd == "I":
        m = int(contents[1])
        n = int(contents[2])
        for i in xrange(n):
            map.append(["O"] * m)
    if cmd == "S":
        name = contents[1]
        print name
        for row in map:
            print "".join(row)
    if cmd == "L":
        x = int(contents[1])-1
        y = int(contents[2])-1
        c = contents[3]
        map[y][x] = c
    if cmd == "F":
        x = int(contents[1])-1
        y = int(contents[2])-1
        c = contents[3]
        t = map[y][x]
        changeColor(x,y,c,t)
    if cmd == "V":
        x = int(contents[1])-1
        y1 = int(contents[2])-1
        y2 = int(contents[3])-1
        c = contents[4]
        for y in range(y1,y2+1):
            map[y][x] = c
    if cmd == "H":
        x1 = int(contents[1])-1
        x2 = int(contents[2])-1
        y = int(contents[3])-1
        c = contents[4]
        for x in range(x1,x2+1):
            map[y][x] = c

""" INPUT
I 5 6
L 2 3 A
S one.bmp
G 2 3 J
F 3 3 J
V 2 3 4 W
H 3 4 2 Z
S two.bmp
X
"""

""" OUTPUT
one.bmp
OOOOO
OOOOO
OAOOO
OOOOO
OOOOO
OOOOO
two.bmp
JJJJJ
JJZZJ
JWJJJ
JWJJJ
JJJJJ
JJJJJ
"""

