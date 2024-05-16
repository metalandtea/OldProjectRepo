
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#action Chains

from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

select_en = driver.find_element(By.ID,'langSelect-EN')
select_en.click()

driver.implicitly_wait(10)
#Cookie

cookie = driver.find_element(By.ID,"bigCookie")
cookies = driver.find_element(By.ID,"cookies")

#Upgrades (p means price)

upgrade_0p = driver.find_element(By.ID,"productPrice0")
upgrade_1p = driver.find_element(By.ID,"productPrice1")

#ACTIONS

chain_actions = ActionChains(driver)

#RUN ACTIONS IN LOOP

for i in range(5000):
    driver.implicitly_wait(.2)
  
    cookie_amt = int(cookies.text.split()[0])

    price_0 = int(upgrade_0p.text.split()[0])
    price_1 = int(upgrade_1p.text.split()[0])

    print(f"cookie amt: {cookie_amt}")

    chain_actions.click(cookie)

    if cookie_amt >= price_1:
        chain_actions.click(upgrade_1p)

    elif cookie_amt >= price_0:
        chain_actions.click(upgrade_0p)


    chain_actions.perform()
