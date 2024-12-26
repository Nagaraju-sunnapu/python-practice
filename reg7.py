# program for demonstrating the regular expressions
import re
gd="abKpDw&8cLq@6P XzU6!amS"
x=re.finditer(r"\s",gd)
for i in x:
	print("start index:{},end index:{},value:{}".format(i.start(),i.end(),i.group()))