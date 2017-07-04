Jun 20 2017

Lesson 1 Data Analysis Process 
| Process | Explanation|
----------|------------|
|Question Phase| For example: Characteristics of Student who pass projects.<br> How to store market so that people can buy their preferred products|
|Wrangling Phase| 1. Data Acquisition 2. Data Cleaning |
|Exploration Phase| Build Intuition and Find Patters|
|Draw Conclusion Phase| Prediction and Conclusion(statistics and machine learning)|
|Communication Phase|Blog post, data visualization |
 
 
 
 

Articles to start:

Applications of Data Analysis

Paper by Facebook on exposure to ideologically diverse information
OKCupid blog post on the best questions to ask on a first date
How Walmart used data analysis to increase sales
How Bill James applied data analysis to baseball
A pharmaceutical company uses data analysis to predict which chemical compounds are likely to make effective drugs

1. in Python csv file is commonly represented as a list of rows

- each row is a list 
- each row is a dictionary (when the csv file has header)

```
daily_engagement_filename = 'daily_engagement.csv'
def read_data(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data
daily_engagement = read_data('daily_engagement.csv')


```

2. csv doesn't convert data type 



3. Draw conclusions Phase

	Prove the difference due to to the noise or the truth. --> statistics
	
4. Correlation does not imply causation --> A/B test

	an online experiment to determine whether one factor cause the another.
	

Data Science

- similar to data analysis

- more focused on building systems

- may require more experience

Data Engineering

- More focus on data wrangling 

- Involve data storage and processing 


Big Data

- Fuzzy term for 'a lot of data'


#Lesson 2

1. Numpy Arrays and Python List

|Similarities|Difference|
|------------|----------|
|Access elements by position| Each item should have same dtpye|
|Access a range of elements by slicing|Convenient functions|
|Use loop| Multi-dimensional|

2. 


Np.array.argmax()  ---> index of the maximum value 

3. Vectorized Operations

4. +, +=

+=: operate in place while + not

5. numpy array has different behavior than python list.

numpy does not create a new arrray when slice the array.


6. Panda Series vs Numpy array

s.describe()
implemented in C (faster)

pandas has index


7.

if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    print s1 + s2

# Indexes do not overlap
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
    print s1 + s2


Series.apply(func) --> apply the function to each cell in the Series

#Lesson 3

1. df.apply(), df.applymap()

df.apply(), apply the function to each column in dataframe
df.applymap(), apply the function to each cell in dataframe.


grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

# Change False to True for this block of code to see what it does

# DataFrame apply()
```
if True:
    def convert_grades_curve(exam_grades):
        # Pandas has a bult-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        return pd.qcut(exam_grades,
                       [0, 0.1, 0.2, 0.5, 0.8, 1],
                       labels=['F', 'D', 'C', 'B', 'A'])
        
    # qcut() operates on a list, array, or Series. This is the
    # result of running the function on a single column of the
    # DataFrame.
    print convert_grades_curve(grades_df['exam1'])
    
    # qcut() does not work on DataFrames, but we can use apply()
    # to call the function on each column separately
    print grades_df.apply(convert_grades_curve)
```

df.add(s, axis='index')

The functions sub(), mul(), and div() work similarly to add()

2. 
df_1.merge(df_2,
		   left_on = [],
		   right_on = [],
		   how = '')
		   
3D data --> pd.panel

3.

a = [['a', '1.2', '4.2'], ['b', '70', '0.03'], ['x', '5', '0']]
df = pd.DataFrame(a, columns=['one', 'two', 'three'])
df
Out[16]: 
  one  two three
0   a  1.2   4.2
1   b   70  0.03
2   x    5     0

df.dtypes
Out[17]: 
one      object
two      object
three    object

df[['two', 'three']] = df[['two', 'three']].astype(float)

df.dtypes
Out[19]: 
one       object
two      float64
three    float64

# Extra

1. Regular Expression

Python offers two different primitive operations based on regular expressions:
match checks for a match only at the beginning of the string,
while search checks for a match anywhere in the string

re.match(pattern, string, flags=0)



re.sub(pattern, repl, string, max=0)

June 27 2017

