
import math
'''
def bermudan_option_price(S, K, r, s, T, H, n):
      dt = T / n
      sigma = s
      h = math.floor((math.log(S/H)) / (sigma * math.sqrt(dt)))
      lamda =  (math.log(S/H)) / (h * sigma * math.sqrt(dt))
      u = math.exp(lamda * sigma *math.sqrt(dt))
      d = 1 / u
      m = 1
      pu = (1/(2*(lamda**2))) + ((r-(sigma**2)/2)*math.sqrt(dt)) / (2*lamda*sigma)
      pd = (1/(2*(lamda**2))) - ((r-(sigma**2)/2)*math.sqrt(dt)) / (2*lamda*sigma)
      pm = 1 -pu - pd
    #   print(pu,pd,pm)

      # Initialize the binomial tree
      tree = [[0] *((i+1)*2-1) for i in range(n+1)]

      # Compute the stock price at each node
      for i in range(n+1):
            for j in range((i+1)*2-1):
                  tmp1 = i-j
                  if (tmp1)<0:
                        tmp1 = 0
                  tmp2 = j-i
                  if (tmp2)<0:
                        tmp2 = 0
                #   tree[i][j] = S * (d ** tmp1) * (m) * (u ** tmp2) 
                  tree[i][j] = S * (u ** tmp1) * (m) * (d ** tmp2) 
    
      # Compute the option value at maturity
    #   print(h)
      for j in range((i+1)*2-1):
            if S>=H:
                  tree[n][j] = max( tree[n][j] - K , 0)
            else:
                  tree[n][j] = 0 
            tree[n][n+h] = 0 # barrier的地方
            print(j,tree[n][j])      
      # Compute the option value
      for i in range(n-1, -1, -1):
            for j in range((i+1)*2-1):
                  if j < i+h:
                        # tree[i][j] = max(K - tree[i][j] + 1 , (tree[i+1][j]*pu + tree[i+1][j+1]*pm + tree[i+1][j+2]*pd))
                        # tree[i][j] = max(K - tree[i][j] + 1 , (tree[i+1][j+2]*pu + tree[i+1][j+1]*pm + tree[i+1][j]*pd))
                        tree[i][j] =  (pu*tree[i+1][j] + pm*tree[i+1][j+1] + pd*tree[i+1][j+2])  #/r
                  else :
                        tree[i][j] = 0

      # Return the option price
      return tree[0][0]/math.exp(r*T)

# Example usage

# S = 95
# K = 100
# r = 0.1  # 5%
# s = 0.25
# T = 1
# H = 90  # 30%
# n = 75 
# price = bermudan_option_price(95, 100, 0.1, 0.25, 1, 90, 75)
# print("Option price at n = {}: {:.4f}".format(75, price))
# price = bermudan_option_price(95, 100, 0.1, 0.25, 1, 90, 400)
# print("Option price at n = {}: {:.4f}".format(400, price))



S = int(input( '請輸入 股票價格 S:' ))
K = int(input( '請輸入 執行價格 K:' ))
r = int(input( '請輸入 連續複利年利率 r (例如利率為 5%，輸入值為 5):' )) / 100  # 5%
s = int(input( '請輸入 年度波動率 s (例如波動率為 30%，輸入值為 30):' )) / 100 # 30%
T = float(input( '請輸入 到期時間年 T:' ))
H = int(input( '請輸入 barrier H:' ))
n = int(input( '請輸入 時間步數 n:' ))
price = bermudan_option_price(S, K, r, s, T, H, n)
print("Option price at n = {}: {:.4f}".format(n, price))


'''




# Your function
# ...
def trinomial_tree(S, K, r, s, T, H, n):
      dt = T / n
      sigma = s
      h = math.floor((math.log(S/H)) / (sigma * math.sqrt(dt)))
      lamda =  (math.log(S/H)) / (h * sigma * math.sqrt(dt))
      u = math.exp(lamda * sigma *math.sqrt(dt))
      # u=(r-(sigma**2)/2)
      d = 1 / u
      m = 1
      pu = (1/(2*(lamda**2))) + ((r-(sigma**2)/2)*math.sqrt(dt)) / (2*lamda*sigma)
      pd = (1/(2*(lamda**2))) - ((r-(sigma**2)/2)*math.sqrt(dt)) / (2*lamda*sigma)
      pm = 1 -pu - pd
    #   print(pu,pd,pm)

      # Initialize the binomial tree
      tree = [[0] *((i+1)*2-1) for i in range(n+1)]

      # Compute the stock price at each node
      for i in range(n+1):
            for j in range((i+1)*2-1):
                  tmp1 = i-j
                  if (tmp1)<0:
                        tmp1 = 0
                  tmp2 = j-i
                  if (tmp2)<0:
                        tmp2 = 0
                #   tree[i][j] = S * (d ** tmp1) * (m) * (u ** tmp2) 
                  tree[i][j] = S * (u ** tmp1) * (m) * (d ** tmp2) 
    
      # Compute the option value at maturity
      for j in range((i+1)*2-1):
            if S>=H:
                  tree[n][j] = max( tree[n][j] - K , 0)
            else:
                  tree[n][j] = 0 
            # print(tree[n][j])      
      # Compute the option value
      for i in range(n-1, -1, -1):
            for j in range((i+1)*2-1):
                  if j < i+h:
                        # tree[i][j] = max(K - tree[i][j] + 1 , (tree[i+1][j]*pu + tree[i+1][j+1]*pm + tree[i+1][j+2]*pd))
                        # tree[i][j] = max(K - tree[i][j] + 1 , (tree[i+1][j+2]*pu + tree[i+1][j+1]*pm + tree[i+1][j]*pd))
                        tree[i][j] =  (pu*tree[i+1][j] + pm*tree[i+1][j+1] + pd*tree[i+1][j+2])  #/r
                  else :
                        tree[i][j] = 0

      # Return the option price
      return tree[0][0]/math.exp(r*T)
# Generate testcases
import pandas as pd
import itertools
from tqdm import tqdm
import time

start_time = time.perf_counter()

S_values = [103.8, 100, 150.99]
K_values = [97.45, 101.9, 168]
r_values = [4.2, 5.11, 15]
s_values = [25.82, 30, 30.54]
T_values = [0.5, 1.8, 3]
H_values = [87.65, 90, 93.4]
n_values = [75, 203, 342]
print(list(itertools.product(S_values, K_values, r_values, s_values, T_values, H_values, n_values)))
total_iterations = len(list(itertools.product(S_values, K_values, r_values, s_values, T_values, H_values, n_values)))
print(f"Number of testcases = {total_iterations}")

prices = []
for values in tqdm(itertools.product(S_values, K_values, r_values, s_values, T_values, H_values, n_values), total=total_iterations):
    S, K, r, s, T, H, n = values
    prices.append(round(trinomial_tree(S, K, r/100, s/100, T, H, n), 4))

# data = [[price] for price in prices]
# df = pd.DataFrame(data, columns=['prices'])

# file_name = "trinomial_test.csv"
# print(f"Outputting a csv file named {file_name}")
# df.to_csv(file_name, index=False)

# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time:.4f} seconds\n")


# url = "https://www.csie.ntu.edu.tw/~r11922148/trinomial.csv"
# wait_time = 20
# print(f"Trying to read data from {url}")
# while True:
#     try:
#         df_url = pd.read_csv(url)
#         print("Data read successfully!")
#         break
#     except Exception as e:
#         print(f"Error: {e}")
#         print(f"Waiting {wait_time} seconds before trying again...")
#         time.sleep(wait_time)

# print("Checking if the two DataFrames are the same")
# if df.equals(df_url):
#     print("DataFrames are the same!")
# else:
#     print("DataFrames are not the same")
    
#     df_diff = df.compare(df_url)
#     print("Differeces:")
#     print(df_diff)






'''
import math

def bermudan_option_price(S, K, r, s, T, H, n):
      dt = T / n
      sigma = s
      h = math.floor((math.log(S/H)) / (sigma * math.sqrt(dt)))
      lamda =  (math.log(S/H)) / (h * sigma * math.sqrt(dt))
      u = math.exp(lamda * sigma *math.sqrt(dt))
      # u=(r-(sigma**2)/2)
      d = 1 / u
      m = 1
      pu = (1/(2*(lamda**2))) + ((r-(sigma**2)/2)*math.sqrt(dt)) / (2*lamda*sigma)
      pd = (1/(2*(lamda**2))) - ((r-(sigma**2)/2)*math.sqrt(dt)) / (2*lamda*sigma)
      pm = 1 -pu - pd
      
      print(pu,pd,pm)

      # Initialize the binomial tree
      tree = [[0] *((i+1)*2-1) for i in range(n+1)]

      # Compute the stock price at each node
      for i in range(n+1):
            for j in range((i+1)*2-1-1, -1,-1):
                  tmp1 = i-j
                  if (tmp1)<0:
                        tmp1 = 0
                  tmp2 = j-i
                  if (tmp2)<0:
                        tmp2 = 0
                  tree[i][j] = S * (d ** tmp1) * (m) * (u ** tmp2) 
                  # tree[i][j] = S * (u ** tmp1) * (m) * (d ** tmp2) 
    
      # Compute the option value at maturity
      for j in range((i+1)*2-1-1, -1,-1):
            if S>=H:
                  tree[n][j] = max( tree[n][j] - K , 0)
            else:
                  tree[n][j] = 0 
            print(tree[n][j])      
      # Compute the option value
      for i in range(n-1, -1, -1):
            for j in range((i+1)*2-1-1, -1,-1):
                  if j > i-h:
                        # tree[i][j] = max(K - tree[i][j] + 1 , (tree[i+1][j]*pu + tree[i+1][j+1]*pm + tree[i+1][j+2]*pd))
                        # tree[i][j] = max(K - tree[i][j] + 1 , (tree[i+1][j+2]*pu + tree[i+1][j+1]*pm + tree[i+1][j]*pd))
                        tree[i][j] =  (pu*tree[i+1][j+2] + pm*tree[i+1][j+1] + pd*tree[i+1][j])  #/r
                  else :
                        tree[i][j] = 0

      # Return the option price
      return tree[0][0]/math.exp(r*T)

# Example usage

# S = 95
# K = 100
# r = 0.1  # 5%
# s = 0.25
# T = 1
# H = 90  # 30%
# n = 75 
price = bermudan_option_price(95, 100, 0.1, 0.25, 1, 90, 75)
print("Option price at n = {}: {:.4f}".format(75, price))
# price = bermudan_option_price(95, 100, 0.1, 0.25, 1, 90, 400)
# print("Option price at n = {}: {:.4f}".format(400, price))



# S = int(input( '請輸入 股票價格S:' ))
# K = int(input( '請輸入 執行價格K:' ))
# r = int(input( '請輸入 連續複利年利率r (例如利率為 5%，輸入值為 5):' )) / 100  # 5%
# s = int(input( '請輸入 年度波動率s (例如波動率為 30%，輸入值為 30):' )) / 100 # 30%
# T = float(input( '請輸入 到期時間年T:' ))
# n = int(input( '請輸入 時間步數n:' ))
# price = bermudan_option_price(S, K, r, s, T, H, n)
# print("Option price at n = {}: {:.4f}".format(n, price))

'''