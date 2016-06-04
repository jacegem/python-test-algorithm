file = 'p003.TheTrip.in'
f = open(file, 'r')

def getInt(f):
    return int(f.readline().strip())
def getFloat(f):
    return float(f.readline().strip())

while 1:
    num = getInt(f)
    if num == 0:
        break
    fees = []
    sum = 0
    for i in xrange(num):
        fee = getFloat(f)
        fees.append(fee)
        sum += fee
    avg = round(sum / num, 2)
    trans = 0
    for fee in fees:
        if (avg > fee):
            trans += (avg - fee)
    print "${0}".format(trans)

"""
3
10.00
20.00
30.00
4
15.00
15.01
3.00
3.01
0
"""