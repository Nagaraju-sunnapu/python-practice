# program for demonstratng the regular expressions
import re
gd="abKpDw&8cLq@6PXzU6!amS"
sp="[abc]"
x=re.search(sp,gd)
if(type(x)!=None):
	print("start index={},end index={},value={}".format(x.start(),x.end(),x.group()))
else:
	print("search is unsuccessful")
	