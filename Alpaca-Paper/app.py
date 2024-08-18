
from alpaca.trading.client import TradingClient

TRADE_API_KEY=""
TRADE_API_SECRET=""

#### We use paper environment for this example ####
PAPER=True
TRADE_API_URL="https://paper-api.alpaca.markets"
TRADE_API_WSS=None
DATA_API_URL=None
OPTION_STREAM_DATA_WSS=None

api_key = TRADE_API_KEY
secret_key = TRADE_API_SECRET
paper = PAPER
trade_api_url = TRADE_API_URL

trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=paper, url_override=trade_api_url)
acc = trade_client.get_account()

print(acc)

# underlying_symbol = "SPY"
# req = GetOptionContractsRequest(
#     underlying_symbol=[underlying_symbol],                 
# # specify underlying symbol
#     status=AssetStatus.ACTIVE,                           
# # specify asset status: active (default)
#     expiration_date=None,                                
# # specify expiration date (specified date + 1 day range)
#     expiration_date_gte=None,                            
# # we can pass date object
#     expiration_date_lte=None,                           
#  # or string (YYYY-MM-DD)
#     root_symbol=None,                                    
# # specify root symbol
#     type=None,                                           
# # specify option type (ContractType.CALL or ContractType.PUT)	
# )
		
# res = trade_client.get_option_contracts(req)
# print(res)