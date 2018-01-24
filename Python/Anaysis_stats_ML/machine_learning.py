## Machine Learning ##
#
# AI constructing systems to make predictions from large
# amounts of data
# 
# supervised learning : have examples where answer is known, 
# train the model with known. Regression.
# 
# unsupervised learning: clustering  
#
# Linear regression 
# with gradient descent
# Cost function J(x)
# Defining cost funtion as linear regression 
# (sum error terms squared)
#
# J(theta) = sum (Y_p -Y_o)**2
#
# J(theta) = 0.5 * sum(Y_p(theta_i)-Y_oi)**2
#  Y_p(theta_i)  = sum (theta_n theta_ni)
# Predicted value is sum weighted impute variable
# 
# The idea is to minimise J(x)
# Search to find convergnece
#
# Gradient descent in python:
import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    
    cost_history = []
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
     
    m = len(values)
    for i in range(num_iterations):
    	Yi = numpy.dot(features,theta) # predicted values
    	# update theta
     	theta = theta - (alpha/m) * (numpy.dot((Yi - values),features)) 
     	# small step in direction of steepest gradient
    	cost = compute_cost(features,values,theta)
    	cost_history.append(cost)
    

    return theta, pandas.Series(cost_history) # leave this line for the grader
#
#
# Evaluate model
# 
# R^2 = coeffient of determination
#
# data = y_i ... y_n
# predictions = f_i ... f_n
# average of data = ybar
#
# R^2 = 1 - (sum((yi-fi)^2)/sum((yi-ybar)^2))
# R^2 = 1 - (SST / SSReg)
# R^2 closer to 1  is best (zero is bad)
#
import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    r_squared = 1 - (np.sum((data - predictions	)**2)/np.sum((data - np.mean(data))**2))

    return r_squared
#
#
# Many more linear reqression:
# Least squares
# Parameter estimation - confidence intervals
# Over/ underfitting - training set and test set (cross validation)
# Multiple local minima (gradient descent might not pick up global min)
# NB seed random values
#
# K- means clustering and PCA are useful
# 
#
# http://georgemdallas.wordpress.com/2013/10/30/principal-component-analysis-4-dummies-eigenvectors-eigenvalues-and-dimension-reduction/
#
# establish causal connections