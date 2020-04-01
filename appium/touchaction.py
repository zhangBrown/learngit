from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver
import time

# 查看包名adb logcat -v time | findstr START
desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '127.0.0.1:7555'
# 应用参数
desired_caps['appPackage'] = 'com.pikachuclientproject'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://192.168.137.1:4723/wd/hub', desired_caps)

# 高级手势 tap轻敲 press按下 release抬手 wait等待 long_press长按
# move_to移动->手势解锁
wlan = driver.find_element_by_xpath("//*[@text='WLAN']")

TouchAction(driver).tap(wlan).perform()
TouchAction(driver).press(x=650, y=650).wait(2000).release().perform()
TouchAction(driver).long_press(x=650, y=650, duration=2000).perform()
TouchAction(driver).press(x=650, y=650).move_to(x=10, y=20)\
    .move_to(x=20, y=30).release().perform()
# 手机操作api get_window_size 获取手机分辨率 get_screenshot_as_file("screen.png")
# 获取网络network_connect 设置网络set_network_connect(0/1/2/4/6)
# 发送键到设备press_keycode() 百度搜索keycode数字
# 通知栏操作open_notifications()
print(driver.network_connection)
driver.press_keycode(4)     # 返回键
driver.open_notifications()

time.sleep(5)
driver.quit()
