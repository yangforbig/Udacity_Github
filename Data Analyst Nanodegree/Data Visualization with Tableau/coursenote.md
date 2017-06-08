Lesson 1 Data Visualization Fundamentals
 
1. For quantitative data, especially when comparing two variables, dots are preferred.

2. Since humans see trends from lines, it's inappropriate to use lines when a trend doesn’t make sense.

3.  Color is often used to encode a third dimension since it is really difficult 
	to interpret three dimensional data on a two dimensional plane
	
4.  [Great Article about Visual Encoding](https://www.perceptualedge.com/articles/b-eye/encoding_values_in_graph.pdf)
<<<<<<< HEAD

5.  Choropleths use color to encode another value associated with the location on the map 
such as population, population density, GDP, etc. 
Cartograms are similar to choropleths, but distort the boundaries of regions - 
such as countries - to encode a value, typically along with some color encoding

6.  [Data Visualization: Rules for Encoding Values in Graph ](http://extremepresentation.typepad.com/blog/2015/01/announcing-the-slide-chooser.html)

7.  [Selecting the Right Graph for Your Message](http://www.perceptualedge.com/articles/ie/the_right_graph.pdf)


8. Bullet graph



![Bullet graph](https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57d35099_bullet-graph/bullet-graph.png)

9. Sparkline

Edward Tufte introduced these in Visual Display of Quantitative Information (along with naming small multiples) 

as a way to succinctly visualize some quantity changing over time

![Sparkline](https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57f4233e_sparkline-chart/sparkline-chart.png)


10. Sequential palettes

Sequential palettes have a smooth transition from light to dark or dark to light. 
These are great for continuous data that is all positive 
so low values are light and high values are dark (or the other way around if you prefer). 
Here's an example of a sequential palette going from light to dark red.

11. Diverging palettes

When you're working with data that has some breakpoint, 
values that go from negative to positive for example, 
it is typically best to use a diverging palette.
 Diverging palettes transition from one color to another, 
 passing through a light (or dark) color with the luminance shifting linearly through the palette. 
 You've seen one already, the palette that went from red to green.

12. [I want hue](http://tools.medialab.sciences-po.fr/iwanthue/) is a great tool for building optimally distinct palettes

13.   Try to stay away from red-green palettes and use blue-orange instead in case of colorblindness 

14.  chart junk :When designing your visualizations, you need to take care to remove anything that distracts from the data

15. Data Ink

Even without chart junk, many graphs devote a lot of visual space to non-data elements.
 Tufte uses the term ink to refer to any visual element in the figure.
  Visual elements that encode data are data-ink, and everything else is non-data-ink. 
As designers, we should strive to reduce the amount of non-data-ink to remove distractions from the data.

16.  [This article](http://www.storytellingwithdata.com/blog/2014/01/multifaceted-data-and-story) is a good example of how your story can change by emphasizing different visual elements
