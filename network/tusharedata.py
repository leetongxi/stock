import datetime

import tushare as ts
import pandas as pd
import requests

# 环境初始化
ts.set_token('b278d91ba50a2184d52ce392e087b7e35e2572ecc38eed462fa88a09')
pro = ts.pro_api()


class Network(object):
    def __init__(self):
        pass

    def trade_cal(self):
        trade_data = pro.query('stock_basic', exchange='', list_status='L',
                         fields='ts_code,symbol,name,area,industry,list_date')
        return trade_data

    def pro_bar(self, ts_code, start_date, end_date):
        df = ts.pro_bar(ts_code=ts_code, adj='qfq', start_date=start_date, end_date=end_date)
        return df

    def stock_basic(self, exchange=''):
        stock_data = pro.query('stock_basic', exchange=exchange, list_status='L',
                         fields='ts_code,symbol,name,area,industry,list_date')
        return stock_data

    def trade_date_cal(self, start_date='20180101', end_date=datetime.datetime.now().strftime("%Y%m%d")):
        df = pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
        return df

class RPS(object):
    def __init__(self):
        self


if __name__ == "__main__":
    net = Network()
    data = net.stock_basic()
    print(data)
