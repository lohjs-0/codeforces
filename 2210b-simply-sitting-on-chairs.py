import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    pos = [0] * (n + 2)
    for i in range(1, n + 1):
        pos[p[i-1]] = i
    L = R = best = 0
    for k in range(1, n + 2):
        best = max(best, L + R)
        if k <= n:
            pi = p[k-1]
            if pi <= k: L += 1
            else: R += 1
            if pos[k] < k: R -= 1
    print(best)

for _ in range(int(input())):
    solve()