# -*- coding: utf-8 -*-
"""
IBAPI - EClient and EWrapper classes intro

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    # def error(self, reqId, errorCode, errorString):
    #     print("Error {} {} {}".format(reqId, errorCode, errorString))

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson=""):
        print("Error {} {} {}".format(reqId, errorCode, errorString))

    def contractDetails(self, reqId:int, contractDetails):
        print("reqId: {}, contract:{}".format(reqId, contractDetails))

app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)

contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(10004, contract)
app.run()