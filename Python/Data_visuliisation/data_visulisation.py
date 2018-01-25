# Two main plotting in python:
# Matlibplot 
# ggplot
# ggplot works well with python
#
# grammar of graphics

import ggplot

ggplot(data,aes(xvar,yvar))

print ggplot(data, aes(xvar, yvar)) + geom_point(color = 'coral') + geom_line(color='coral') + \
      ggtitle('title') + xlab('x-label') + ylab('y-label')

# geom point = scatter, geom line = join everything up
# chose geometric objects to represent the data
# best to move to note books for this
