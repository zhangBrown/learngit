'''
遇到frame/iframe表单嵌套页面的定位
通过switch_to.frame() 可以直接取id或者name属性   先找到<iframe>标签，再定位
'''
from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.implicitly_wait(10)
dr.get("http://mail.163.com")

fr = dr.find_element_by_xpath("//div[@id='loginDiv']/iframe")
dr.switch_to.frame(fr)
sleep(2)
dr.find_element_by_xpath("//input[@name='email']").send_keys("13631289205")
sleep(2)
dr.switch_to.default_content()  # 切换到默认(最外层)表单
dr.find_element_by_link_text("企业邮箱").click()

sleep(3)
dr.quit()