def knapsack_01(value,weight,capacity):
    n=len(value)
    dp=[[0 for _ in range(capacity+1)]for _ in range(n+1)]
    
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weight[i-1]<=w:
                dp[i][w]=max(value[i-1]+dp[i-1][w-weight[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    
    return dp[n][capacity]

n=int(input("Enter the no. of items : "))
values=[]
weights=[]

for i in range(n):
    values.append(int(input(f"Enter the value for item {i+1} : ")))
    weights.append(int(input(f"Enter the weight for item {i+1} : ")))

capacity=int(input("Enter the capacity of knapsack : "))

max_value=knapsack_01(values,weights,capacity)
print(max_value)