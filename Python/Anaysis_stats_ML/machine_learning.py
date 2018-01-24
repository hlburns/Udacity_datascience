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
# J(x) = sum (Y_p -Y_o)**2
#
# J(x) = 0.5 * sum(Y_p(x_i)-Y_oi)**2
#  Y_p(x_i)  = sum (x_n x_ni)
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
    theta_j = theta 
    Yi = numpy.dot(features[:,0],values)
    m = len(values)
    for i in range(num_iterations):
     	theta_j = theta_j + (alpha/m) * (numpy.dot(features[:,0],(Yi - values))) 
    	cost = compute_cost(features,values,theta_j)
    	cost_history.append(cost)

    return theta, pandas.Series(cost_history) # leave this line for the grader
