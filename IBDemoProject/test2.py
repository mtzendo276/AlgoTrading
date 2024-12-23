from ibapi.client import EClient
from ibapi.common import TickerId
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        # print(errorString)
        print("Error {} {} {}".format(reqId, errorCode, errorString))
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

def websocket_con():
    app.run()
    event.wait()
    if event.is_set():
        app.close()

event = threading.Event()

app = TradingApp()
#7497 for paper account
app.connect("127.0.0.1", 7497, clientId=1)


# contract = Contract()
# contract.symbol = "AAPL"
# contract.secType = "STK"
# contract.currency = "USD"
# contract.exchange = "SMART"
# app.reqContractDetails(1005, contract)
# app.run()

# starting a separate daemon thread to execute the websocket connection
con_thread = threading.Thread(target=websocket_con)
con_thread.start()
time.sleep(1) # some latency added to ensure that the connection is established

#creating object of the Contract class - will be used as a parameter for other function calls
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(100, contract) # EClient function to request contract details
time.sleep(5) # some latency added to ensure that the contract details request has been processed
event.set()