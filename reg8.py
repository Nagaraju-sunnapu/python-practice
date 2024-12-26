# program for demonstrating the regular expressions
import re
sp=r"\S"
gd="abKpDw&8cLq@6PXzU6!amS"
x=re.findall(sp,gd)
print(x)