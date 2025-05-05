from scipy.stats import uniform,binom,poisson
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Uniform
mean=100
a=0
b=30
x1=0
x2=10
prob=uniform.cdf(x2,loc=a,scale=b-a)-uniform.cdf(x1,loc=a,scale=b-a)
print(prob)

#Binomial
sd=5
size=100000
data=np.random.normal(mean,sd,size)
sns.histplot(data,kde=True)
plt.show()

#Poisson
#lambda=average rate
a=3
k=5
#mu=average rate(mean)
#k=actual number of events
prob=poisson.pmf(k,mu=a)
print(f"P(X={k}) = {prob:.4f}")