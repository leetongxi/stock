from network.tusharedata import Network
import pandas as pd
from network.basicdata import rpsdx

if __name__ == "__main__":
    rps = rpsdx()
    print(rps.cal_rps())