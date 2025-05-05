import math
from scipy import stats

#one sample t-test

sample_data=[12,15,14,10,13,14,15,16,14,13]
population_mean=13

t_statistic, p_value = stats.ttest_1samp(sample_data, population_mean)

print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")

print()   

# Two sample independent t-test (equal variance assumed)

group1=[23,21,19,24,25]
group2=[27,29,26,30,28]
 
#Hypothesis
# H0: The means of both groups are equal (mu1=mu2)
# H1: The means of both groups are different (mu1!=mu2)
t_stat_two,p_value_two=stats.ttest_ind(group1,group2,equal_var=True)
                                                                                                              
print("Two-sample t-test(Independent samples, equal variance):")
print("H0: mu1 = mu2")
print("H1: mu1!=mu2")
print(f"T-statistic = {t_stat_two:.4f}")
print(f"P-value = {p_value_two:.4f}")
