import sys
input = lambda: sys.stdin.readline().rstrip()

N,X,Y=map(int,input().split())
ptl=[]
p_set=set()
for _ in range(N-1):
    tmp=[int(i) for i in input().split()]
    ptl.append(tmp)
    p_set.add(tmp[0])
Q=int(input())
q_list=[]
for _ in range(Q):
    q_list.append(int(input()))
    
##LCM
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_set(numbers_set):
    result = 1
    for num in numbers_set:
        result = lcm(result, num)
    return result

lcm_p=lcm_set(p_set)

#lcm_p作成
pass_time=[]
for start in range(lcm_p):
    c=""
    time = start + X
    for pt in ptl:
        syou = time%pt[0]
        if syou == 0:
            time += pt[1]
        else:
            time += pt[1] + (pt[0]-syou)
    time+=Y
    pass_time.append(time-start)

for q in q_list:
    qtime=pass_time[q%lcm_p]+q
    print(qtime)
