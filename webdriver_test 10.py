from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.jccosmeticos.net/')

driver.implicitly_wait(1.5)

driver.find_element_by_xpath('//*[@id="menu-item-2358"]/a').click()

driver.implicitly_wait(20)





