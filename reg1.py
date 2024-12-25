# program for demonstrating the regular expressions
import re
gd="abKpDw&8cLq@6PXzU6!amS"
sp="[abc]"
x=re.finditer(sp,gd)
for i in x:
	print("start index:{},end index:{},value:{}".format(i.start(),i.end(),i.group()))