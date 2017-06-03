# Prive vs x

ggplot(data = diamonds, aes(x = x, y = price)) + 
  geom_point(alpha = 1/15)

# correlation

with(diamonds, cor.test(x, price))
with(diamonds, cor.test(y, price))
with(diamonds, cor.test(z, price))


#price v. depth

ggplot(data = diamonds, aes(x = price, y = depth)) + 
  geom_point(alpha = 1 / 20)

# # Change the code to make the transparency of the
# points to be 1/100 of what they are now and mark
# the x-axis every 2 units. See the instructor notes
# for two hints.

ggplot(data = diamonds, aes(x = price, y = depth)) + 
  geom_point(alpha = 1/100) + 
  scale_x_continuous(limits = c(326, 18823))

# correlation , price vs depth 

with(diamonds, cor.test(price, depth))

# Create a scatterplot of price vs carat
# and omit the top 1% of price and carat
# values.

ggplot(data = diamonds, aes(x = carat, y = price)) + 
  geom_point() +
  xlim(0, quantile(diamonds$carat, 0.99)) +
  ylim(0, quantile(diamonds$price, 0.99))


# Create a scatterplot of price vs. volume (x * y * z).
# This is a very rough approximation for a diamond's volume.

# Create a new variable for volume in the diamonds data frame.

diamonds$volume <- diamonds$x * diamonds$y * diamonds$z
ggplot(data = diamonds, aes(x = volume, y = price)) + 
  geom_point(alpha = 1 / 100) + 
  geom_smooth(method = 'lm', formula = y ~ x + I(x^2), color = 'blue')
  
#Correlations on Subsets

with(subset(diamonds, volume !=0 & volume <= 800), cor.test(price, volume))


subset(diamonds, volume !=0 & volume >= 800)

# linear model to fit the plot

sub.diamonds <- subset(diamonds, volume != 0 & volume <= 800)

ggplot(data = sub.diamonds, aes(x = volume, y = price)) + 
  geom_point() + 
  geom_smooth(method = 'lm', formula = y ~ x + I(x^2), color = 'blue')

# Use the function dplyr package
# to create a new data frame containing
# info on diamonds by clarity.
# Name the data frame diamondsByClarity
# The data frame should contain the following
# variables in this order.
#       (1) mean_price
#       (2) median_price
#       (3) min_price
#       (4) max_price
#       (5) n
# where n is the number of diamonds in each
# level of clarity.

diamondsByClarity <- diamonds %>% 
  group_by(clarity) %>%
  summarise(mean_price = mean(price), median_price = median(price),
            min_price = min(price), max_price = max(price), n = n()) %>%
  arrange(mean_price)

# We’ve created summary data frames with the mean price
# by clarity and color. You can run the code in R to
# verify what data is in the variables diamonds_mp_by_clarity
# and diamonds_mp_by_color.

# Your task is to write additional code to create two bar plots
# on one output image using the grid.arrange() function from the package
# gridExtra.

library(gridExtra)

diamonds_by_color <- group_by(diamonds, color)
diamondsByColor <- summarise(diamonds_by_color, mean_price = mean(price))

