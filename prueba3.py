import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.jccosmeticos.net/')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="post-1040"]/div/div[4]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div[1]/a/img').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="product-3222"]/div[1]/div/div[1]/div/div[2]/div/form/button').click()

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/div/div/div[1]/a/span[1]').click()

time.sleep(6)

driver.close()