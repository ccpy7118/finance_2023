# import numpy as np

# def american_put_price(S, K, r, s, T, n, N):
#     dt = T / n
#     discount_factor = np.exp(-r * dt)
    
#     # Generate stock price paths
#     paths = generate_stock_paths(S, r, s, T, n, N)
    
#     # Initialize option value matrix
#     option_values = np.maximum(K - paths[:, -1], 0)
    
#     # Perform LSM algorithm
#     for t in range(n-1, 0, -1):
#         continuation_values = discount_factor * option_values[t]
#         exercise_values = np.maximum(K - paths[:, t], 0)
        
#         # Regression to estimate continuation values
#         basis_functions = np.column_stack((np.ones(N), paths[:, t], paths[:, t]**2, paths[:, t]**3))
#         coefficients = np.linalg.lstsq(basis_functions, continuation_values, rcond=None)[0]
#         estimated_continuation_values = np.dot(basis_functions, coefficients)
        
#         # Determine optimal exercise strategy
#         optimal_exercise = exercise_values > estimated_continuation_values
#         option_values = np.where(optimal_exercise, exercise_values, option_values)
    
#     # Calculate option price
#     option_price = np.mean(option_values) * discount_factor
    
#     # Calculate standard error
#     standard_error = np.std(option_values) / np.sqrt(N)
    
#     return option_price, standard_error





import numpy as np


def american_put_price(S, K, r, s, T, n, N):
    dt = T / n
    discount_factor = np.exp(-r * dt / 100)  # Convert interest rate to decimal
    
    # Generate stock price paths
    paths = generate_stock_paths(S, r, s, T, n, N)
    
    # Initialize option value matrix
    option_values = np.maximum(K - paths[:, -1], 0)
    
    # Perform LSM algorithm
    for t in range(n-1, 0, -1):
        continuation_values = discount_factor * option_values
        exercise_values = np.maximum(K - paths[:, t], 0)
        
        # Regression to estimate continuation values
        basis_functions = np.column_stack((np.ones(N), paths[:, t], paths[:, t]**2, paths[:, t]**3))
        coefficients = np.linalg.lstsq(basis_functions, continuation_values, rcond=None)[0]
        estimated_continuation_values = np.dot(basis_functions, coefficients)
        
        # Determine optimal exercise strategy
        optimal_exercise = exercise_values > estimated_continuation_values
        option_values = np.where(optimal_exercise, exercise_values, option_values)
    
    # Calculate option price
    option_price = np.mean(option_values) * discount_factor
    
    # Calculate standard error
    standard_error = np.std(option_values) / np.sqrt(N)
    
    return option_price, standard_error

def generate_stock_paths(S, r, s, T, n, N):
    dt = T / n
    drift = (r / 100 - 0.5 * (s / 100)**2) * dt
    volatility = s / 100 * np.sqrt(dt)
    
    paths = np.zeros((N, n+1))
    paths[:, 0] = S
    
    for t in range(1, n+1):
        epsilon = np.random.normal(0, 1, N)
        paths[:, t] = paths[:, t-1] * np.exp(drift + volatility * epsilon)
    
    return paths


# Option Price: 1.5405939732907692
# Standard Error: 0.026594089898247374
S = 17000  # Stock price
K = 17050  # Strike price
r = 5  # Interest rate (in percent)
s = 15  # Volatility (in percent)
T = 0.01  # Time to maturity in years
n = 100  # Number of time steps
N = 10000  # Number of simulation paths

# S = int(input( '請輸入 股票價格 S:' ))
# K = int(input( '請輸入 執行價格 K:' ))
# r = int(input( '請輸入 利率 r (例如利率為 5%，輸入值為 5):' ))   # 5%
# s = int(input( '請輸入 年度波動率 s (例如波動率為 30%，輸入值為 30):' ))  # 30%
# T = float(input( '請輸入 到期時間年 T:' ))
# n = int(input( '請輸入 時間步數 n:' ))
# N = int(input( '請輸入 模擬路徑數 N:' ))

option_price, standard_error = american_put_price(S, K, r, s, T, n, N)
print("Option Price:", option_price)
print("Standard Error:", standard_error)


"""Your function
* Name the function as american_put_price(...)
* The function should return: 
    1. american put price
    2. standard error
"""
# ...



"""Generate testcases"""
import itertools
import pandas as pd
import numpy as np
from tqdm import tqdm
import time

start_time = time.time()

# Example testcases from the paper
S_values = [val for val in range(36, 46, 2)]
K = 40
r = 6
s_values = [val for val in range(20, 60, 20)]
T_values = [val for val in range(1, 3, 1)]
N = 100000

total_iterations = len(list(itertools.product(S_values, s_values, T_values)))
print(f"Calculating {total_iterations} testcases of the paper...")
column_names = ["S", "s(%)", "T", "American price", "standard error"]
df = pd.DataFrame(columns=column_names)

print(f"K= {K}, r= {r}%, N= {N}, 50 exercisable points per year")
for values in tqdm(itertools.product(S_values, s_values, T_values), total=total_iterations):
    S, s, T = values
    n = T * 50
    american_price, standard_error = american_put_price(S, K, r, s, T, n, N)
    curr_row_values = [S, s, T, round(american_price, 4), round(standard_error, 4)]
    df.loc[len(df)] = curr_row_values

df[["S", "s(%)", "T"]] = df[["S", "s(%)", "T"]].astype(int)
print(df)

# Show execution time
end_time = time.time()
execution_time = end_time - start_time
if execution_time >= 60:
    minutes = execution_time // 60
    seconds = execution_time % 60
    print(f"Execution time: {int(minutes)} m {seconds:.4f} s\n")
else:
    print(f"Execution time: {execution_time:.4f} s\n")

# Comparing prices with the paper prices
print("Comparing your calculated prices with the paper prices...")
paper_prices = [4.472, 4.821, 7.091, 8.488,
                3.244, 3.735, 6.139, 7.669,
                2.313, 2.879, 5.308, 6.921,
                1.617, 2.206, 4.588, 6.243,
                1.118, 1.675, 3.957, 5.622]

column_names = ["S", "K", "r(%)", "s(%)", "T", "n", "N", "Your American price", "Paper American price"]
diff_df = pd.DataFrame(columns=column_names)

margin_error = 0.02
for index, value in df["American price"].items():
    if value < paper_prices[index] * (1 - margin_error) or value > paper_prices[index] * (1 + margin_error):
        curr_row_values = [df["S"][index], K, r, df["s(%)"][index], 
                           df["T"][index], df["T"][index] * 50, N, 
                           round(value, 4), round(paper_prices[index], 4)]
        diff_df.loc[len(diff_df)] = curr_row_values

if diff_df.empty:
    print(f"Your calculated prices are all within a margin of plus or minus {int(margin_error*100)}% of the paper prices!")
else:
    print(f"Some of your calculated prices exceed a margin of plus or minus {int(margin_error*100)}% of the paper prices")
    print("The following are the testcases that are not within the margin of error")
    diff_df[["S", "K", "r(%)", "s(%)", "T", "n", "N"]] = diff_df[["S", "K", "r(%)", "s(%)", "T", "n", "N"]].astype(int)
    print(diff_df)



"""
# Testcases of random inputs
np.random.seed(72)
num_testcases = 20
S_values = np.random.uniform(16500, 17000, num_testcases)
K_values = np.random.uniform(16500, 17000, num_testcases)
r_values = np.random.uniform(3, 15, num_testcases)
s_values = np.random.uniform(5, 50, num_testcases)
T_values = np.random.uniform(1, 10, num_testcases)
n_values = np.random.randint(25, 1000, num_testcases)
N_values = np.random.randint(100, 100000, num_testcases)

print(f"Testing {num_testcases} testcases of random inputs")
column_names = ["S", "K", "r(%)", "s(%)", "T", "n", "N", "American price", "standard error"]
df = pd.DataFrame(columns=column_names)

for S, K, r, s, T, n, N in tqdm(zip(S_values, K_values, r_values, s_values, T_values, n_values, N_values), total=num_testcases):
    american_price, standard_error = american_put_price(S, K, r, s, T, n, N)
    curr_row_values = [S, K, r, s, T, n, N, round(american_price, 4), round(standard_error, 4)]
    df.loc[len(df)] = curr_row_values

df[["n", "N"]] = df[["n", "N"]].astype(int)
print(df)
"""
