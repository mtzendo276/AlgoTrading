
from ibapi.client import EClient
from ibapi.common import BarData
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import pandas as pd

from datetime import datetime
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson=""):
        print("Error {} {} {}".format(reqId, errorCode, errorString))

    def contractDetails(self, reqId, contractDetails):
        print("reqID: {}, contract:{}".format(reqId, contractDetails))

    def historicalData(self, reqId: int, bar: BarData):
        print("HostroicalData. RegId:", reqId, "BarData.", bar)

def websocket_con():
    app.reqHistoricalData(reqId=1,
                          contract=contract,
                          endDateTime='',
                          durationStr='3 M',
                          barSizeSetting='5 mins',
                          whatToShow='ADJUSTED_LAST',
                          useRTH=1,
                          formatDate=1,
                          keepUpToDate=0,
                          chartOptions=[])
    app.run()



app = TradingApp()
# 7497 paper account port
# 7496 real user
app.connect("127.0.0.1", 7497, clientId=1)
time.sleep(1)

contract = Contract()
contract.symbol = "FB"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"
# app.reqContractDetails(100, contract)

con_thread = threading.Thread(target=websocket_con(), daemon=True)
con_thread.start()




# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
