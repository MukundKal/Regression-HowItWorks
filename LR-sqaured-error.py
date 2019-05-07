
# coding: utf-8

# In[47]:


from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


# ### Creating Sample X's and Y's to then formulate the best-fit slope.

# In[40]:


xs1 = np.array([1,2,3,4,6,8])
ys1 = np.array([4,6,7,9,10,12])


# ### The best-fit slope *m* is given by the formula 
#  Estimated Best-fit Linear Regression Slope **m = __Cov(xs,ys)__ /  __Var(xs)__ **

# In[49]:


def best_fit_slope_and_intercept(xs,ys):
    m = ( mean(xs*ys) - mean(xs)*mean(ys) ) / ( mean(xs*xs) - mean(xs)*mean(xs) )
    b = mean(ys)- m*mean(xs)
    return m,b
    


# Using the function to get the best-fit slope of the sample values *xs* and *ys*

# In[50]:


m,b = best_fit_slope_and_intercept(xs1,ys1)
print(m,b)


# In[51]:


regression_line= [m*x+b for x in xs] 
# for  x in xs:
#     regression_line.append(m*x+b)


# In[56]:


plt.scatter(xs1,ys1)
plt.plot(xs1, regression_line)
plt.show()


# In[63]:


predict_x=5.6
predict_y= m*predict_x+b 

plt.scatter(xs1,ys1)
plt.scatter(predict_x,predict_y,color='red')
plt.plot(xs1, regression_line)
plt.title('Best-Fit Line',color='green')
plt.show()


# The _Best-Fit Line_ to a particular set of data is the linear line that fits it the most.
# But is it an accurate/good-fit to that data?
# 
# The _Good-Fit Line_ is the line that is the most accurate to that data.
# The **R<sup>2</sup>** or the _coefficent of determination_ indicates the extent of how well the line has fit the data and this s done using **Sqaured Error** theory

# In[74]:


def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)


# In[77]:


def coefficent_of_determination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    r = 1 - ( squared_error_regr / squared_error_y_mean )     
    return r


# In[78]:


r_squared = coefficent_of_determination(ys1, regression_line)
print(r_squared) #higher value indicating that the regression_line found is actually accurate to the data.


# In[ ]:




