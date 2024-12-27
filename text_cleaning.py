# program for demonstrating the removing the punctuation
import re
def text_punctuation(text):
	clean_text=re.sub(r"[^\w\s]","",text)
	clean_text=clean_text.lower()
	return clean_text
text=input("enter a text:")
print(text_punctuation(text))