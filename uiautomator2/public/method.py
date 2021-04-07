import uiautomator2 as u2
from time import sleep


d = u2.connect("127.0.0.1:62001")


def res_ass(res):
    if res.exists:
        return True
    else:
        return False


def login():
    d.swipe_points([(170, 560), (170, 745),
                        (175, 930), (358, 926), (549, 931)], 0.2)
    sleep(2)
    count = res_ass(d(text="99+"))
    sleep(2)
    d.xpath("//android.widget.TextView[@text='工单处理 ']").click()
    sleep(2)
    d.xpath("//android.view.View/android.view.View[3]/android.widget.ImageView[1]").click()
    sleep(2)
    if count is False:
        d(text="仅看我处理的").sibling(className="android.view.View").click()