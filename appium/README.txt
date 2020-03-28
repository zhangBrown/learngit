3-28
appium
	java环境
		安装，配置环境变量java_home class_path path
	ad sdk环境
		解压到任意目录，不能有中文
		配置ANDROID_HOME D:\sdk 
			path % ANDROID_HOME%\tools % ANDROID_HOME%\platform-tools
	安卓模拟器
	adb
		获取包名、界面名
		获取app启动时间
			adb shell am start -w 包名/启动名
		获取日志
			adb logcat     E开头的是error
		其他
			adb --help
	appium
		安装appium客户端 v1.10.1 选择simple 0.0.0.0 4723 start server
		安装python库 pip install Appium-Python-Client
		编写代码
			from appium import webdriver
			import time

			# 查看包名adb logcat -v time | findstr START
			desired_caps = dict()
			desired_caps['platformName'] = 'Android'
			desired_caps['platformVersion'] = '6.0.1'
			desired_caps['deviceName'] = '127.0.0.1:7555'
			desired_caps['appPackage'] = 'com.pikachuclientproject'
			desired_caps['appActivity'] = '.MainActivity'

			driver = webdriver.Remote('http://192.168.137.1:4723/wd/hub', desired_caps)

			time.sleep(3)

			driver.quit()
	
