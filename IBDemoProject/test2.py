from ibapi.client import EClient
from ibapi.common import TickerId
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    # def error(self, reqId, errorCode, errorString):
    #     print(errorString)
        # print("Error {} {} {}".format(reqId, errorCode, errorString))
    def error(
        self,
        reqId: TickerId,
        errorCode: int,
        errorString: str,
        advancedOrderRejectJson="",
    ):
        print("Error {} {} {}".format(reqId, errorCode, errorString))

    def contractDetails(self, reqId, contractDetails):
        print("reqID: {}, contract:{}".format(reqId, contractDetails))

app = TradingApp()
#7497 for paper account
app.connect("127.0.0.1", 7497, clientId=1)


# contract = Contract()
# contract.symbol = "AAPL"
# contract.secType = "STK"
# contract.currency = "USD"
# contract.exchange = "SMART"
# app.reqContractDetails(1005, contract)
app.run()