N,M=map(int,input().split())
S=[]
for i in range(N):
    S.append(list(input()))
    

# import numpy as np
# count=np.zeros((N,M))
    
count=[[0]*M for _ in range(N)]
    

iru=[(1,1)]
old=set((1,1))
while len(iru) != 0:
    for i,now in enumerate(iru):
        old.add(now)
        for ue in reversed(range(0,now[0])):
            i=ue
            j=now[1]
            if S[i][j] == "#":
                if not ((i+1,j) in old):
                    iru.append((i+1,j))
                break
            if S[i][j] == ".":
                count[i][j]=1
        for sita in range(now[0]+1,N):
            i=sita
            j=now[1]
            if S[i][j] == "#":
                if not ((i-1,j) in old):
                    iru.append((i-1,j))
                break
            if S[i][j] == ".":
                count[i][j]=1
        for migi in range(now[1]+1,M):
            i=now[0]
            j=migi
            if S[i][j] == "#":
                if not ((i,j-1) in old):
                    iru.append((i,j-1))
                break
            if S[i][j] == ".":
                count[i][j]=1
        for hidari in reversed(range(0,now[1])):
            i=now[0]
            j=hidari
            if S[i][j] == "#":
                if not ((i,j+1) in old):
                    iru.append((i,j+1))
                break
            if S[i][j] == ".":
                count[i][j]=1
        iru.remove(now)
# print(int(count.sum()))
ANS=0
for i in range(N):
    ANS+=sum(count[i])
 
print(ANS)