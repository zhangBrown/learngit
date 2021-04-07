from selenium import webdriver
from time import sleep

search_text = ['练习','selenium',520]
for text in search_text:
    dr = webdriver.Firefox()
    dr.implicitly_wait(10)
    dr.get('http://www.baidu.com')
    dr.find_element_by_css_selector("#kw").send_keys(text)
    dr.find_element_by_css_selector("#su").click()
    sleep(2)
    dr.quit()
