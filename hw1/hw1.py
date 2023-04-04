import csv
import math
'''
# Input variables
L = 10000000  # loan amount in dollars
r1 = 8  # annual interest rate for the first n1 periods
r2 = 3  # annual interest rate for the remaining periods
n1 = 10  # number of periods when the interest rate is r1
n = 20  # duration of the loan in years
m = 12  # number of payments per annum
'''
#input 
L = int(input('輸入L (loan amount in dollars)：'))
r1 = int(input('輸入r1 (annual interest rate in percent for the first n1 periods)：'))
r2 = int(input('輸入 r2 (annual interest rate in percent for the remaining periods)：'))
n1 = int(input('輸入n1 (number of periods when the interest rate is r1)：'))
n = int(input('輸入n (duration of the loan in years)：'))
m = int(input('輸入m (the number of payments per annum)：'))
period = m * n
time=0
payment=0
Interest = 0
Principal = 0
Remaining_principal = 10000000

#month_rate_r1
month_rate_r1 = (r1 / 100) / m
#month_rate_r2
month_rate_r2 = (r2 / 100) / m

# Open the output csv file
with open('amortization_schedule.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'Payment', 'Interest', 'Principal', 'Remaining principal'])
    writer.writerow([int(time), round(payment, 2), round(Interest, 2), round(Principal, 2), round(Remaining_principal, 2)])
    
    # Calculate payment
    temp1 = math.pow( (1 + month_rate_r1) , (n1 * m) )
    temp2 = (1 - math.pow( (1 + month_rate_r2) , -((n - n1) * m) )) * month_rate_r1
    temp3 = (temp1 * month_rate_r2) - month_rate_r2
    payment = ( month_rate_r1 * month_rate_r2 * temp1 * L ) / ( temp3 + temp2 )
    
    for i in range (1,period+1):
        time = time + 1
        # Calculate Interest and Principal and Remaining_principal
        if ( 0 < i <= (n1 * m)):
            Interest = Remaining_principal * ((r1/m) / 100)
            Principal = payment - Interest
            Remaining_principal = Remaining_principal - Principal
        elif ((n1 * m) < i):
            Interest = Remaining_principal * ((r2/m) / 100)
            Principal = payment - Interest
            Remaining_principal = Remaining_principal - Principal
            
        while (Remaining_principal < 0):
            Remaining_principal=0
            
        print(time , payment , Interest , Principal , Remaining_principal)
        # Write to csv file
        writer.writerow([int(time), round(payment, 2), round(Interest, 2), round(Principal, 2), round(Remaining_principal, 2)])
        
    


