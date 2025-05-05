import numpy as np
from scipy.stats import chi2_contingency as cc

observed=np.array([[35,52.5,12.5],[28.1,42.1,9.8],[6.9,10.4,2.7]])

#Chi-square test

chi2_stat,p_value,dof,expected=cc(observed)
print("Chi-square test of independence")
print("-------------------------------")
print(f"Chi-square statisitic = {chi2_stat:.4f}")
print(f"Degrees of freedom = {dof}")
print(f"P-value = {p_value:.4f}")
print("\nExpected Frequencies: ")
print(expected)
alpha=0.05
if p_value<alpha:
    print("\nReject the null hypothesis: There is a significant association between variables")
else:
    print("\nFail to reject the null hypothesis: No significant association between vairables")
