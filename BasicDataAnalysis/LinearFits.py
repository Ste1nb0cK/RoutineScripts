import numpy as np
import pandas as pd
from sklearn import linear_model

#A little bit faster way for using sklearn to obtain linear regression coeffcients and r^2
def regcoeff(x,y):
    regresion = linear_model.LinearRegression()
    regresion.fit(x, y)
    b = regresion.coef_[0] #slope
    a = regresion.intercept_[0] #intercept
    r2 = np.corrcoef(x, y)[0] #Get only the diagonal
    output = {'slope' : b, 'intercept' : a, 'r2' : r2}
    return output

#Function for calculating the uncertainty of a regression.
def regcoeff_uncertainty(x, y, b, a):
    n = x.shape[0]
    epsilon = y - b*x - a
    sigma_y = np.sqrt( np.sum(epsilon**2)/(n-2))
    db = sigma_y * np.sqrt( n / (n*np.sum(x**2) - np.sum(x)**2))
    da = sigma_y * np.sqrt( np.sum(x**2) / (n*np.sum(x**2) - np.sum(x)**2))
    return db, da