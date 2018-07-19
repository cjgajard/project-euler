from math import sqrt
from math import log
from time import time
from fractions import gcd


def maxpower(a):
    global n
    res = int(log(n) / log(a))
    if pow(a, res + 1) <= n:
        res += 1
    if pow(a, res) > n:
        res -= 1
    return res


def lcm(a, b):
    a /= gcd(a, b)
    return a * b


def recurse(lc, index, sign, left, right, thelist):
    if lc > right:
        return 0
    res = sign * (right / lc - (left - 1) / lc)
    for i in xrange(index + 1, len(thelist)):
        res += recurse(lcm(lc, thelist[i]), i, -sign, left, right, thelist)
    return res


def dd(left, right, a, b):
    res = right / b - (left - 1) / b
    thelist = []
    for i in xrange(a, b):
        if check[i]:
            thelist.append(i)
    for i in xrange(len(thelist)):
        res -= recurse(lcm(b, thelist[i]), i, 1, left, right, thelist)
    return res


thetime = time()
n = pow(10, 6)
sqn = int(sqrt(n))
used = [False] * (sqn + 1)
maxc = maxpower(2)
counts = [0] * (maxc + 1)
counts[1] = n - 1

for c in xrange(2, maxc + 1):
    check = [True] * (maxc + 1)
    umin = (c - 1) * n + 1
    umax = c * n
    for i in xrange(c, maxc / 2 + 1):
        u = 2 * i
        while u <= maxc:
            check[u] = False
            u += i
    for f in xrange(c, maxc + 1):
        if check[f]:
            counts[f] += dd(umin, umax, c, f)

for c in xrange(2, maxc + 1):
    counts[c] += counts[c - 1]

ans = 0
coll = 0
for i in xrange(2, sqn+1):
    if not used[i]:
        c = maxpower(i)
        ans += counts[c]
        u = i
        for j in xrange(2, c + 1):
            u *= i
            if u <= sqn:
                used[u] = True
            else:
                coll += c - j + 1
                break
ans += (n - sqn) * (n - 1)
ans -= coll * (n - 1)
print n, ans, time() - thetime
