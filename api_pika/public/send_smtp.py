import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(time, receiver, file_dir):
    smtpserver = "smtp.qq.com"
    port = 465
    sender = "412058966@qq.com"
    pwd = "gowjzdbfjomtbgcg"
    receiver = receiver

    # ------------编辑邮件内容--------
    file_path = file_dir
    with open(file_path, "rb") as fp:
        mail_body = fp.read()
    msg = MIMEMultipart()

    msg['subject'] = time + "皮卡接口自动化测试报告"  # 标题

    text = time + "皮卡接口自动化测试报告"     # 正文
    body = MIMEText(text, "html", "utf-8")
    msg.attach(body)

    att = MIMEText(mail_body, "base64", "utf-8")    # 附件
    att["Content-Type"] = "application/octet-stram"
    att["Content-Disposition"] = 'attachment;filename="test_report.html"'
    msg.attach(att)

    msg['from'] = sender
    msg['to'] = receiver

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.connect(smtpserver)
        smtp.login(sender, pwd)
    except Exception as msg:
        return "发送失败%s" % msg

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    return "发送成功%s" % msg['subject']