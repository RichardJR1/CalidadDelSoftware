import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.jccosmeticos.net/')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="post-1040"]/div/div[4]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/a').click()

time.sleep(6)

driver.close()