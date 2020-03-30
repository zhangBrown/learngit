from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.implicitly_wait(10)
dr.get('http://www.baidu.com')

first_handle = dr.current_window_handle  # 获取当前
dr.find_element_by_xpath("//div[@id='u1']/a[7]").click()
dr.find_element_by_link_text("立即注册").click()
all_handles = dr.window_handles  # 获取所有

for i in all_handles:
    if i != first_handle:
        dr.switch_to.window(i)
        dr.find_element_by_xpath("//input[@name='userName']").send_keys("username")
        sleep(3)
for i in all_handles:
    if i == first_handle:
        dr.switch_to.window(i)
        dr.find_element_by_id("kw").send_keys("selenium")
        sleep(3)
sleep(3)
dr.quit()