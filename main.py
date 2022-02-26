from network.tusharedata import Network
import pandas as pd

if __name__ == "__main__":
    net = Network()
    data = net.trade_cal()
    print(data)