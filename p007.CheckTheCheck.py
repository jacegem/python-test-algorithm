# -*- coding: utf-8 -*-
import re

def isKing(r,c,e):
    if r > 0 and r  < 8 and c > 0 and c < 8 and map[r][c] == e :
        return True
    else:
        return False

def lookFor(r,c,dr,dc,e):
    while True:
        r += dr
        c += dc
        if r < 0 or r >= 8 or c < 0 or c>= 8:
            return False
        if map[r][c] == e:
            return True
        if map[r][c] != ".":
            return False
    return False

def lookForR(r,c,e):
    if lookFor(r,c,1,0,e) or lookFor(r,c,-1,0,e) or lookFor(r,c,0,1,e) or lookFor(r,c,0,-1,e):
        return True
    else:
        return False

def lookForB(r,c,e):
    if lookFor(r,c,1,1,e) or lookFor(r,c,1,-1,e) or lookFor(r,c,-1,1,e) or lookFor(r,c,-1,-1,e):
        return True
    else:
        return False

def lookForQ(r,c,e):
    if lookFor(r,c,1,1,e) or lookFor(r,c,1,-1,e) or lookFor(r,c,-1,1,e) or lookFor(r,c,-1,-1,e) or lookFor(r,c,1,0,e) or lookFor(r,c,-1,0,e) or lookFor(r,c,0,1,e) or lookFor(r,c,0,-1,e):
        return True
    else:
        return False



file = 'p007.CheckTheCheck.in'
f = open(file, 'r')

whites = []
blacks = []
map = []
emptyMap = []
emptyMap = [["." for i in xrange(8)] for i in xrange(8)]
idx = 0
while True:
    line = list(f.readline().strip())
    if line:
        map.append(line)
        continue
    if map == emptyMap:
        break
    idx += 1
    for r in range(len(map)):
        for c in range(len(map[r])):
            a = map[r][c]
            if re.match("[a-z]", a):
                whites.append((r,c,a))
            else:
                blacks.append((r,c,a))
    # 각 말을 확인해야 함
    bkf = False
    wkf = False
    for w in whites:
        e = "K"
        r = w[0]
        c = w[1]
        a = w[2]
        if a == "p":
            if isKing(r+1,c-1,e):
                bkf = True
            if isKing(r+1,c+1,e):
                bkf = True
        elif a == "r":
            if lookForR(r,c,e):
                bkf = True
        elif a == "b":
            if lookForB(r,c,e):
                bkf = True
        elif a == "q":
            if lookForQ(r,c,e):
                bkf = True
        elif a == "k":
            for i in range(-1,2):
                for j in range(-1,2):
                    if isKing(r+i,c+j,e):
                        bkf = True
        elif a == "n":
            if isKing(r+1,c+2,e) or isKing(r+1,c-2,e) or isKing(r-1,c+2,e) or isKing(r-1,c-2,e):
                bkf = True
            if isKing(r+2,c+1,e) or isKing(r+2,c-1,e) or isKing(r-2,c+1,e) or isKing(r-2,c-1,e):
                bkf = True
        if bkf:
            break

    for b in blacks:
        e = "k"
        r = b[0]
        c = b[1]
        a = b[2]
        if a == "P":
            if isKing(r+1,c-1,e):
                wkf = True
            if isKing(r+1,c+1,e):
                wkf = True
        elif a == "R":
            if lookForR(r,c,e):
                wkf = True
        elif a == "B":
            if lookForB(r,c,e):
                wkf = True
        elif a == "Q":
            if lookForQ(r,c,e):
                wkf = True
        elif a == "K":
            for i in range(-1,2):
                for j in range(-1,2):
                    if isKing(r+i,c+j,e):
                        wkf = True
        elif a == "N":
            if isKing(r+1,c+2,e) or isKing(r+1,c-2,e) or isKing(r-1,c+2,e) or isKing(r-1,c-2,e):
                wkf = True
            if isKing(r+2,c+1,e) or isKing(r+2,c-1,e) or isKing(r-2,c+1,e) or isKing(r-2,c-1,e):
                wkf = True
        if wkf:
            break

    if wkf:
        msg = "while king is in check"
    elif bkf:
        msg = "balck king is in check"
    else:
        msg = "no king is in check"

    print "Game #{0}: {1}".format(idx, msg)
    wkf = bkf = False
    map = []

"""INPUT
..k.....
ppp.pppp
........
.R...B..
........
........
PPPPPPPP
K.......

rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR

rnbqk.nr
ppp..ppp
....p...
...p....
.bPP....
.....N..
PP..PPPP
RNBQKB.R

........
........
........
........
........
........
........
........
"""

"""OUTPUT
Game #1: while king is in check
Game #2: no king is in check
Game #3: balck king is in check
"""


""" BLOG
<h1>[python] 체크 확인(Check the Check)</h1>
<div class='desc'>
소문자는 화이트, 대문자는 블랙이므로, 이를 구별하기 위해 정규표현식을 사용합니다.
</div>
<pre class='brush:py'>
import re
if re.match("[a-z]",text):
    print "소문자"
</pre>

<h3>해당하는 자리가 원하는 말이 있는지 확인하는 함수</h3>
<pre class='brush:python'>
def isKing(r,c,e):
    if r > 0 and r  < 8 and c > 0 and c < 8 and map[r][c] == e :
        return True
    else:
        return False
</pre>

<h3>변화값을 사용하여 이어지는 줄에 원하는 말이 있는지 확인하는 함수</h3>
<div class='desc'>
dr, dc 값을 이용하여, 계속해서, r,c 값을 변경하여 확인합니다.
</div>
<pre class='brush:python'>
def lookFor(r,c,dr,dc,e):
    while True:
        r += dr
        c += dc
        if r < 0 or r >= 8 or c < 0 or c>= 8:
            return False
        if map[r][c] == e:
            return True
        if map[r][c] != ".":
            return False
    return False
</pre>

<h3>각 말마다 다른 방향을 갖도록 설정하여 말을 확인합니다.</h3>
<pre class='brush:python'>
def lookForR(r,c,e):
    if lookFor(r,c,1,0,e) or lookFor(r,c,-1,0,e) or lookFor(r,c,0,1,e) or lookFor(r,c,0,-1,e):
        return True
    else:
        return False

def lookForB(r,c,e):
    if lookFor(r,c,1,1,e) or lookFor(r,c,1,-1,e) or lookFor(r,c,-1,1,e) or lookFor(r,c,-1,-1,e):
        return True
    else:
        return False

def lookForQ(r,c,e):
    if lookFor(r,c,1,1,e) or lookFor(r,c,1,-1,e) or lookFor(r,c,-1,1,e) or lookFor(r,c,-1,-1,e) or lookFor(r,c,1,0,e) or lookFor(r,c,-1,0,e) or lookFor(r,c,0,1,e) or lookFor(r,c,0,-1,e):
        return True
    else:
        return False
</pre>

<h3>전체소스</h3>
<pre class='brush:python'>
# -*- coding: utf-8 -*-
import re

def isKing(r,c,e):
    if r > 0 and r  < 8 and c > 0 and c < 8 and map[r][c] == e :
        return True
    else:
        return False

def lookFor(r,c,dr,dc,e):
    while True:
        r += dr
        c += dc
        if r < 0 or r >= 8 or c < 0 or c>= 8:
            return False
        if map[r][c] == e:
            return True
        if map[r][c] != ".":
            return False
    return False

def lookForR(r,c,e):
    if lookFor(r,c,1,0,e) or lookFor(r,c,-1,0,e) or lookFor(r,c,0,1,e) or lookFor(r,c,0,-1,e):
        return True
    else:
        return False

def lookForB(r,c,e):
    if lookFor(r,c,1,1,e) or lookFor(r,c,1,-1,e) or lookFor(r,c,-1,1,e) or lookFor(r,c,-1,-1,e):
        return True
    else:
        return False

def lookForQ(r,c,e):
    if lookFor(r,c,1,1,e) or lookFor(r,c,1,-1,e) or lookFor(r,c,-1,1,e) or lookFor(r,c,-1,-1,e) or lookFor(r,c,1,0,e) or lookFor(r,c,-1,0,e) or lookFor(r,c,0,1,e) or lookFor(r,c,0,-1,e):
        return True
    else:
        return False



file = 'p007.CheckTheCheck.in'
f = open(file, 'r')

whites = []
blacks = []
map = []
emptyMap = []
emptyMap = [["." for i in xrange(8)] for i in xrange(8)]
idx = 0
while True:
    line = list(f.readline().strip())
    if line:
        map.append(line)
        continue
    if map == emptyMap:
        break
    idx += 1
    for r in range(len(map)):
        for c in range(len(map[r])):
            a = map[r][c]
            if re.match("[a-z]", a):
                whites.append((r,c,a))
            else:
                blacks.append((r,c,a))
    # 각 말을 확인해야 함
    bkf = False
    wkf = False
    for w in whites:
        e = "K"
        r = w[0]
        c = w[1]
        a = w[2]
        if a == "p":
            if isKing(r+1,c-1,e):
                bkf = True
            if isKing(r+1,c+1,e):
                bkf = True
        elif a == "r":
            if lookForR(r,c,e):
                bkf = True
        elif a == "b":
            if lookForB(r,c,e):
                bkf = True
        elif a == "q":
            if lookForQ(r,c,e):
                bkf = True
        elif a == "k":
            for i in range(-1,2):
                for j in range(-1,2):
                    if isKing(r+i,c+j,e):
                        bkf = True
        elif a == "n":
            if isKing(r+1,c+2,e) or isKing(r+1,c-2,e) or isKing(r-1,c+2,e) or isKing(r-1,c-2,e):
                bkf = True
            if isKing(r+2,c+1,e) or isKing(r+2,c-1,e) or isKing(r-2,c+1,e) or isKing(r-2,c-1,e):
                bkf = True
        if bkf:
            break

    for b in blacks:
        e = "k"
        r = b[0]
        c = b[1]
        a = b[2]
        if a == "P":
            if isKing(r+1,c-1,e):
                wkf = True
            if isKing(r+1,c+1,e):
                wkf = True
        elif a == "R":
            if lookForR(r,c,e):
                wkf = True
        elif a == "B":
            if lookForB(r,c,e):
                wkf = True
        elif a == "Q":
            if lookForQ(r,c,e):
                wkf = True
        elif a == "K":
            for i in range(-1,2):
                for j in range(-1,2):
                    if isKing(r+i,c+j,e):
                        wkf = True
        elif a == "N":
            if isKing(r+1,c+2,e) or isKing(r+1,c-2,e) or isKing(r-1,c+2,e) or isKing(r-1,c-2,e):
                wkf = True
            if isKing(r+2,c+1,e) or isKing(r+2,c-1,e) or isKing(r-2,c+1,e) or isKing(r-2,c-1,e):
                wkf = True
        if wkf:
            break

    if wkf:
        msg = "while king is in check"
    elif bkf:
        msg = "balck king is in check"
    else:
        msg = "no king is in check"

    print "Game #{0}: {1}".format(idx, msg)
    wkf = bkf = False
    map = []

"""INPUT
..k.....
ppp.pppp
........
.R...B..
........
........
PPPPPPPP
K.......

rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR

rnbqk.nr
ppp..ppp
....p...
...p....
.bPP....
.....N..
PP..PPPP
RNBQKB.R

........
........
........
........
........
........
........
........
"""

"""OUTPUT
Game #1: while king is in check
Game #2: no king is in check
Game #3: balck king is in check
"""
</pre>


"""