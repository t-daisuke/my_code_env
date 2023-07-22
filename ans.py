N, M = map(int, input().split())
S = [[c for c in input()] for _ in range(N)]
dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

visited = [[0]*M for _ in range(N)]
visited[1][1] = 1
cie=set()
cie.add((1,1))
stop=[(1,1)]

while stop:
    y, x = stop.pop()
    for dy, dx in dxdy:
        ty,tx=y,x
        while S[ty+dy][tx+dx] =='.':
            ty+=dy
            tx+=dx
            visited[ty][tx]=1       
        if (ty, tx) not in cie:
            cie.add((ty, tx))
            stop.append((ty, tx))

print(sum(sum(row) for row in visited))
