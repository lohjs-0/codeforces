import sys
input = sys.stdin.readline

N = 1_500_000
sieve = bytearray([1]) * (N + 1)
sieve[0] = sieve[1] = 0
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [i for i in range(2, N + 1) if sieve[i]]
del sieve

def solve():
    n = int(input())
    print(*[primes[i] * primes[i+1] for i in range(n)])

for _ in range(int(input())):
    solve()