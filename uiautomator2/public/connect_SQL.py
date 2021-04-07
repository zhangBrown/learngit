# *-* coding:utf-8 *-*
import pymysql


class ConSql:
    def __init__(self):
        self.con = pymysql.connect(
            host="42.186.57.244",
            user="gas",
            password="gas_fee",
            database="PIKACHU",
            charset="utf8")

    def run_sql(self, sql=None):

        # 执行sql语句的光标对象
        cursor = self.con.cursor()
        # 执行sql
        cursor.execute(sql)
        # 获取单条数据
        data = cursor.fetchone()
        # 关闭光标对象
        cursor.close()
        # 关闭数据库
        self.con.close()

        return data

if __name__ == "__main__":
    run = ConSql()
    res = run.run_sql("select captcha from PhoneCaptcha order by pcid desc limit 1;")
    print(res[0])



