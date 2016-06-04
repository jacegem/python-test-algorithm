import re
import sys
import subprocess

numArgs = len(sys.argv)
if numArgs < 3:
    print sys.argv,'cmd','regex','before','after'
    sys.exit(2)

cmd = sys.argv[1]
regex = sys.argv[2]
before = numArgs > 3 and int(sys.argv[3]) or 0
after = numArgs > 4 and int(sys.argv[3]) or 0


p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

arr = []
afterline = 0

while True:
    out = p.stdout.readline()
    if not out:
        break

    if afterline > 0:
        print out
        afterline -= 1
        pass

    arr.append(out)

    if re.match(regex, out):
        print "##MATCH##"

        if before > 0:
            start = len(arr) - before - 1
            if start < 0:
                start = 0
            for i in range(start, len(arr)):
                print arr[i]
            afterline = after
        else:
            print out

        arr=[]









