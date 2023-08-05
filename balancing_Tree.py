class BalancingTree:
    # https://qiita.com/Kiri8128/items/6256f8559f0026485d90
    def __init__(self, n, ibl = 0):
        self.N = n
        if 1:
            self.S = {1<<n} # <-- 存在チェックをしないならいらない
        self.identifying_bit_length = ibl
        self.root = self.node(1<<n, 1<<n, ibl, 0)

    def add(self, v): # v を追加（既に存在する場合はなにもしない）
        v += 1
        # 存在する元を追加しないことが分かっている場合はこの確認は不要
        ### ここから
        if 1:
            if v in self.S:
                return 0 
            self.S.add(v)
        ### ここまで
        nd = self.root
        while True:
            nd.size += 1
            nd.sum += v - 1 >> self.identifying_bit_length
            if v == nd.value:
                #####
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2, self.identifying_bit_length)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2, self.identifying_bit_length)
                        break

    def leftmost(self, nd):
        while nd.left:
            nd = nd.left
        return nd

    def rightmost(self, nd):
        while nd.right:
            nd = nd.right
        return nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1<<self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)
    
    @property
    def sum(self):
        return self.root.sum

    def delete(self, v, nd = None, prev = None, chk = 0): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        ### ここから
        if 1:
            if not chk:
                if v not in self.S: return 0
                self.S.remove(v)
        ### ここまで
        if not nd: nd = self.root
        if not prev: prev = nd
        while 1:
            while v != nd.value:
                nd.size -= 1
                nd.sum -= v - 1 >> self.identifying_bit_length
                prev = nd
                if v <= nd.value:
                    if nd.left:
                        nd = nd.left
                    else:
                        #####
                        return
                else:
                    if nd.right:
                        nd = nd.right
                    else:
                        #####
                        return
            nd.size -= 1
            nd.sum -= v - 1 >> self.identifying_bit_length

            if (not nd.left) and (not nd.right):
                if not prev.left:
                    prev.right = None
                elif not prev.right:
                    prev.left = None
                else:
                    if nd.pivot == prev.left.pivot:
                        prev.left = None
                    else:
                        prev.right = None
                break
            elif nd.right:
                nd.value = self.leftmost(nd.right).value
                v, nd, prev = nd.value, nd.right, nd
                continue
            else:
                nd.value = self.rightmost(nd.left).value
                v, nd, prev = nd.value, nd.left, nd
                continue
    
    def count_less_than(self, v):
        v += 1
        re = 0
        nd = self.root
        while 1:
            if nd.value < v:
                re += (nd.left.size if nd.left else 0) + 1
                if nd.right:
                    nd = nd.right
                else:
                    return re
            else:
                if nd.left:
                    nd = nd.left
                else:
                    return re
    def count_not_less_than(self, v):
        return self.root.size - 1 - self.count_less_than(v)
    def sum_of_first_k_elements(self, k, nd = None):
        if not nd:
            if k >= self.root.size - 1:
                return self.root.sum
            if k <= 0:
                return 0
            nd = self.root
        re = 0
        while 1:
            if nd.left:
                l = nd.left.size
                if k < l:
                    nd = nd.left
                elif k > l:
                    re += nd.left.sum + (nd.value - 1 >> self.identifying_bit_length)
                    k -= l + 1
                    nd = nd.right
                else:
                    re += nd.left.sum
                    return re
            else:
                l = 0
                if k > l:
                    re += (nd.value - 1 >> self.identifying_bit_length)
                    k -= l + 1
                    nd = nd.right
                else:
                    return re
    def sum_less_than(self, v):
        v += 1
        re = 0
        nd = self.root
        while 1:
            if nd.value < v:
                re += (nd.left.sum if nd.left else 0) + (nd.value - 1 >> self.identifying_bit_length)
                if nd.right:
                    nd = nd.right
                else:
                    return re
            else:
                if nd.left:
                    nd = nd.left
                else:
                    return re
    def sum_not_less_than(self, v):
        return self.root.sum - 1 - self.sum_less_than(v)
    def kth_smallest(self, k, nd = None):
        if not nd:
            assert 0 <= k < self.root.size - 1
            nd = self.root
        while 1:
            l = nd.left.size if nd.left else 0
            if k < l:
                nd = nd.left
            elif k > l:
                k -= l + 1
                nd = nd.right
            else:
                return nd.value - 1
    def kth_largest(self, k, nd = None):
        if not nd:
            assert 0 <= k < self.root.size - 1
            nd = self.root.left
        while 1:
            r = nd.right.size if nd.right else 0
            if k < r:
                nd = nd.right
            elif k > r:
                k -= r + 1
                nd = nd.left
            else:
                return nd.value - 1
    
    def __getitem__(self, k):
        if type(k) == int:
            if 0 <= k < self.root.size - 1:
                return self.kth_smallest(k)
            if 0 <= ~k < self.root.size - 1:
                return self.kth_largest(~k)
        
        l = k.start
        if l is None:
            l = 0
        elif l < 0:
            l = self.root.size - 1 + l
        r = k.stop
        if r is None:
            r = self.root.size - 1
        if r < 0:
            r = self.root.size - 1 + r
        if l >= r:
            return 0
        return self.sum_of_first_k_elements(r) - (self.sum_of_first_k_elements(l) if l else 0)
    
    def __contains__(self, v: int) -> bool:
        return v + 1 in self.S

    class node:
        def __init__(self, v, p, identifying_bit_length, s = None):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None
            self.size = 1
            if s is None:
                s = v - 1 >> identifying_bit_length
            self.sum = s

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.sum, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1, nd_.size)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(nd.value - 1)
            if nd.right:
                re += debug_node(nd.right)
            return re
        return debug_node(self.root)[:-1]

####################
import sys
input = lambda: sys.stdin.readline().rstrip()
K = 20
bt = BalancingTree(30 + K, K)
N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    t, x = map(int, input().split())
    if t == 0:
        bt.add((x << K) + i)
    elif t == 1:
        A.append((x << K) + i)
    else:
        B.append(x)
A.sort()
B.sort()
ans = 0
while M > 0:
    print("ans, bt[-M:]")
    print(ans, bt[-M:])
    ans = max(ans, bt[-M:])
    if not A or not B:
        break
    for _ in range(B.pop()):
        if not A:
            break
        bt.add(A.pop())
    M -= 1
print(ans)
print([ bin(i) for i in bt.debug_list()])
# BT = BalancingTree(5) # 0 ～ 30 までの要素を入れられるピボット木
# BT.add(3)
# BT.add(20)
# BT.add(5)
# BT.add(10)
# BT.add(13)
# BT.add(8)
# BT.debug()
# BT.delete(20)
# BT.debug()
# print(BT.find_l(12)) # 10
# print(BT.find_r(5)) # 8
# print(BT.min) # 3
# print(BT.max) # 13
# print(3 in BT) # True
# print(4 in BT) # False
# BT.debug_list()

# # 愚直チェック
# from random import randrange
# BT = BalancingTree(5) # 0 ～ 30 までの要素を入れられるピボット木
# S = set()
# for _ in range(1000):
#     a = randrange(31)
#     if randrange(2) == 0:
#         BT.add(a)
#         S.add(a)

#     else:
#         BT.delete(a)
#         if a in S: S.remove(a)
#     if BT.debug_list() != sorted(list(S)):
#         print("NG!!")
#     # print(BT.debug_list(), sorted(list(S)))
# print("END")