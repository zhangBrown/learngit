import re


# res = re.match("\w{4,20}@(163|126|qq|sina)\.com$", "hello@qq.com")
# () \\1
# 起别名?P<xxx> 引用(?P=xxx)
res = re.match("<(?P<name1>[a-zA-Z0-9]+)>.*</(?P=name1)>", "<html>test</html>")

if res:
    print("匹配成功%s" % res.group())
    print(res.group(1))
else:
    print("匹配失败")