import sys
input = sys.stdin.readline

N,M=map(int,input().split())

MAP=[input().strip() for i in range(N)]
OK=[[0]*M for i in range(N)]
USED=[[0]*M for i in range(N)]

Q=[(1,1)]
OK[1][1]=1
USED[1][1]=1

while Q:
    x,y=Q.pop()

    z,w=x,y
    for i in range(300):
        if MAP[z+1][w]==".":
            z+=1
            OK[z][w]=1
        else:
            break
    if USED[z][w]==0:
        USED[z][w]=1
        Q.append((z,w))

    z,w=x,y
    for i in range(300):
        if MAP[z-1][w]==".":
            z-=1
            OK[z][w]=1
        else:
            break
    if USED[z][w]==0:
        USED[z][w]=1
        Q.append((z,w))

    z,w=x,y
    for i in range(300):
        if MAP[z][w+1]==".":
            w+=1
            OK[z][w]=1
        else:
            break
    if USED[z][w]==0:
        USED[z][w]=1
        Q.append((z,w))

    z,w=x,y
    for i in range(300):
        if MAP[z][w-1]==".":
            w-=1
            OK[z][w]=1
        else:
            break
    if USED[z][w]==0:
        USED[z][w]=1
        Q.append((z,w))


ANS=0
for i in range(N):
    ANS+=sum(OK[i])

print(ANS)