# intro to inferential statistics

1. marginal of error = sigma / sqrt(n) half width of CI

2. critical value of z 

3. Z-test works when we know mu and sigma

4. Cohen's D:
	d = (xbar - mu) / S
	

5. dependent T test: 
	
	Within-subjects designs:
		- two conditions
		- Pre-test, post-test
		- Growth over time (longitudinal study )
	
	
		
6. Type of Effect size Measures

- Differences Measure	
	Mean Difference
	standardized differences (Cohen's d)
- Correlation Measure
	r^2(coefficient of determination): proportion of variation in one variable that
	 is related to(explained by) another variable

	
7. statistical significance

- rejected null
- results are not likely due to chance (sampling error)

8. meaningfulness of results

(1) What was measured? variables - practical, theoretical, importance
(2) effect size
(3) can we rule out the random chance?
(4) can we rule out alternative explanation.


9. Result Section

(1) Descriptive Statistics ( M,SD)
- in text
- in graph
- in tables

(2) inferential Statistics
hypothesis test (alpha)

APA style, t(df) = x.xx, p = .xx, direction

APA style(CI), CI on the mean difference, 95%CI = (4,6)

Standard Error Mean (SEM) = S / sqrt(n)

CI: xbar +- t(critical)*margin of error


10.  two sample t-test: 

df = n1 + n2 - 2

11. pool the variance: Sp^2 = (SS1 + SS2) / (df1 + df2)


sd = sqrt(Sp^2/n1+Sp^2/n2)

t-test Assumption:

(1) X and Y should be random samples from two independent population.

(2) population are approximately normal

(3) sample data can estimate population variance

(4) population variances are roughly equal.

t-statistic = difference / (sd / sqrt(n))

print stats.t.interval(0.95,
                df = 9,
                loc = -3,
                scale = moe)
print stats.t.ppf(q=0.05, df=9)

stats.t.cdf(x= -2.5742, df= 49) * 2   

12. One-way ANOVA (Categorical vs Numerical Variables)

Between-Group Variability: the smaller the distance between sample means, 
the less likely population means will differ significantly.

Within-Group Variability: the greater variability of each individual sample, 
the less likely population means will differ significantly.

F: (between-group variability / within-group variability) = {(n∑(x(k)bar-x(G)bar)^2) / (k-1)} / {∑(x(i) - x(k)bar)^2 / (N-k)}
= {SS(between) / df (between)} / {SS(within) / df(within)} = MS(between) / MS(within)

The F distribution is positively skewed, which means it peaks on the left side and stretch out on the right side. peaks at 1

13. Multiple comparison test 

we don't know which one differ...

MS(within) = Sp

- Tukey's HSD (any two groups)

q• sqrt(MS(within)/n)   q:  Studentized Range Statistic 

sample size has to be the same.

- eta squared : proportion of total variation that is due to between-group differences (explained variation)

SS(Between) / SS(Total)

ANOVA assumption: 

- Normality: All the populations from which the samples are  normally distributed. Unless the sample size is large

- Homogeneity of variance. Unless the ratio of any two variances does not exceed 4

- independent observations (random assignment)

14. Find F critical value (Python)
import scipy.stats as stats
stats.f.ppf(q = 1-0.05, dfn=1, dfd=30)

15. pearson's r : 

r = COV(X,Y) / (Sx * Sy)

stats.pearsonr(X, Y)

r is sensitive to outliers

t = (r * sqrt(N -2 ) / sqrt(1 - r^2))
df = n -2 

a = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
b = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
from scipy.stats import linregress
linregress(a, b)


16. standard error of estimate 


17. t-test for slope

df = n -2 

18.

Z-test
t- test
ANOVA
Correlation
Regression
nonparametric test; do not require parametric info: like mean, std ---> Chi-squared Test 

19.  Chi-square for the goodness of fit at how well the expected value for certain variable 

Tests for Two Categorical Variables


Chi-square = ∑(fo - fe)^2 / fe

degree of freedom: Number of categories - 1

more categories, more degree of freedom.

The degrees of freedom for a test of independence equals the product of the number of categories in each variable minus 1.
In this case we have a 5x3 table so df = 4x2 = 8


20. Chi-square for independence

Cramer's V = sqrt(x^2 / ((k-1) * n)) k is the smaller number of rows or columns

check the table for effect size 


assumptions:

avoid dependent observations: the source of the data in the cells is different from the other cells.

avoid small expected frequencies(at least 5)


21. Python code for Chi-square tests


```
crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 4)   # Df = number of variable categories - 1

print("Critical value")
print(crit)

p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df=4)
print("P value")
print(p_value)

stats.chisquare(f_obs= observed,   # Array of observed counts
                f_exp= expected) 
                
```

```
# check variable independence
stats.chi2_contingency(observed = observed)

```
http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-25-chi.html





