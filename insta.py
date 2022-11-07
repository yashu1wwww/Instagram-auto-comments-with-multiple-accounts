#here i added 2 auto accounts which auto login and put comments to the post if you want more comments in diff accounts means copy line from 78 to 148 and paste in 150 line and dont forgot to replace insta username & password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(5)
driver.find_element_by_name('username').send_keys('dlopohjuh') #replace with your insta username 
driver.find_element_by_name('password').send_keys('ytfg123$%') #replace with your insta pass
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(9)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
driver.implicitly_wait(6)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(5)

driver.close()

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(5)
driver.find_element_by_name('username').send_keys('user123') #replace with your insta username 
driver.find_element_by_name('password').send_keys('buck@#$%') #replace with your insta password
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(9)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
driver.implicitly_wait(6)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()

driver.close()
