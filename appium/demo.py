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

print(driver.current_package)
print(driver.current_activity)

time.sleep(3)

driver.start_activity("com.android.settings", ".Settings")

time.sleep(3)

driver.close_app()

# if driver.is_app_installed(包名):
#     driver.remove_app(app_id
# else:
#     driver.install_app(包名)
# 将应用置于后台(秒)，用于热启动
driver.background_app(5)

driver.quit()