from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#download chromedriver from here "https://sites.google.com/a/chromium.org/chromedriver/downloads" and move it to this path
path="C:\\Python27\\selenium\\webdriver\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com")

#provide username and password of account
username=""
password=""

driver.find_element_by_link_text('Log in').click()

elem = driver.find_element_by_name("username")
elem.send_keys(username)

elem1 = driver.find_element_by_name("password")
elem1.send_keys(password)

#Clicking Login Button
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button").click()

#Removing Notification Popup
run_test = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@class='_dcj9f']")))
run_test.click()

search=driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
search.send_keys("b")
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@class='_gimca']")))
result=driver.find_elements_by_xpath("//*[@class='_gimca']")
all_links=[]

for element in result:
	if 'tags' not in element.get_attribute('href'):
		all_links.append(element.get_attribute('href'))

for i in all_links:
	driver.get(i)
	#WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@class='_qv64e _gexxb _r9b8f _njrw0']")))
	try:
		follow=driver.find_element_by_xpath("//*[@class='_qv64e _gexxb _r9b8f _njrw0']")
		follow.click()
	except Exception,e:
		print "Already Following"
		
#driver.close()
#driver.quit()
