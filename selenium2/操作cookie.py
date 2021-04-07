'''
get_cookies():获取所有cookie信息
get_cookie(name):返回字典的key值为name的cookie信息
add_cookie(cookie_dict):添加cookie,'cookie_dict'值指字典对象。必须有name和value值
delete_cookie(name,optionString) name是要删除cookie，optionString是该cookie选项
delete_all_cookies()
'''
from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.implicitly_wait(10)
dr.get('http://www.baidu.com')
dr.set_window_size(600,600)

dr.find_element_by_css_selector("#kw").send_keys("selenium")
dr.find_element_by_css_selector("#su").click()
# 通过JavaScript设置浏览器窗口滚动条位置
js = "window.scrollTo(100,450);"
dr.execute_script(js)
# 窗口截图
dr.get_screenshot_as_file("D:\baidu.jpg")
# cookie = dr.get_cookies()
# print(cookie)

sleep(3)
dr.quit()