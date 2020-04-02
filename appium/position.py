from selenium.webdriver.support.wait import WebDriverWait

from appium import webdriver
from time import sleep

# 查看包名adb logcat -v time | findstr START
desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '127.0.0.1:7555'
# 应用参数
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodekeyboard'] = True  # 支持输入中文
desired_caps['resetkeyboard'] = True
desired_caps['noReset'] = True

driver = webdriver.Remote('http://192.168.137.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(3)   # 隐式等待
# 显示等待
# WebDriverWait(driver, 20, 4).until(lambda x: x.find_element_by_id("xxx")).click()
# hit_seacher = driver.find_element_by_id("com.android.settings:id/search")
# hit_seacher.click()
# sleep(2)
#
# driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
# sleep(2)
# send_keys clear()  获取文本内容.text
# 获取位置和大小 .location .size 返回都是字典
# 获取属性值 .get_attribute(属性名)  resourceId classname content-desc->name
# driver.find_element_by_xpath("//*[@content-desc='收起']").click()
# 滑动swipe(x,y,x,y,总时间)   传坐标
# scroll 有 drag_and_drop 无 区别是否有惯性，都是先定位，传元素。
# sleep(1)
# 包含设的
cout = driver.find_elements_by_xpath("//*[contains(@text, '设')]")
print(len(cout))
for i in cout:
    print(i.text)

driver.quit()
