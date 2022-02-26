import tushare as ts
import pandas as pd
import requests
# 环境初始化
ts.set_token('b278d91ba50a2184d52ce392e087b7e35e2572ecc38eed462fa88a09')
pro = ts.pro_api()

class Network():
    def trade_cal(self):
        data = pro.query('stock_basic', exchange='', list_status='L',
                         fields='ts_code,symbol,name,area,industry,list_date')
        return data

    def pro_bar(self, ts_code, start_date, end_date):
        df = ts.pro_bar(ts_code=ts_code, adj='qfq', start_date=start_date, end_date=end_date)
        return df

class RPS():
    def __init__(self):
        self



if __name__ == "__main__":
    net = Network()
    data = net.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011')
    print(data)
