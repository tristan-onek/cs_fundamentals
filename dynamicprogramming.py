# Dynamic Programming Fundamentals Demo

print("Dynamic Programming Fundamentals\n")

# 1. Fibonacci Sequence (Top-down with Memoization)
print("1. Fibonacci Sequence (Top-down with Memoization)")

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = 10
fib_result = fibonacci(n)
print(f"Fibonacci({n}):", fib_result)  # Output: 55
print("Memo table:", fibonacci.__defaults__[0])  # Show memoization table

# 2. Fibonacci Sequence (Bottom-up with Tabulation)
print("\n2. Fibonacci Sequence (Bottom-up with Tabulation)")

def fibonacci_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

fib_result_tab = fibonacci_tabulation(n)
print(f"Fibonacci({n}):", fib_result_tab)  # Output: 55

# 3. Longest Common Subsequence (LCS)
print("\n3. Longest Common Subsequence (LCS)")

def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
lcs_length = longest_common_subsequence(X, Y)
print(f"LCS length of '{X}' and '{Y}':", lcs_length)  # Output: 4

# 4. 0/1 Knapsack Problem
print("\n4. 0/1 Knapsack Problem")

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value = knapsack(values, weights, capacity)
print(f"Max value with capacity {capacity}:", max_value)  # Output: 220

# 5. Minimum Edit Distance (Levenshtein Distance)
print("\n5. Minimum Edit Distance")

def min_edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Insert all characters
            elif j == 0:
                dp[i][j] = i  # Delete all characters
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  # Insert, delete, replace
    return dp[m][n]

word1 = "kitten"
word2 = "sitting"
edit_distance = min_edit_distance(word1, word2)
print(f"Edit distance between '{word1}' and '{word2}':", edit_distance)  # Output: 3

# 6. Subset Sum Problem
print("\n6. Subset Sum Problem")

def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]

nums = [3, 34, 4, 12, 5, 2]
target = 9
is_possible = subset_sum(nums, target)
print(f"Is subset with sum {target} possible:", is_possible)  # Output: True

# 7. Matrix Chain Multiplication
print("\n7. Matrix Chain Multiplication")

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    for chain_len in range(2, n + 1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]

dims = [1, 2, 3, 4]
min_cost = matrix_chain_order(dims)
print(f"Minimum cost of multiplying matrices with dimensions {dims}:", min_cost)  # Output: 18

# 8. Coin Change Problem (Fewest Coins)
print("\n8. Coin Change Problem")

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 11
min_coins = coin_change(coins, amount)
print(f"Fewest coins to make {amount} with {coins}:", min_coins)  # Output: 3