import sys
sys.setrecursionlimit(10**7)
H,W=map(int,input().split())
mat=[]
ans=0
for _ in range(H):
    mat.append(list(input()))

def sround_cell(h,w):
    ret=set()
    #hwの周りで#のものを返す(まだ見ていない)
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            tmph = max(h+i,0)
            tmpw = max(w+j,0)

            tmph = min(H-1,tmph)
            tmpw = min(W-1,tmpw)

            if (tmph,tmpw) == (h,w):
                continue
            elif mat[tmph][tmpw] == '#':
                ret.add((tmph,tmpw))
    return ret

#(h,w)と同期するセンサーを探して、#から.にする この点は.になっているはず
def search_same_sens(h,w):
    # if mat[h][w] != "#": print(f"ERROR{(h,w)}")
    sround = sround_cell(h,w)
    mat[h][w] = "."
    if len(sround) == 0: return
    for cell in sround:
        search_same_sens(cell[0], cell[1])

for i in range(H):
    for j in range(W):
        if mat[i][j] == '#':
            ans += 1
            search_same_sens(i,j)

print(ans)