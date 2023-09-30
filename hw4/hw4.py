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

# Example usage
# S = 100  # Stock price
# K = 95  # Strike price
# r = 1  # Interest rate (in percent)
# s = 10  # Volatility (in percent)
# T = 1  # Time to maturity in years
# n = 100  # Number of time steps
# N = 10000  # Number of simulation paths

S = int(input( '請輸入 股票價格 S:' ))
K = int(input( '請輸入 執行價格 K:' ))
r = int(input( '請輸入 利率 r (例如利率為 5%，輸入值為 5):' ))   # 5%
s = int(input( '請輸入 年度波動率 s (例如波動率為 30%，輸入值為 30):' ))  # 30%
T = float(input( '請輸入 到期時間年 T:' ))
n = int(input( '請輸入 時間步數 n:' ))
N = int(input( '請輸入 模擬路徑數 N:' ))

option_price, standard_error = american_put_price(S, K, r, s, T, n, N)
print("Option Price:", option_price)
print("Standard Error:", standard_error)

