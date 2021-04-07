# *-* coding:utf-8 *-*
import pymysql


class ConSql:
    def __init__(self):
        self.con = pymysql.connect(
            host="42.186.57.244",
            user="gas",
            password="gas_fee",
            database="GB_BMS",
            charset="utf8")

    def run_sql(self, values):

        # 执行sql语句的光标对象
        cursor = self.con.cursor()
        # i = 100
        # while i < 40000100:
        # try:
            # 执行sql
            # cursor.execute(sql, i)
        cursor.executemany("insert ignore into DataAnalysis(gameid,begin,end,app_channel) values(%s, %s, %s, %s)", values)
        self.con.commit()
        # except Exception as e:
            # print(e)
            # self.con.rollback()
        # 关闭光标对象
        cursor.close()
         # 关闭数据库
        # self.con.close()

if __name__ == "__main__":
    # run = ConSql()
    # run.run_sql('insert into Summary(gameid,identifer,platform,status) values("ma47","netease.614bfcly_cps_dev","android","计算完毕");')
    # run.run_sql('insert into DataAnalysis(gameid,begin,end,app_channel) values("g%s","2020-01-01","2020-01-01","netease");')
    run = ConSql()
    for k in range(4000):
        print(k)
        list1 = [("g" + str(i),"2020-01-01","2020-01-01","netease") for i in range(k * 10000,  k * 10000 + 10000)]
        run.run_sql(list1)
    run.con.close()
