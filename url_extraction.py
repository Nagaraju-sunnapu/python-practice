# program for demonstrating the url extraction by using the regular expressions
import re
def url_extraction(url):
	if(re.search(r"(https://[^\s]+)",url)):
		print("valid url")
	else:
		print("invalid url")
url=input("enter url:")
url_extraction(url)