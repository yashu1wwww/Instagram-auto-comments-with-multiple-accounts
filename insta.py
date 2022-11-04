from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(3)
driver.find_element_by_name('username').send_keys('dlopoele') #enter your insta acc
driver.find_element_by_name('password').send_keys('fff123$%') #enter your insta pass
#note no two factor authentication is on when automation goes create another insta acc
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(9)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
driver.implicitly_wait(6)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()


sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()


sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(3)

driver.close()

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(3)
driver.find_element_by_name('username').send_keys('usernone212') #replace with your insta acc
driver.find_element_by_name('password').send_keys('pass7#$%') #replace with your insta password
#note no two factor authentication is on when automation goes create another insta acc
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(9)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
driver.implicitly_wait(6)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()


sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()


sleep(4)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

driver.close()






