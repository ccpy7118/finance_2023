import math

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
            # print(j,tree[n][j])      
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
