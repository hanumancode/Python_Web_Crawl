from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#tabularize and turn result of url request into a dataset
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

#opening up connection, grabbing the page
uClient = uReq(my_url)

#stores content to a variable
page_html = uClient.read() 

uClient.close() 

#parse html using soup function
#parse html and store it into page_soup variable
page_soup = soup(page_html, "html.parser") 


#find all divs that have the class 'item-container'
containers = page_soup.findAll("div",{"class":"item-container"})

#check length of the containers
len(containers)

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()


	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()	

