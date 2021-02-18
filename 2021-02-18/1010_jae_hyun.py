"code by jae_hyun, cachi"

memo = [[0 for _ in range(31)] for _ in range(31)]


def combin(n, r):
    "calculating combination"
    if memo[n][r]:
        return memo[n][r]
    
    return combin(n-1, r - 1) + combin(n-1, r)


if __name__ == '__main__':
    for i in range(int(input())):
        n, m = map(int, input().split())
        print(combin(m, n))
     