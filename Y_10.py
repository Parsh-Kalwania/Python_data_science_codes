from scipy import stats
gorup_a=[34,45,23,44,54,39,28]
group_b=[29,33,30,25,31,27,34]
stat,p_value=stats.ttest_ind(gorup_a,group_b)
print("T-statistic: ",stat)
print("P_value: ",p_value)
alpha=0.05
if p_value<alpha:
    print("Reject the null hypothesis: SIgnificant difference between A and B")
else:
    print("Fail to reject the null hypothesis: No significant difference between A and B")