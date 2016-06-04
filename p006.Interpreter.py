# -*- coding: utf-8 -*-

def reduce(idx):
    r[idx] = r[idx] % 1000

file = 'p006.Interpreter.in'
f = open(file, 'r')

case = int(f.readline())
f.readline() # 빈줄 읽기

r = [0 for i in range(10)]
ram = [0 for i in range(1000)]
cmds = []

while True:
    line = f.readline().strip()
    if not line:
        break
    cmds.append(line)

idx = 0
cnt = 0
while True:
    cnt += 1
    #print "idx:#{0} \tcnt:#{1}".format(idx,cnt)
    cmd = cmds[idx]

    codes = list(cmd)
    cmd = int(codes[0])
    d = int(codes[1])
    n = s = a = int(codes[2])
    if cmd == 1:
        break
    elif cmd  == 2:
        r[d] = n
    elif cmd == 3:
        r[d] += n
    elif cmd == 4:
        r[d] *= n
    elif cmd == 5:
        r[d] = r[s]
    elif cmd == 6:
        r[d] += r[s]
    elif cmd == 7:
        r[d] *= r[s]
    elif cmd == 8:
        r[d] = ram[r[s]]
    elif cmd == 9:
        ram[r[a]] = r[s]
    elif cmd == 0:
        if r[s] != 0:
            idx = r[d]
            continue
    reduce(d)
    idx += 1

print cnt

""" INPUT
1

299
492
495
399
492
495
399
283
279
689
078
100
000
000
000
"""

""" OUTPUT
16
"""

""" BLOG
<h1>[python] 인터프리터 (Interperter) - 나머지 연산 </h1>

<h3>파일 읽기</h3>
<pre class='brush:py'>
file = 'p006.Interpreter.in'
f = open(file, 'r')
</pre>

<h3>케이스 수를 출력합니다.</h3>
<pre class='brush:py'>
case = int(f.readline())
print case
</pre>

<h3>빈줄을 읽는 경우에 루프를 종료합니다.</h3>
<div class='desc'>
마지막 줄 바꿈 기호를 제거하기 위해서, .strip()을 사용합니다.
</div>
<pre class='brush:py'>
liㅑne = f.readline().strip()
if not line:
    break
</pre>

<h3>변수를 초기화 합니다. </h3>
<pre class='brush:py'>
r = [0 for i in range(10)]
ram = [0 for i in range(1000)]
</pre>
ㅑ
<div class='desc'>
모든 결과는 값이 1000이 넘어가면 1000으로 나눈 나머지로 줄어든다.
나머지로 변경하는 함수를 만들어서 호출한다. 파라미터는 레지스터의 인덱스.
</div>


<pre class='brush:py'>
def reduce(idx):
    r[idx] = r[idx] % 1000
</pre>






"""