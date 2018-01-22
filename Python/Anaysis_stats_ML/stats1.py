# Stats rigor
# Sample size
# Significance

# Normal distribution
# mu = mean
# sigma = std
#
# f(x) = (2*pi*sig**2)**-0.5 * exp(-(x-mu)**2 / (2sig**2))
#
# T-test
# Accept or reject null hypothesis:
# Same sample population, a sample is drawn from a probability
# distribution
#
# one sample: mu = mu_0
# two sample: mu_0 = mu_1
#
# Welch's T-test
# most general - no assumption of equal sample size or variance
#
# t = (mu_1 - mu _2) * ((sig1**2 / N1) + (sig2**2 / N2))**-0.5
#
# N = sample size
#
# v = degrees of freedom (n-1)
#
# v =  (((sig1**2 / N1) + (sig2**2 / N2))**2 /
#       ((sig1**4 / v1N1**2) + (sig2**4 / v2N2**2)))
#
# p value = probability of obtaining test stat at least
# as extreme as value if null hypothesis was true.
#
# NOT probability of hypoth true give the data
#
# set a critical value - below critical allows reject null hypoth:
# if p < pcrit:
#	REJECT Null hypothesis
# else:
# 	can not reject null
#
# Be very careful typing that up in python!!
# Luckiliy scipy stats helps
#
# scipy.stats.ttest_ind(data1,data2, equal_var=False)
#
# equal varience = false = Welch's test 
# returns a tuple t, p (2 tail)
# scipy.stats.ttest_ind assumes a two-side t-test only testing 
# if means are different
# 
# one sided would be half that of two sided!
# mean is greather than:  P/2 < Pcirt, t > 0
# mean is less than:      P/2 > Pcirt, t < 0
import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    df = pandas.read_csv(filename)
    df = pandas.DataFrame(pandas.read_csv(filename))
    averagesL = df[df.handedness == 'L'].avg
    averagesR = df[df.handedness == 'R'].avg
   
    Ttestvals = scipy.stats.ttest_ind(averagesR,averagesL, equal_var=False)
    if Ttestvals[1] <= 0.05:
    	return (True, Ttestvals)
    else:
        return (False, Ttestvals)
    