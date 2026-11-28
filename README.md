# Multivariate_Statistical_Modeling_in_Engineering_and_Management
Unofficial Python implementation of the Multivariate Statistical Modeling in Engineering and Management book

## Finding first quartile, second quartile (median) and the third quartile values
- For any list of data points finding quartile means identifying the numbers that divides the data set into four equal parts.
- First quartile or 25<sup>th</sup> percentile is the value below which 25% of the observations in the dataset lie. It is calculated as (n+1)*(25/100).
- Similarly second quartile and third quartile are the value below which 50% and 75% of the data points lie.
- We may want to find the quartiles of the data points to visualize the spread of the data set as we do in the case of a box plot.

- **Check out on YouTube:**
  https://youtu.be/N_VOuAckMqA
  
- **Source file:**
  - [`Quartile/first_quartile.py`](Quartile/first_quartile.py)
  - [`Quartile/second_quartile.py`](Quartile/second_quartile.py)
  - [`Quartile/third_quartile.py`](Quartile/third_quartile.py)

> [!NOTE]
> In NumPy, the default formula for calculating percentile is `(n - 1) * (p / 100)`, where `n` is the number of data points and `p` is the target percentile.
> Either formula can be used for calculating percentile.

## Finding the mean of a given dataset
- The **mean** of the dataset can be thought of as the center of mass of all the data points.   
It is calculated as mean = (Sum of all the data points)/n where n is the number of data points.
- It is a measure of central tendency. By trying to find the central tendency of a dataset, a person may be trying to find a way to represent the whole dataset with a single number that will give a very good idea of all the data points.
- Knowing the central tendency may be useful if a person want to know an estimate of price of a house at a particular location.
- Knowing the mean may not be a very good way of finding the central tendency as it is very sensitive to outliers and so we also use median and mode to identify the central tendency.

- **Check out on YouTube:**
https://youtu.be/8RrP_uxzo84

- **Source file:** [`Mean_Var_Std/mean.py`](Mean_Var_Std/mean.py)
