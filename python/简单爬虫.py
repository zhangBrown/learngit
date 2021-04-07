import urllib.request
import re
import threading


def get_move():
    """电影天堂电影下载地址"""
    move_url = "https://www.ygdy8.net/html/gndy/dyzz/index.html"
    res_data = urllib.request.urlopen(move_url)
    res_text = res_data.read()
    res_html = res_text.decode("GBK")
    res_list = re.findall("<a href=\"(.*)\" class=\"ulink\">(.*)</a>", res_html)

    index = "https://www.ygdy8.net"
    move_dict = {}
    i = 1
    for move_url, move_name in res_list:
        new_url = index + move_url
        res_data = urllib.request.urlopen(new_url)
        res_text = res_data.read()
        res_html = res_text.decode("GBK")

        res = re.search("bgcolor=\"#fdfddf\"><a href=\"(.*?)\">", res_html)
        move_dict[move_name] = res.group(1)
        print("已经获取%s条信息" % i)
        i += 1
    return move_dict


def main():
    thread1 = threading.Thread(target=get_move)
    thread1.daemon = True
    thread1.start()
    thread1.join()


if __name__ == '__main__':
    main()




