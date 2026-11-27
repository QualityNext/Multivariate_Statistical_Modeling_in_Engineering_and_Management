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
print(f"(Trial 2) The mean of the given dataset using numpy is = {avg_2:.3f} ")

#O/P: (Trial 2) The mean of the given dataset using numpy is = 10.667 
#--------------------------------------------------------------------------------------------------

'''
Find outliers and calculate mean for the new dataset.
10, 12, -28, 11, 0.001, 9, 9, 10, 11, 12, 2000, 11, 10, 11, 12
'''
my_new_list = np.array([10, 12, -28, 11, 0.001, 9, 9, 10, 11, 12, 2000, 11, 10, 11, 12]) #We need to define the dataset as an np.array for *1

q1 = np.percentile(my_new_list,25) #Gives the Q1-quartile using the numpy's percentile function.
q3 = np.percentile(my_new_list,75) #Similarly this gives the Q3-quartile.
iqr = q3-q1 # IQR is the difference between the Q3 and Q1.

lower_limit = q1-1.5*iqr
upper_limit = q3+1.5*iqr

#Finding values that are above the upper limit.
print(f"These values are outliers as they are above our defined upper limit: {my_new_list[my_new_list>upper_limit]} ") # *1. This is a numpy functions that lists all the values according to the condition.
# O/P: These values are outliers as they are above our defined upper limit: [2000.]

#Finding values that are below the lower limit.
print(f"These values are outliers too because they are below our defined lower limit: {my_new_list[my_new_list<lower_limit]}")
# O/P: These values are outliers too because they are below our defined lower limit: [-2.8e+01  1.0e-03]

#Calculating and printing mean
print(f"The mean of the dataset is: {np.mean(my_new_list):.3f}")
# O/P: The mean of the dataset is: 140.000
# The mean of the dataset jumped to 140 because of a single high value outlier 2000. In most of the other values they are in the range below 12 so 140 may not be a very good representation of the dataset. 