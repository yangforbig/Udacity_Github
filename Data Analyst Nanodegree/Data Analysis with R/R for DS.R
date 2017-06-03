library(tidyverse)
mpg
str(mpg)

ggplot(data = mpg, aes(x = displ, y = hwy, color = class)) + 
  geom_point()
?mpg
