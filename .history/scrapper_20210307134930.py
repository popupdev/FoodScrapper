from selenium import webdriver
import urllib
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
word = "coffee"
url = "http://images.google.com/search?q="+word+"&tbm=isch&sout=1"
driver.get(url)
imageXpathSelector = '//*[@id="ires"]/table/tbody/tr[1]/td[1]/a/img'
img = driver.find_element_by_xpath(imageXpathSelector)

src = (img.get_attribute('src'))
urllib.urlretrieve(src, word+".jpg")
driver.close()
