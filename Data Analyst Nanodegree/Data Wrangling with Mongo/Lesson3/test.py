import re
a = 'ABCDCDC'
b = 'CDC'
match = re.findall('(?='+b+')+',a)
print match
