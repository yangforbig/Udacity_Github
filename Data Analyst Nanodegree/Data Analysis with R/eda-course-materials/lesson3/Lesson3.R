pf = read.csv('pseudo_facebook.tsv', sep = '\t')
names(pf)

ggplot(aes(x = dob_day), data = pf) + 
  geom_histogram(binwidth = 0.5) + 
  scale_x_continuous(breaks = 1:31) +
  theme_set(theme_minimal(24)) 

# histogram of ages for each gender
ggplot(aes(x = age), data =pf) + 
  geom_histogram(binwidth = 0.5) +
  facet_grid(. ~ gender) 


ggplot(data = pf, aes(x = dob_day)) + 
  geom_histogram(binwidth = 1) + 
  scale_x_continuous(breaks = 1:31) + 
  facet_wrap(~dob_month)

# friend count 
ggplot(data = subset(pf, !is.na(gender)), aes(x = friend_count)) +
  geom_histogram(binwidth = 25) +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) + 
  facet_grid(~gender)
  
table(pf$gender)
by(pf$friend_count, pf$gender, summary)

# tenure 

qplot(x = tenure/365, data = pf, color = I('black'), fill = I("#1E90FF")) +
  scale_x_continuous(limits = c(0, 7), breaks = seq(0, 7, 1)) + 
  xlab("number of years using FB") + 
  ylab("number of users")

# age 
qplot(x = age, data = pf, binwidth = 1, color = I('black'), fill = I('#E6E6FA')) + 
  scale_x_continuous(limits = c(10, 80), breaks = seq(10, 80, 5)) 

# girdExtra for friend_count 
install.packages("gridExtra")
library(gridExtra)
library(ggplot2)

p1 <- ggplot(data = subset(pf, !is.na(gender)), aes(x = friend_count)) +
  geom_histogram()# +
  #scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50))

p2 <- p1 + scale_x_log10()

p3 <- p1 + scale_x_sqrt()

grid.arrange(p1, p2, p3)

# which gender makes mpre likes on www

ggplot(data = subset(pf, !is.na(gender)), aes(x = www_likes, y = ..count../sum(..count..))) + 
  geom_freqpoly(aes(color = gender), binwidth = 20) + 
  scale_x_continuous(limits = c(5000, 15000)) 

by(pf$www_likes, pf$gender, sum)

# boxplot of www_likes for each gender

qplot(x = gender, y = friendships_initiated, data = subset(pf, !is.na(gender)), geom = 'boxplot')  
  #coord_cartesian(ylim= c(0, 25))

#
mobile_checkin <- ifelse(pf$mobile_likes > 0, 1, 0)
pf$mobile_checkin <- factor(mobile_checkin)
sum(pf$mobile_checkin) / leng(pf$mobile_checkin)






















