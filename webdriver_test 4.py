from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

achains = ActionChains(driver)

driver.get('https://www.jccosmeticos.net/')   

menubuttons = driver.find_element(By.XPATH,'//*[@id="post-1040"]/div/div[4]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/a/img[2]')

achains.move_to_element(menubuttons).perform()

driver.implicitly_wait(2)

driver.find_element(By.XPATH,'//*[@id="post-1040"]/div/div[4]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div/a').click

driver.implicitly_wait(20)





