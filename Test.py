from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://rackedu.com/')

driver.implicitly_wait(1.5)

driver.close()
