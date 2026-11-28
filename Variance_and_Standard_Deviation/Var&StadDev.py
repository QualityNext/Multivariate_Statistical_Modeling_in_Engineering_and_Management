'''
Compute variance and standard deviation of the data set given
10 12 11 9 9 10 11 12 11 10 11 12
'''
#--------------------------------------------------------------------------------------------------------------

# Input data:
my_list = [10, 12, 11, 9, 9, 10, 11, 12, 11, 10, 11, 12 ]

#=========
# Step-1
#=========
#Calculating Mean:
sum_my_list = sum(my_list)
count = len(my_list)
mean_of_my_list = sum_my_list/count

#=========
# Step-2
#=========
# Calculating Mean Subtracted Deviation:
# A python list mean_subtracted_deviation is defined to staore all the values.
# Subtracting the mean from all individual data point and storing inside a list mean_subtracted_deviation python list.
mean_subtracted_deviation = []  
for i in range(count):
    mean_subtracted_deviation.append(my_list[i]-mean_of_my_list) 

#=========
# Step-3
#=========
# Calculating Squared Mean Subtracted Deviation:
# A python list squared_mean_subtracted_deviation is defined to staore all the values.
# Squaring each term of the mean_subtracted_deviation and storing it inside the squared_mean_subtracted_deviation python list.
squared_mean_subtracted_deviation =[]
for i in range(count):
    squared_mean_subtracted_deviation.append(mean_subtracted_deviation[i]**2)

#=========
# Step-4
#=========
# Calculating Sum of Squared Mean Subtracted Deviation for Variance calculation:
# Adding up all the values in the squared_mean_subtracted_deviation list and storing inside a variable.
sum_of_squared_mean_subtracted_deviation = sum(squared_mean_subtracted_deviation)

#Printing results from Step 2, 3 & 4:
print(f"Mean Subtracted Deviation ={[round(x,3) for x in mean_subtracted_deviation]}") #Also known as MSD
print(f"Squared Mean Subtracted Deviation ={[round(x,3) for x in squared_mean_subtracted_deviation]}") #Squared MSD
print(f"Sum of squared Mean Subtracted Deviation = {sum_of_squared_mean_subtracted_deviation:.3f}") #Sum of Squared MSD

# O/P:
# Mean Subtracted Deviation =[-0.667, 1.333, 0.333, -1.667, -1.667, -0.667, 0.333, 1.333, 0.333, -0.667, 0.333, 1.333]
# Squared Mean Subtracted Deviation =[0.444, 1.778, 0.111, 2.778, 2.778, 0.444, 0.111, 1.778, 0.111, 0.444, 0.111, 1.778]
# Sum of squared Mean Subtracted Deviation = 12.667

#=========
# Step-5
#=========
# Calculating Sample Variance and Sample Standard Deviation because this dataset is of a sample observation:
# Dividing sum_of_squared_mean_subtracted_deviation by number of variable - 1, gives us Sample Variance
# Square root of the Sample Variance gives the Sample Standard Deviation
Sample_Variance = sum_of_squared_mean_subtracted_deviation/(count-1) 
Sample_Standard_Deviation = Sample_Variance **0.5

#Printing Final Result:
print(f"Sample variance = {Sample_Variance:.3f}")
print(f"Sample Standard Deviation = {Sample_Standard_Deviation:.3f}")

# O/P:
# Sample variance = 1.152
# Sample Standard Deviation = 1.073
#--------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

#To present the data in a clean pandas dataframe making a Dictionary named data and storing the data with proper header.
data = {
            'Observation' : my_list,
            'MSD' : mean_subtracted_deviation,
            'Squared MSD' : squared_mean_subtracted_deviation
        }

# Presenting the observations, MSD and Squared MSD in a clean pandas DataFrame for easy reading:
df = pd.DataFrame(data)
print(f"\nPandas Data Frame representation:\n{df.round(3)}")

#O/P:
#Pandas Data Frame representation:
#    Observation    MSD  Squared MSD
#0            10 -0.667        0.444
#1            12  1.333        1.778
#2            11  0.333        0.111
#3             9 -1.667        2.778
#4             9 -1.667        2.778
#5            10 -0.667        0.444
#6            11  0.333        0.111
#7            12  1.333        1.778
#8            11  0.333        0.111
#9            10 -0.667        0.444
#10           11  0.333        0.111
#11           12  1.333        1.778

#Calculating Sample Variance and Sample Standard Deviation of the Observation
# ddof = 0 is the default case. It calculates Population Variance and Population Standard Deviation. Putting ddof = 1 will calculate Sample Variance and Standard Deviation.
Sample_Variance_1 = np.var(df['Observation'], ddof=1) 
Sample_Standard_Deviation_1 = np.std(df['Observation'], ddof=1)

#Printing Results
print("Sample Variance calculated using numpy =",Sample_Variance_1.round(3))
print("Sample Standard deviaion calculated using numpy =", Sample_Standard_Deviation_1.round(3))

# O/P:
# Sample Variance calculated using numpy = 1.152
# Sample Standard deviaion calculated using numpy = 1.073