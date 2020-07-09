Stats Calculator Project

Authors: Adib Haque & Marlon Sarkor

Responsibilities: Shared Code and ReadME description

This program is a statistics calculator able to utilize and resolve multiple statistical functions such as mean, median, mode, variance, standard deviation and
Z-Score. The program is based on the previous Calculator program which performed basic math functions. Inheritance was used to gain abilities from the original 
project. Encapsulation and abstraction were also demonstrated by using static methods to perform certain operations. The statistics calculator also checked values 
ensuring the correct data type. 

Below are descriptions for the different functions of a Stats Calculator. 

Mean: The mean is the sum of all given numbers divided by the number of numbers. The mean produces the average. Please see demonstation below:

![github-medium](https://www.mathsteacher.com.au/year9/ch17_statistics/01_mean/Image2766.gif)

Median: The median is the middle number in a sorted, ascending or descending, list of numbers and can be more descriptive of that data set than the average. 
The median is sometimes used as opposed to the mean when there are outliers in the sequence that might skew the average of the values.
Source: www.investopedia.com

![github-medium](https://cdn.wallstreetmojo.com/wp-content/uploads/2019/03/Median-Formula.jpg)

Mode: The mode of a set of data values is the value that appears most often. 
If X is a discrete random variable, the mode is the value x (i.e, X = x) at which the probability mass function takes its maximum value. 
In other words, it is the value that is most likely to be sampled.
Source: en.wikipedia.org
![github-medium](https://cdn.educba.com/academy/wp-content/uploads/2019/07/Mode-Formula.jpg)

Variance: Variance (σ2) in statistics is a measurement of the spread between numbers in a data set. 
That is, it measures how far each number in the set is from the mean and therefore from every other number in the set.
Source: www.investopedia.com
![github-medium](https://www.statisticshowto.com/wp-content/uploads/2013/09/Variance_Formula.png)

Standard Deviation: In statistics, the standard deviation is a measure of the amount of variation or dispersion of a set of values. 
A low standard deviation indicates that the values tend to be close to the mean of the set, while a high standard deviation indicates that the values are spread out over a wider range.
Source: www.wikipedia.org
![github-medium](https://i.ytimg.com/vi/IaTFpp-uzp0/maxresdefault.jpg)

Z-Score: In statistics, the standard score is the number of standard deviations by which the value of a raw score is above or below the mean value of what is being observed or measured. 
Raw scores above the mean have positive standard scores, while those below the mean have negative standard scores.
Source: en.wikipedia.org

![github-medium](https://www.z-table.com/uploads/2/1/7/9/21795380/5175170_orig.gif)

Population Sampling Functions:
See below for descriptions of population sampling functions. 

Simple Random Sampling
A simple random sample is a subset of a statistical population in which each member of the subset has an equal probability of being chosen. A simple random sample is meant to be an unbiased representation of a group.
Source: investopedia.org

![github-medium](https://faculty.elgin.edu/dkernler/statistics/ch01/images/srs.gif)

The formula follows below:

![github-medium](https://slideplayer.com/slide/6574460/23/images/27/Simple+random+sampling+%E2%80%93+determining+sample+size.jpg)

Confidence Interval: In statistics, a confidence interval is a type of estimate computed from the statistics of the observed data. This proposes a range of plausible values for an unknown parameter. The interval has an associated confidence level that the true parameter is in the proposed range.
Source: stattrek.com

![github-small](https://www.statisticshowto.com/wp-content/uploads/2009/10/ci-for-the-mean-formula.png)

Margin of Error: A margin of error tells you how many percentage points your results will differ from the real population value. For example, a 95% confidence interval with a 4 percent margin of error means that your statistic will be within 4 percentage points of the real population value 95% of the time.
Source: statisticshowto.com

![github-medium](https://cdn.wallstreetmojo.com/wp-content/uploads/2019/03/Margin-of-Error-Formula.jpg)

Cochran’s Sample Size Formula: The Cochran formula allows you to calculate an ideal sample size given a desired level of precision, desired confidence level, and the estimated proportion of the attribute present in the population. Cochran's formula is considered especially appropriate in situations with large populations.
Source: www.quora.com

![github-medium](https://slideplayer.com/slide/5294690/17/images/23/Cochran+equation+Where+n0+is+the+sample+size%2C.jpg)


Correlation Coefficients: Correlation coefficients are used in statistics to measure how strong a relationship is between two variables. 
Source: stattrek.com
![github-large](https://cdn.wallstreetmojo.com/wp-content/uploads/2019/03/Correlation-Coefficient-Formula-2.jpg)

P-Value: In statistical hypothesis testing, the p-value or probability value is the probability of obtaining test results at least as extreme as the results actually observed, assuming that the null hypothesis is correct.
Source: wikipedia.org
![github-medium](https://cdn.wallstreetmojo.com/wp-content/uploads/2019/04/P-Value-Formula.jpg)

Proportion: A proportion refers to the fraction of the total that possesses a certain attribute. For example, suppose we have a sample of four pets - a bird, a fish, a dog, and a cat. We might ask what proportion has four legs. Only two pets (the dog and the cat) have four legs.
Source: stattrek.com

![github-medium](https://people.richland.edu/james/lecture/m170/ch10-pro.htg/img2.gif)

Program Functionality/Diagram/Outline: 
Most of the program's concepts have been described above, but please see quick overview below:
The Program consists of several sections to utilize different functions.  

Calculator: This provides simple mathematical attributes to process calculations. The Stat Calculator inherits these traits
![github-medium](https://compass1.org/wp-content/uploads/2015/06/Calculator_clipped_rev_1.png)

CsvReader: This allows for the program to parse through CSV files and output data when needed. This ability also allows for identifying the correct 
data type. For example, this function will identify integers correctly as opposed to categorizing it as a string. 

Decorators and File Utilities: This section of the program allows for correct location discovery for needed files.

Statistics (THE GOLD): This holds all needed attributes supporting the different uses of statistics described above. Please use README file to reference and understand the different formulas and calculations. 
![github-medium](https://online.stanford.edu/sites/default/files/styles/figure_default/public/2018-08/introduction-to-probability-and-statistics-for-epidemiology_HRP259.jpg?itok=hu6PM2ZF)

Tasks Lists:
Adib and Marlon worked in person for a great amount of the project. The contributions reflect collaborative efforts throughout the project.

Please see below for sample view of github commits. Since we are talking statistics, why not use a sample to demonstrate! 




