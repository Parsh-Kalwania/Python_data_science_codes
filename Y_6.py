import math
from  scipy.stats import norm
import scipy.stats as stats
import statsmodels.api as sm

# Sample data

sample_mean=169.5
pop_mean=168
std_dev=3.9
sample_size=36
alpha=0.05
tail='two'

z_score=((sample_mean-pop_mean)*math.sqrt(sample_size))/std_dev
print("Z_score: ",z_score)

if tail == 'two':
    p_value=2*(1-norm.cdf(abs(z_score)))
elif tail == 'left':
    p_value=norm.cdf(z_score)
elif tail=='right':
    p_value=1-norm.cdf(z_score)
else:
    raise ValueError("tail must be either 'two' 'right' 'left'")

print("p_value: ",p_value)
if(p_value<alpha):
    print("Null hypothesis REJECTED")
else:
    print("Null hypothesis ACCEPTED")