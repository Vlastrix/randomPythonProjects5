from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep

FORM_URL = "https://forms.gle/aqEq3a4tex2BQsvH8"
LISTINGS_URL = "https://www.zillow.com/homes/San-Francisco,-CA_rb/"
listings_link_list = []
listings_price_list = []
listings_address_list = []

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Forwarded-For": "190.186.23.2",
    "X-Http-Proto": "HTTP/1.1",
}

driver.maximize_window()
driver.get(LISTINGS_URL)

sleep(2)

scr1 = driver.find_element_by_xpath('//*[@id="search-page-list-container"]')
for number in range(4):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight / 4", scr1)
    sleep(2)

webpage = driver.page_source
sleep(1)
driver.quit()

soup = BeautifulSoup(webpage, 'html.parser')

links_of_listings = soup.find_all(name="a", class_="list-card-img")

for listing in links_of_listings:
    link = listing.get("href")
    listings_link_list.append(link)

price_of_listings = soup.select(selector=".list-card-heading div")

for price in price_of_listings:
    listing_price = price.text
    listings_price_list.append(listing_price)

address_of_listings = soup.select(selector=".list-card-link-top-margin address")

for address in address_of_listings:
    address_text = address.text
    listings_address_list.append(address_text)

print(len(listings_price_list))
print(len(listings_link_list))
print(len(listings_address_list))

driver.get(FORM_URL)

for n in range(len(listings_link_list)):
    sleep(1)
    form_inputs = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    submit_button = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    form_inputs[0].send_keys(listings_address_list[n])
    form_inputs[1].send_keys(listings_price_list[n])
    form_inputs[2].send_keys(listings_link_list[n])
    submit_button.click()
    sleep(1)
    another_response_button = driver.find_element_by_link_text("Enviar otra respuesta")
    another_response_button.click()
