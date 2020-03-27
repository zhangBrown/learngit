from api_auto.public.operation_Excel import OperExcel
import json
from urllib import parse


class TransferDict:
    """将抓包到的data和headers转换成需要的字典形式"""

    def __init__(self):
        self.transfer = OperExcel()

    def data_dict(self, row, col):
        wbs = OperExcel(sheetname="Sheet2").read()
        row_count = row
        for i in wbs:
            for j in i:
                if j == "data":
                    param = i[j]
                elif j == "headers":
                    header = i[j]

            param = parse.unquote(param)  # urldecode解码
            li = param.split("?", 1)
            if len(li) == 2:
                print(li[0])
                params = li[1]
            else:
                params = li[0]

            c = {}

            list_a = params.split("&")
            for i in list_a:
                b = {}
                a = i.split("=")
                b[a[0]] = a[1]
                for j in b:
                    c[j] = b[j]

            self.__write_exl(row_count, col, json.dumps(c))
            self.__header_dict(header, row_count, col-1)
            row_count += 1

    def __header_dict(self, header, row, col):
        d = {}
        list_b = header.split(": ")
        d[list_b[0]] = list_b[1]

        self.__write_exl(row, col, json.dumps(d))

    def __write_exl(self, row, col, value):
        self.transfer.write(row, col, value)


if __name__ == '__main__':
    trf_data = TransferDict()
    trf_data.data_dict(9, 6)
    #
    # trf_headers = TransferDict()
    # trf_headers.header_dict(headers, 2, 5)