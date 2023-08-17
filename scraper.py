from selenium import webdriver
from bs4 import BeautifulSoup

# Set up a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = "https://www.pinterest.com/search/pins/?q=fashion"  # Example URL
driver.get(url)

driver.implicitly_wait(10)  

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')
text = soup.get_text()

print(text)
