'''Adjust values in a list by normalizing
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.
For this program, adjust the values by dividing all values by the largest value. The input begins with an integer indicating the number of floating-point values that follow.
Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
 print('{:.2f}'.format(your_value))
Ex: If the input is:
5
30.0
50.0
10.0
100.0
65.0

the output is:
0.30
0.50
0.10
1.00
0.65

The 5 indicates that there are five floating-point values in the list, namely 30.0, 50.0, 10.0, 100.0, and 65.0. 100.0 is the largest value in the list, so each value is divided by 100.0.
vals = []
total = int(input())'''

for i in range(total):
	num_in = float(input())
	vals.append(num_in)
    
max_val = max(vals)

for i in vals:
	print('{:.2f}'.format(i/max_val))
