from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from os import path


options = webdriver.ChromeOptions()

options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")

options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR") # 한국어!

chromedriver = path.expandvars(r'%LOCALAPPDATA%\Programs\Python\chromedriver.exe')
driver = webdriver.Chrome(chromedriver,chrome_options=options)
url = ""

driver.get("https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=20191030")

driver.find_element_by_xpath('//*[@id="wrap"]/table/tbody/tr/td[2]/div/div[4]/ol/li[1]/div[2]/div[1]/a').click()

driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div/a[1]').click()

is_see_more = True
see_more_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbox_module > div > div.u_cbox_paginate > a')))
while is_see_more:
    try:

        see_more_button.click()

    except NoSuchElementException as e:
        print('exception',e)
        is_see_more = False
    except ElementNotInteractableException as e:
        print('exception',e)
        is_see_more = False
    except ElementClickInterceptedException as e:
        print('exception',e)

res = driver.find_elements_by_class_name('u_cbox_contents')
#res = driver.find_element_by_xpath('.//*[@class=\"u_cbox_contents\"]')
for com in res:
    print(com.text)
#f = open("comments_naver.txt",'w')
#f.write(res.text);
#f.close();



#driver.close()
