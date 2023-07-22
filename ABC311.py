# N,M=map(int,input().split())
# S=[]
# for i in range(N):
#     S.append(list(input()))
    

# # import numpy as np
# # count=np.zeros((N,M))
    
# count=[[0]*M for _ in range(N)]
    

# iru=[(1,1)]
# old=set((1,1))
# while len(iru) != 0:
#     for i,now in enumerate(iru):
#         old.add(now)
#         for ue in reversed(range(0,now[0])):
#             i=ue
#             j=now[1]
#             if S[i][j] == "#":
#                 if not ((i+1,j) in old):
#                     iru.append((i+1,j))
#                 break
#             if S[i][j] == ".":
#                 count[i][j]=1
#         for sita in range(now[0]+1,N):
#             i=sita
#             j=now[1]
#             if S[i][j] == "#":
#                 if not ((i-1,j) in old):
#                     iru.append((i-1,j))
#                 break
#             if S[i][j] == ".":
#                 count[i][j]=1
#         for migi in range(now[1]+1,M):
#             i=now[0]
#             j=migi
#             if S[i][j] == "#":
#                 if not ((i,j-1) in old):
#                     iru.append((i,j-1))
#                 break
#             if S[i][j] == ".":
#                 count[i][j]=1
#         for hidari in reversed(range(0,now[1])):
#             i=now[0]
#             j=hidari
#             if S[i][j] == "#":
#                 if not ((i,j+1) in old):
#                     iru.append((i,j+1))
#                 break
#             if S[i][j] == ".":
#                 count[i][j]=1
#         iru.remove(now)
# # print(int(count.sum()))
# ANS=0
# for i in range(N):
#     ANS+=sum(count[i])
 
# print(ANS)

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
