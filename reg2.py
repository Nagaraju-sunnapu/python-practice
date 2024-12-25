# program for demonstrating the regular expressions
import re
gd="abKpDw&8cLq@6PXzU6!amS"
sp="[abc]"
x=re.findall(sp,gd)
print(x)