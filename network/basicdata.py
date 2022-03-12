from network.tusharedata import Network
net = Network()
import pandas as pd
import datetime

class rpsdx(object):
    def __init__(self):
        pass

    def cal_rps(self, d=120, s=None, end_time=datetime.datetime.now().strftime("%Y%m%d")):
        s_list = []
        if s:
            s_list.append(s)
        else:
            data1 = net.stock_basic()
            s_list = data1['ts_code'].tolist()

        # 计算250日前的日期
        # 遍历股票列表计算rps
