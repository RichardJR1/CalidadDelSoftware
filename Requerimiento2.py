from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.jccosmeticos.net/')

driver.find_element('xpath', '//html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/div/div/form/div/button')

driver.implicitly_wait(20)

driver.close()
'''
<input type="text" placeholder="Search product..." name="s" class="ws">
'''