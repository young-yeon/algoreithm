"code by cachi"

memo = [[0 for _ in range(31)] for _ in range(31)]


def combi(n, r):
    "calculating combination"
    if memo[n][r] != 0:
        return memo[n][r]
    if n == r or r == 0:
        return 1
    memo[n][r] = combi(n-1, r-1) + combi(n-1, r)
    return memo[n][r]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(combi(M, N))

