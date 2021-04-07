from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.get("http://www.baidu.com")
dr.maximize_window()  # 窗口最大化
title = dr.title  # 打印当前页面
now_url = dr.current_url  # 打印当前页面url
print(title,now_url)
sleep(3)
# clear()清除文本 send_keys模拟按键输入   click()单击元素  submit()回车
dr.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
# 获取输入框尺寸
# size = dr.find_element_by_css_selector("#kw").size
# print(size)
# 获取文本        获取元素属性get_attribute("xx")      判断指定元素是否显示is_displayed("xx")
text = dr.find_element_by_css_selector("[id=cp]").text
print(text)
dr.find_element_by_xpath("//input[@type='submit']").click()
'''
sleep(3)
dr.refresh()  # 刷新当前页面
dr.back()  # 返回网页
sleep(3)
dr.forward()  # 前进网页
'''
sleep(3)
dr.quit()

