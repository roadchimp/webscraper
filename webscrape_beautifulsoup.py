#advanced HTML parser that can extract tags
from bs4 import BeautifulSoup
from urllib.request import urlopen

my_address = "http://www2.travelerbuddy.com/index.html"

html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')
my_soup = BeautifulSoup(html_text, "html5lib")

#strip out tags
#print(my_soup.get_text())

#print attributes
# print(my_soup.title.get_text())



#find all instances of a particular tag
#print(my_soup.find_all("img", src="img/home/4/feature-main.png"))
print(len(my_soup.find_all("img")))
#rint(my_soup.find_all("a"))


# print(my_soup)