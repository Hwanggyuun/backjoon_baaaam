
N = int(input())
hang = [] 

dp = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    x,y = map(int, input().split())
    if i == 0:
        hang.append(x) 
    hang.append(y)
for len in range(1,N):
    for i in range(N-len):
        j= i +len
        if i ==j:
            dp[i][j] = 0
        else:
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + hang[i] * hang[k + 1] * hang[j + 1])
print(dp[0][N-1])