from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.jccosmeticos.net/')

driver.implicitly_wait(1.5)

driver.find_element_by_xpath('//*[@id="post-1040"]/div/div[4]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/a').click()

driver.implicitly_wait(20)



