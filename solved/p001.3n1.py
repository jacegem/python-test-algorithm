__author__ = 'Administrator'


file = 'p001.3n1.in'
f = open(file, 'r')

for line in f:
    s, e = [int(x) for x in line.split()]
    maxCnt = 0;

    for n in range(s,e+1):
        m = n
        cnt = 1

        while m != 1:
            if (m%2 ==0):
                m = m /2
            else:
                m = m *3 +1
            cnt+=1

        if cnt > maxCnt:
            maxCnt = cnt

    print s,e,maxCnt

f.close()