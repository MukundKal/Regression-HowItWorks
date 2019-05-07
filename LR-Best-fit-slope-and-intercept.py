
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


# In[59]:


predict_x=5.6
predict_y= m*predict_x+b 

plt.scatter(xs1,ys1)
plt.scatter(predict_x,predict_y,color='red')
plt.plot(xs1, regression_line)
plt.show()

