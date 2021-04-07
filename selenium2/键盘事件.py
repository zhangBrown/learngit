from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

dr = webdriver.Firefox()
dr.implicitly_wait(5)
dr.get('http://www.baidu.com')

dr.find_element_by_xpath("//*[@id='kw']").send_keys("seleniumm")
sleep(3)
'''
dr.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.BACK_SPACE)  # 删除多输入一个m
dr.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.SPACE)  # 空格
sleep(3)
'''
dr.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.CONTROL,'a')  # 全选输入框
dr.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.ENTER)  # 回车
