import datetime
from network.tusharedata import Network

net = Network()

def cal_delt_time(timestr, delt=250):
    date = datetime.datetime.strptime(timestr, '%Y%m%d')
    dd = date - datetime.timedelta(days=delt)
    return datetime.datetime.strftime(dd, "%Y%m%d")



if __name__ == "__main__":
    dd = cal_delt_time("20220312", delt=50)
    print(dd)
