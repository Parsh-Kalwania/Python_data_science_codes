import numpy as np
import scipy.stats as stats

#Z-test(binary: Conversions)

conversions_a=200
conversions_b=240
total_a=1000
total_b=1000

#Conversion rates

p_a=conversions_a/total_a
p_b=conversions_b/total_b
print(f"Z-test: Conversion Rate A = {p_a:.4f}, Conversion Rate B = {p_b:.4f}")

#Pooled probability fo z-test

p_pool=(conversions_a + conversions_b)/(total_a+total_b)

# Standard error and z-score

se_z=np.sqrt(p_pool*(1-p_pool)*(1/total_a+total_b))
z_score=(p_a-p_b)/se_z
p_value_z=2*(1-stats.norm.cdf(abs(z_score)))
print(f"Z-score = {z_score:.4f}")
print(f"P-value (z-test) = {p_value_z:.4f}")
if p_value_z<0.05:
    print("Z-test Result: Statistically significant differnce")
else:
    print("Z-test result: No statistically significant difference")
    