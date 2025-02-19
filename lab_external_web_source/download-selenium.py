from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#driver.get("https://directory.enterprise-ireland.com/vendors")
#driver.get("https://directory.enterprise-ireland.com/vendors?limit=10&service=Cybersecurity")
#driver.get("https://directory.enterprise-ireland.com/vendors?limit=10&service=Cybersecurity&service=Enterprise%20Software")
driver.get("https://directory.enterprise-ireland.com/vendors?limit=10&language=English&service=Aerospace%20%26%20Aviation&service=Agriculture%20%26%20Equine&service=Automotive&service=Business%20Process%20Outsourcing&service=Construction%20Products&service=Construction%20Services&service=Construction%20Tech&service=Consumer%20Products")
time.sleep(7.7)

#print(driver.page_source)

elements = driver.find_elements(by=By.XPATH,value="//a[@href]")



# for element in elements:
#      print(element.get_attribute("href"))


links = driver.find_elements(By.TAG_NAME,'a')


for link in links:
     print(link.get_attribute('href'))

driver.close()