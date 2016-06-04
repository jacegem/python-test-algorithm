file = 'p002.Minesweeper.in'
f = open(file, 'r')

def getCount(map, r, c, h, w):
    cnt = 0

    for rowOffset in range(-1,2):
        for colOffset in range(-1,2):
            if rowOffset == 0 and colOffset == 0:
                continue
            row = r + rowOffset
            col = c + colOffset
            if row < 0 or row > h-1 or col <0 or col > w-1:
                continue
            if map[row][col] == '*':
                cnt += 1
    return cnt


idx = 0
while 1:
    line = f.readline().strip()
    #print 'line is ' + line
    if line == '0 0':
        break

    idx += 1
    map = []
    h, w = [int(x) for x in line.split()]

    for row in xrange(h):
        line = f.readline().strip()
        map.append(list(line))

    print "Field #{0}".format(idx)
    for r in xrange(h):
        pRow = ""
        for c in xrange(w):
            if map[r][c] == '*':
                cnt = '*'
            else:
                cnt = getCount(map, r, c, h, w)
            pRow += str(cnt)
        print pRow

    print

"""
with line as f.readline():
    h, w = [int(x) for x in line.split()]
    #map = [['.' for i in range(h)] for j in range(w)]

    for row in range(h):
        line = f.readline()
        map[row] = [x for x in line.split()]

    print map
"""



