import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.jccosmeticos.net/')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="menu-item-2358"]/a/span/span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="wpcf7-f6-p74-o1"]/form/p[1]/label/span/input').send_keys('Manuel')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="wpcf7-f6-p74-o1"]/form/p[2]/label/span/input').send_keys('MaNu@hotmail.com')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="wpcf7-f6-p74-o1"]/form/p[3]/label/span/input').send_keys('6593956')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="wpcf7-f6-p74-o1"]/form/p[4]/label/span/input').send_keys('Fallo en comparacion de productos')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="wpcf7-f6-p74-o1"]/form/p[5]/label/span/textarea').send_keys('Tuve un fallo al comparar dos cremas y un delineador')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="wpcf7-f6-p74-o1"]/form/p[6]/input').click()

time.sleep(6)


