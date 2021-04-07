# 鼠标操作
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

dr = webdriver.Firefox()
dr.implicitly_wait(5)
dr.get("https://www.baidu.com/")
moreLoc = dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[8]")
ActionChains(dr).move_to_element(moreLoc).perform()
sleep(2)
dr.find_element_by_xpath("//div[@class='bdpfmenu']/a[1]").click()
sleep(2)
dr.find_element_by_class_name("prefpanelgo").click()
sleep(2)
# 通过switch_to 警告框处理，保存文本
a = dr.switch_to.alert.text
print(a)
# accept()接受现有警告框       dismiss()解散警告框
dr.switch_to.alert.accept()
dr.close()