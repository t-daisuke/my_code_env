def sendable(t,s):
    if (len(t) - len(s)) not in [-1, 0, 1]:
        return False
    ti = 0
    si = 0
    count = 0
    while (ti != len(t)) and (si != len(s)):
        print((ti, si))
        if t[ti] == s[si]:
            ti += 1
            si += 1
            print("Match")
            continue
        else:
            count += 1
            if count == 2:
                return False
            if (ti == len(t)-1):
                if (si == len(s)-1):
                    return True
                elif t[ti] == s[si+1]:
                    return True
                else:
                    return False
            elif (si == len(s)-1):
                if t[ti+1] == s[si]:
                    return True
                else:
                    False
            else:
                if t[ti+1] == s[si+1]:
                    ti += 1
                    si += 1
                    #change
                    continue
                elif t[ti+1] == s[si]:
                    ti += 1
                    #delete
                    continue
                elif t[ti] == s[si+1]:
                    si += 1
                    #add
                    continue
                else:
                    return False
    return True

import sys
input = lambda: sys.stdin.readline().rstrip()
one_raw=input().split()
N=int(one_raw[0])
t=one_raw[1]
sl=[]
for _ in range(N):
    sl.append(input())

ans=[]
for i in range(N):
    tmp = sendable(t, sl[i])
    if tmp == True:
        ans.append(i+1)

def print_numbers_with_hash_separator(numbers):
    output = ' '.join(map(str, numbers))
    print(output)

print(len(ans))
if len(ans) == 0:
    print()
else:
    print_numbers_with_hash_separator(ans)