'''
Compute mean for the data set given:
10, 12, 11, 9, 9, 10, 11, 12, 11, 10, 11, 12
'''
#--------------------------------------------------------------------------------------------------
#Input:
my_list = [10, 12, 11, 9, 9, 10, 11, 12, 11, 10, 11, 12]

#Calculations:
count = len(my_list)
add = sum(my_list)
avg_1 = add/count

#Printing result:
print(f"(Trial-1) The mean of the given dataset using normal python is = {avg_1:.3f}")

#O/P: (Trial-1) The mean of the given dataset using normal python is = 10.667

#--------------------------------------------------------------------------------------------------
import numpy as np

#Calculation using numpy:
avg_2 = np.mean(my_list)

#Printing result:
print(f"(Trial 2 The mean of the given dataset using numpy is = {avg_2:.3f} ")

#O/P: (Trial 2 The mean of the given dataset using numpy is = 10.667 
