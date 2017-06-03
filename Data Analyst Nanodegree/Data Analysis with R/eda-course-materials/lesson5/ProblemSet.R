# 1. price histograms with facet and color 
# Create a histogram of diamond prices.
# Facet the histogram by diamond color
# and use cut to color the histogram bars.

# The plot should look something like this.
# http://i.imgur.com/b5xyrOu.jpg

# Note: In the link, a color palette of type
# 'qual' was used to color the histogram using
# scale_fill_brewer(type = 'qual')

ggplot(data = diamonds, aes(x = price)) + 
  geom_histogram(aes(fill = cut), position = 'fill') + 
  facet_wrap( ~ color) + 
  scale_fill_brewer(type = 'qual')

# Create a scatterplot of diamond price vs.
# table and color the points by the cut of
# the diamond.

# The plot should look something like this.
# http://i.imgur.com/rQF9jQr.jpg

# Note: In the link, a color palette of type
# 'qual' was used to color the scatterplot using
# scale_color_brewer(type = 'qual')

ggplot(data = diamonds, aes(x = table, y = price)) + 
  geom_point(aes(color = cut)) + 
  scale_colour_brewer(type = 'qual')

# color 
df_1 <- read.table(header = T, text = '
                 cond yval 
                   A   2
                   B   2.5
                   C   1.6')
df_2 <- read.table(header = T, text = '
                    cond1 cond2 yval
                      A      I 2
                      A      J 2.5
                      A      K 1.6
                      B      I 2.2
                      B      J 2.4
                      B      K 1.2
                      C      I 1.7
                      C      J 2.3
                      C      K 1.9
')

ggplot(data = df_1, aes(x = cond, y = yval)) + 
  geom_bar(stat = 'identity')

ggplot(data = df_2, aes(x = cond1, y = yval)) + 
  geom_bar(aes(fill = cond2), 
               stat = 'identity',
               color = 'black', 
               position = 'dodge',
              alpha = 1/2)

# Create a scatterplot of diamond price vs.
# volume (x * y * z) and color the points by
# the clarity of diamonds. Use scale on the y-axis
# to take the log10 of price. You should also
# omit the top 1% of diamond volumes from the plot.

# Note: Volume is a very rough approximation of
# a diamond's actual volume.

# The plot should look something like this.
# http://i.imgur.com/excUpea.jpg

# Note: In the link, a color palette of type
# 'div' was used to color the scatterplot using
# scale_color_brewer(type = 'div')

ggplot(data = diamonds, aes(x = volume, y = price)) + 
  geom_point(aes(color = clarity)) + 
  scale_y_log10()

# Many interesting variables are derived from two or more others.
# For example, we might wonder how much of a person's network on
# a service like Facebook the user actively initiated. Two users
# with the same degree (or number of friends) might be very
# different if one initiated most of those connections on the
# service, while the other initiated very few. So it could be
# useful to consider this proportion of existing friendships that
# the user initiated. This might be a good predictor of how active
# a user is compared with their peers, or other traits, such as
# personality (i.e., is this person an extrovert?).

# Your task is to create a new variable called 'prop_initiated'
# in the Pseudo-Facebook data set. The variable should contain
# the proportion of friendships that the user initiated.

# This programming assignment WILL BE automatically graded.

pf <- pf %>% 
  mutate(prop_initiated = friendships_initiated / friend_count )

# Create a line graph of the median proportion of
# friendships initiated ('prop_initiated') vs.
# tenure and color the line segment by
# year_joined.bucket.

# Recall, we created year_joined.bucket in Lesson 5
# by first creating year_joined from the variable tenure.
# Then, we used the cut function on year_joined to create
# four bins or cohorts of users.

# (2004, 2009]
# (2009, 2011]
# (2011, 2012]
# (2012, 2014]

ggplot(data = subset(pf, friend_count!=0), aes(x = tenure, y = prop_initiated)) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = median) + 
  geom_smooth()

#zoom in 0~500
ggplot(data = subset(pf, friend_count!=0), aes(x = tenure, y = prop_initiated)) + 
geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) + 
  geom_smooth()
  #coord_cartesian(xlim = c(0,500))

#Largest Group Mean prop_initiated

pf_sub = subset(pf, !is.na(prop_initiated))
with(subset(pf_sub, year_joined.bucket == "(2012,2014]"), mean(prop_initiated))

# Create a scatter plot of the price/carat ratio
# of diamonds. The variable x should be
# assigned to cut. The points should be colored
# by diamond color, and the plot should be
# faceted by clarity.

# The plot should look something like this.
# http://i.imgur.com/YzbWkHT.jpg.

# Note: In the link, a color palette of type
# 'div' was used to color the histogram using
# scale_color_brewer(type = 'div')

ggplot(data = diamonds, aes(y = price/carat, x = cut)) + 
  geom_point(aes(color = color), position = "jitter")+ 
  facet_wrap(~clarity) + 
  scale_color_brewer(type = 'div')

