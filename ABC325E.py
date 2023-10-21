import numpy as np
n,a,b,c=map(int,input().split())
mat=[]
route=[]
for _ in range(n):
    mat.append([int(i) for i in input().split()])
    if _ == 0:
        for i in range(n):
            route.append([mat[0][i]*a, mat[0][i]*b + c])

list=np.argsort(mat[0])
print(list)

for i in list:
    if i == 0:
        continue
    for j in range(1,n):
        tmpl=[]
        tmpl.append(route[i][0])
        tmpl.append(route[i][1])
        tmpl.append(route[j][0] + mat[j][i]*a)
        tmpl.append(route[j][0] + mat[j][i]*b+c)
        tmpl.append(route[j][1] + mat[j][i]*b+c)
        tmp_den=min(tmpl)

        tmp_w=min(route[i][0], route[j][0] + mat[j][i]*a)
    route[i][0] = tmp_w
    route[i][1] = tmp_den
    # print(route)
print(min(route[n-1]))
