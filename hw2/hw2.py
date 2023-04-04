import math

def bermudan_option_price(S, K, r, s, T, n):
    dt = T / n
    u = math.exp(s * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)
    early_exercise_times = [T/4, 3/4*T]
    
    # Initialize the binomial tree
    tree = [[0.0] * (i+1) for i in range(n+1)]
    
    # Compute the stock price at each node
    for i in range(n+1):
        for j in range(i+1):
            tree[i][j] = S * (u ** (i-j)) * (d ** j)
    
    # Compute the option value at maturity
    for j in range(n+1):
        tree[n][j] = max(K - tree[n][j] + 1, 0)
    
    # Compute the option value at each time step
    for i in range(n-1, -1, -1):
        # Compute the option value at the early exercise times
        if (i*dt) in early_exercise_times:
            for j in range(i+1):
                tree[i][j] = max(K - tree[i][j] + 1, tree[i+1][j]*p + tree[i+1][j+1]*(1-p))
        else:
            for j in range(i+1):
                tree[i][j] = math.exp(-r*dt) * (p*tree[i+1][j] + (1-p)*tree[i+1][j+1])
    
    # Return the option price
    return tree[0][0]

# Example usage
""" 
S = 100
K = 100
r = 0.05  # 5%
s = 0.30  # 30%
T = 0.5
n = 100 
"""
S = int(input( '請輸入 股票價格S:' ))
K = int(input( '請輸入 執行價格K:' ))
r = int(input( '請輸入 連續複利年利率r (例如利率為 5%，輸入值為 5):' )) / 100  # 5%
s = int(input( '請輸入 年度波動率s (例如波動率為 30%，輸入值為 30):' )) / 100 # 30%
T = float(input( '請輸入 到期時間年T:' ))
n = int(input( '請輸入 時間步數n:' ))
price = bermudan_option_price(S, K, r, s, T, n)
print("Option price at n = {}: {:.4f}".format(n, price))

""" 
n = 200
price = bermudan_option_price(S, K, r, s, T, n)
print("Option price at n = {}: {:.4f}".format(n, price))
 """