# Web Scraper code
import requests
import random
from bs4 import BeautifulSoup

# list of user agents to resolve 403 forbidden error
userAgents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.1',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.1',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3']

# requests
website = "https://hamishandandy.com/shop/"
html_data = requests.get(website, headers={'User-Agent': random.choice(userAgents)})

#print(html_data.text)

# Parse HTML Code
# create beautiful soup object
soup = BeautifulSoup(html_data.content, "html.parser")

shop_elements = soup.find_all("div", class_="c-product-tile__wrap")
print(shop_elements)

for element in shop_elements:
    product_element = element.find_all("h5")
    stock_element = element.find_all("span", class_="soldout-tag")
    print(product_element, end="\n"*2)
    print(stock_element, end="\n"*2)
    