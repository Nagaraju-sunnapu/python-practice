# program for demonstrating the regular expressions
import re
x=re.finditer("K*","KVKKVKKKVKV")
for i in x:
	print("start index:{},end index:{},value:{}".format(i.start(),i.end(),i.group()))