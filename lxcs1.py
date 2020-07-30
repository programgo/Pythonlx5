from selenium import webdriver

# driver = webdriver.Chrome()
for i in range(10):
    driver = webdriver.Chrome()
    driver.get("https://yjzch.mti-sh.cn/#/home")
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[1]/div/div/input').send_keys('csa')
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[2]/div/div/input').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[3]/div/button/span').click()
    driver.implicitly_wait(5000)
    driver.quit()