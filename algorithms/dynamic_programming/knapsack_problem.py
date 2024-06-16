def knapsack(weights, values, max_weight):
    n = len(values)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n)]
    for i in range(n):
        for w in range(1, max_weight + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n-1][max_weight],dp
if __name__ == "__main__":
    weights = [3,1,2,2,1]
    values = [10,3,9,5,6]
    max_weight = 6

    max_value,dp = knapsack(weights,values,max_weight)
    for line in dp:
        print(line)
    print(f"Max value: {max_value}")