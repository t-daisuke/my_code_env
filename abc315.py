N=int(input())
P=[]
for _ in range(N):
    tmp=[int(i) for i in input().split()]
    P.append(tmp[1:])

set_yonda=set()

def yomu(index):
    global set_yonda
    if index in set_yonda:
        return
    while len(P[index-1]) != 0:
        i = P[index-1].pop()
        yomu(i)

    if len(P[index-1]) == 0 and index not in set_yonda:
        if index != 1:
            print(index)
        set_yonda.add(index)
        return
yomu(1)