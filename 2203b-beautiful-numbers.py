import sys
input = sys.stdin.readline

def solve():
    x = input().strip()
    S = sum(int(c) for c in x)
    if S <= 9:
        print(0)
        return
    cuts = sorted([int(c) - (1 if i == 0 else 0) for i, c in enumerate(x)], reverse=True)
    moves = 0
    for r in cuts:
        if S <= 9:
            break
        S -= r
        moves += 1
    print(moves)

for _ in range(int(input())):
    solve()