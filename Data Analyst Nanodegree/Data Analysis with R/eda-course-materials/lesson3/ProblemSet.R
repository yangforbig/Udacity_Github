# load diamonds data

library(ggplot2)
data("diamonds")

# histogram of variable price, largest peak at 604

ggplot(aes(x = price), data = diamonds) + 
  geom_histogram(binwidth =500) +
  scale_x_continuous() + 
  facet_grid(cut~., scales = "free_y")

by(diamonds$price, diamonds$cut, min)

# Create a histogram of price per carat
# and facet it by cut

diamonds$price_per_carat = diamonds$price / diamonds$carat

ggplot(data = diamonds, aes(x = price_per_carat)) + 
  geom_boxplot(bins = 50) + 
  scale_x_log10() + 
  facet_grid(cut~., scales = "free_y")

## Investigate the price of diamonds using box plots,
# numerical summaries, and one of the following categorical
# variables: cut, clarity, or color.

ggplot(data = diamonds, aes(x = color, y = price)) + 
  geom_boxplot()

by(diamonds$price, diamonds$color, summary)

IQR(subset(diamonds, color == 'J')$price)

# Carat Frequency Polygon

ggplot(data = diamonds, aes(x = carat)) + 
  geom_freqpoly(binwidth = 0.1) + 
  coord_cartesian(ylim = c(2000, 10000)) +
  coord_cartesian(xlim = c(0,2)) 
 
#
caratCount = table(diamonds$carat)
caratCount = caratCount[caratCount > 2000]

# data wrangling 

install.packages('devtools')
devtools::install_github('rstudio/EDAWR')
library(EDAWR)

install.packages('tidyr')
library(tidyr)

install.packages('dplyr')
library(dplyr)

install.packages('nycflights13')
library(nycflights13)

pollution %>% group_by('city') %>% 
  summarise(median = median(amount), sum = sum(amount), n = n())

#HIV data


gatherHiv <- gather(hiv, 'year', 'n', 2:34)



# date formates in r

dates <- c("05/27/84", "07/07/05")
betterDates <- as.Date(dates, format = "%m/%d/%y")

# birthday

birth = read.csv('pseudo_facebook.tsv', sep = '\t')

# how many people share my birthday 1991-02-23

subBirth = subset(birth, dob_day == 23 && dob_year == 1991 && dob_month == 2)

# how many brithdays in each month ?

month_count = table(birth$dob_month)
qplot(data = birth, x = dob_month) +
  scale_x_continuous(limits = c(0, 12), breaks = seq(1, 12, 1))



