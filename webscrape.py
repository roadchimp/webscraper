from urllib.request import urlopen
import re #regex support 


#parse the index.html page
my_address = "http://www2.travelerbuddy.com/index.html"
html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')

#find text within specific tags
start_tag = "<title>"
end_tag = "</title>"
start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)
#print(html_text[start_index:end_index])

#search for text that matches a particular string and remove it
match_results = re.search("Lorem ipsum .*?.*ullam.", html_text, re.IGNORECASE)
title = match_results.group()
title = re.sub("Lorem ipsum", "", title) #remove text
print(title)

