Write a program to generate an amortization schedule for repaying a loan. There are two interest rates. 
Inputs: 
(1) L (loan amount in dollars), 
(2) r1 (annual interest rate in percent for the first n1 periods, so 12 instead of 0.12), 
(3) r2 (annual interest rate in percent for the remaining periods), 
(4) n1 (number of periods when the interest rate is r1), 
(5) n (duration of the loan in years), 
(6) m (the number of payments per annum). 
Output: 
A csv file for the amortization schedule and the total interest paid. 
The schedule shall have five columns: 
(1) Time (0, 1, 2, ...), 
(2) The level payment amount, 
(3) Interest (the interest part of each payment), 
(4) Principal (the principal part of each payment), 
(5) Remaining principal. 
For example, if L = 10,000,000, r1 = 8%, r2 = 3%, n1 = 120, n = 20, and m = 12, the example output file is here and the total interest is 8593339.37. 
IMPORTANT notes: 
(1) The Time column must be integers (no floating-point numbers). 
(2) The Payment, Interest, Principal, and Remaining principal columns must be floating-point numbers up to 2 decimal points. 
(3) The order of the columns must be respected. 
(4) The headers of the columns must be as in the sample file. 
(5) Start from Time 0 instead of Time 1. 
This means the value of the first row will be 0, 0, 0, 0, L.
===============================================================================================================================================================
編寫一個程序來生成償還貸款的分期償還計劃，有兩種利率。
輸入：
(1) L（以美元計的貸款金額），
(2) r 1 （前n 1期的年利率，以百分比表示，因此 12 而不是 0.12），
(3) r 2（以百分比表示的年利率，剩餘期限），
（4）n 1（利率為r 1時的期限數），
（5）n（貸款年限），
（6）m（每年的付款次數）。
輸出：
一個 csv 文件，其中包含攤銷時間表和支付的總利息。
明細表應有五欄：
（1）時間（0、1、2，...），
（2）等級支付金額，
（3）利息（每筆支付的利息部分），
（4）本金（本金）每筆付款的本金部分），
(5) 剩餘本金。

例如，
如果L = 10,000,000，r 1 = 8%，r 2 = 3%， n 1 = 120，n = 20，m = 12，示例輸出文件在這裡，總利息為 8593339.37。
重要提示：
(1)時間列必須是整數（無浮點數）。
(2) Payment、Interest、Principal和Remaining principal列必須是小數點後兩位的浮點數。
(3) 必須遵守列的順序。
(4) 列的標題必須與示例文件中的一樣。
(5) 從時間 0 而不是時間 1 開始。
這意味著第一行的值將為 0, 0, 0, 0, L。
