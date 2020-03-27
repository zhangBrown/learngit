import uiautomator2 as u2
from time import sleep
import os

# 守护进程转发到电脑,然后可以通过本地7912端口查看
os.system("adb forward tcp:7912 tcp:7912")
# 获取包名adb shell logcat | findstr cmp=
os.system("adb connect 127.0.0.1:62001")
# sleep(1)
# 可以是wifi或者usb
# d = u2.connect("a3fdcb92")
d = u2.connect("127.0.0.1:62001")
# d.debug = True
# d = u2.connect("192.168.1.102")
# d.info
# d.implicitly_wait(5)
sleep(2)
d.app_start("com.pikachuclientproject")
# d.app_start("com.tencent.mobileqq")
# print(d.app_info("com.tencent.mobileqq"))
# img = d.app_icon("com.tencent.mobileqq")
# img.save("qq_icon.png")
# d(text="登录").click()
# 手势登录
sleep(2)
d.watcher("update").when(text="全新版本").click(text="忽略")
d.watchers.run()
sleep(2)
d.swipe_points([(170, 560), (170, 745),
               (175, 930), (358, 926), (549, 931)], 0.2)
sleep(2)
if d(text="主页").exists:
    print("pass")
else:
    print("fail")
# d.swipe_points([(218, 576), (218, 725), (218, 868),
#                 (362, 868), (505, 868)], 0.2)
'''
d(description="请输入QQ号码或手机或邮箱").clear_text()
sleep(2)
d(description="请输入QQ号码或手机或邮箱").set_text("1490555904")
sleep(2)
d(resourceId="com.tencent.mobileqq:id/password").clear_text()
sleep(2)
d(resourceId="com.tencent.mobileqq:id/password").set_text("ZHang13424117248")
sleep(2)
d(description="登 录").click()
sleep(3)
if d(text="消息").exists:
    print("pass")
else:
    print("fail")

print(d.current_app())
'''
# d.healthcheck()  # 检查并维持设备端守护进程处于运行状态
# 推送文件到手机储存
# d.push("text.txt", "/sdcard/")
# 从手机储存拉文件到当前路径
# d.pull("/sdcard/setting.cfg", "setting.cfg")
sleep(2)
# d.app_stop("com.tencent.mobileqq")
d.app_stop("com.pikachuclientproject")