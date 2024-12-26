# program for demonstrating the regular expressions
import re
x=re.finditer(".","KVKKVKKKVKV")
for i in x:
	print("start index:{},stop index:{},value:{}".format(i.start(),i.end(),i.group()))