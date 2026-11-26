# Multivariate_Statistical_Modeling_in_Engineering_and_Management
Unofficial Python implementation of Jhareswar Maiti's Multivariate Statistical Modeling in Engineering and Management

## Finding first quartile, second quartile (median) and the third quartile values
- For any list of data points finding quartile means identifying the numbers that divides the data set into four equal parts.
- First quartile or 25<sup>th</sup> percentile is the value below which 25% of the observations in the dataset lie. It is calculated as (n+1)*(25/100).
- Similarly second quartile and third quartile are the value below which 50% and 75% of the data points lie.
- We may want to find the quartiles of the data points to visualize the spread of the data set as we do in the case of a box plot.

>[!NOTE]
>In numpy the default formula for calculating percentile is (n-1)*(p/100) where n is the number of data points and p is the target percentile.
>Either of the formula can be used for calculating percentile.
