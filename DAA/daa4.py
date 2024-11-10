#Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy

def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):  # Traverse each item
        for w in range(1, capacity + 1):  # Traverse each weight from 0 to capacity
            if weights[i - 1] <= w:  # Check if item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # Otherwise, item can't be included
                dp[i][w] = dp[i - 1][w]
    
    max_value = dp[n][capacity]
    
    items_included = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_included.append(i - 1)  # Include this item
            w -= weights[i - 1]
    
    items_included.reverse()
    return max_value, items_included

# Example usage
weights = []
values = []
n=int(input("Enter number of values: "))
for i in range(n):
    w=int(input("Enter weight: "))
    v=int(input("Enter value: "))
    weights.append(w)
    values.append(v)
print(weights)
print(values)
capacity = int(input("Enter the capacity: "))
max_value, items_included = knapsack_dynamic_programming(weights, values, capacity)

print("Maximum value:", max_value)
print("Items included (0-indexed):", items_included)