N = int(input())
dimensions = []

# 행렬 차원 정보를 dimensions 배열에 저장
for _ in range(N):
    x, y = map(int, input().split())
    if len(dimensions) == 0:
        dimensions.append(x)  # 첫 번째 행렬의 행
    dimensions.append(y)  # 행렬의 열

# DP 테이블을 무한대로 초기화
dp = [[float('inf')] * N for _ in range(N)]

# 대각선의 길이
for length in range(1, N):
    for i in range(N - length):
        j = i + length
        if i == j:
            dp[i][j] = 0
        else:
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1])

print(dp[0][N - 1])
