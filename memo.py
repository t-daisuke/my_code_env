#nCk
def comb(n,k):
    ans=1
    for i in range(k):
        ans*=n-i
        ans//=i+1
    return ans

#素因数分解
for i in range(2,10**6):
    #最大の素因数は平方根以上にならない
    #これ以上Nを割ることができない
    if i**2>N:break
    if N%i==0:
        npow=0#iの指数
        #iは素因数
        while N%i==0:
            N//=i
            npow+=1
        #Nは素因数i**npowで割り切った
        # ans *= comb(npow+M-1,min(M-1,npow))
        # ans %= mod
if N>1:
    #Nが指数部１の素数
    #この素数p以外でans通りなのだから、一つの素数pがmこの場所のどこかに入る
    #つまりm通り
    # ans = ans*M%mod