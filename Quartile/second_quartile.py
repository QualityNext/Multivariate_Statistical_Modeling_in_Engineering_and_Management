'''
The following sample (n=12) is collected from a population. Obtain its first quartile, second
quartile (median) and the third quartile values.
10, 12, 11, 9, 9, 10, 11, 12, 11, 10, 11, 12
'''

#Input from the question
my_list = [10, 12, 11, 9, 9, 10, 11, 12, 11, 10, 11, 12]
quartile = 50

#Calculations
sorted_list = sorted(my_list)
n = len(sorted_list)
index = int((n+1)*(quartile/100)) #Note: There need to be an int() as index cannot be fraction.

#Output
print("Second quartile:",sorted_list[index])
