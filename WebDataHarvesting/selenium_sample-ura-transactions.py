import time

# install selenium package via `pip install selenium`
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

# download driver for your own platform and browser from `https://www.selenium.dev/downloads/`. (need to expand the `Browser` section on the page)
browser = webdriver.Chrome('C:/Users/xingz/Downloads/chromedriver_win32/chromedriver')
browser.maximize_window()  
browser.get("https://www.ura.gov.sg/realEstateIIWeb/transaction/search.action")  

# wait for page to load

WebDriverWait(browser, 10).until(lambda x: x.find_element_by_id("searchForm"))

# now set values for the search-by-district form

time.sleep(1)

# scroll down a bit
browser.execute_script("window.scrollTo(0, 512)")

time.sleep(1)

# select `Search by property type and postal district` tab
district_tab = browser.find_element_by_xpath("//li[@role='presentation']/a[@href='#district']")
district_tab.click()

time.sleep(1)

# select date of sale (from)
search_from_select = Select(browser.find_element_by_id("searchForm_selectedFromPeriodPostalDistrict"))
search_from_select.select_by_index(12)

time.sleep(1)

# select date of sale (to)
search_to_select = Select(browser.find_element_by_id("searchForm_selectedToPeriodPostalDistrict"))
search_to_select.select_by_index(3)

time.sleep(1)

# select `Apartments & Condominiums`
#apartment_radio = browser.find_element_by_id("radio3ac")
apartment_radio = browser.find_element_by_xpath("//label[@for='radio3ac']")
apartment_radio.click()

time.sleep(1)

# select `New Sale`
#new_sale_check = browser.find_element_by_id("checkbox4")
new_sale_check = browser.find_element_by_xpath("//label[@for='checkbox4']")
new_sale_check.click()

time.sleep(1)

browser.execute_script("window.scrollTo(0, 1024)")

time.sleep(1)

# select district 9 & 10
district_09 = browser.find_element_by_id("addToPostal_8")
district_09.click()

time.sleep(1)

district_10 = browser.find_element_by_id("addToPostal_9")
district_10.click()

time.sleep(1)

# click search!
search_btn = browser.find_element_by_id("transSearchPd")
search_btn.click()

# switching page, wait a bit longer
time.sleep(3)

# click `download as csv`
download_csv_btn = browser.find_element_by_xpath("//input[@value='Download into CSV']")
download_csv_btn.click()

# download in progress
time.sleep(5)

browser.close()
