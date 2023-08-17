from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# Set up a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Navigate to Pinterest login page
login_url = "https://www.pinterest.com/"
driver.get(login_url)

# Find the email/username and password input fields and fill them in
elements = driver.find_elements(By.ID ,"fullpage")


# Get the fully rendered HTML content
# page_source = driver.page_source

# Close the browser
for e in elements:
    print(e.text)

# Now you can parse and extract the content using BeautifulSoup
# soup = BeautifulSoup(page_source, 'html.parser')
# Your parsing and scraping code here

# Print the text content
# print(soup.get_text())
