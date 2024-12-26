# program for demonstrating the regular expressions
import re
sp="[A-Z]"
gd="abKpDw&8cLq@6PXzU6!amS"
x=re.finditer(sp,gd)
for i in x:
	print("start index:{},end index:{},value:{}".format(i.start(),i.end(),i.group()))