'''
The following sample (n=12) is collected from a population. Obtain its first quartile, second
quartile (median) and the third quartile values.
10, 12, 11, 9, 9, 10, 11, 12, 11, 10, 11, 12
'''
#--------------------------------------------------------------------------------------------------
#Input from the question
my_list = [10, 12, 11, 9, 9, 10, 11, 12, 11, 10, 11, 12]
quartile = 25

#Calculations
sorted_list = sorted(my_list)
n = len(sorted_list)
index_1 = int((n+1)*(quartile/100)) - 1 #Note: There need to be an int() as index cannot be fraction.

#Printing Result
print("(Trial 1) First quartile:",sorted_list[index_1])

#Output: (Trial 1) First quartile: 10
#--------------------------------------------------------------------------------------------------
# In the above case the fractional value of index calculation was not considered which is not proper.
# To account for the fractional value of index we will use interpolation to find the inbetween number.
index_2 = (n+1)*(quartile/100)-1
lower = int(index_2)
upper = lower+1
quartile_value = sorted_list[lower] + (index_2-lower)*(sorted_list[upper]-sorted_list[lower])

#Printing Result with interpolation
print("(Trial 2) First Quartile:", quartile_value)

#Output: (Trial 2) First Quartile: 10.0
#--------------------------------------------------------------------------------------------------
#Finding first-quartile using numpy
import numpy as np

q_value = np.percentile(my_list,quartile)

#Printing Result
print("(Trial 3) First Quartile:", q_value)

#Output: (Trial 3) First Quartile: 10.0