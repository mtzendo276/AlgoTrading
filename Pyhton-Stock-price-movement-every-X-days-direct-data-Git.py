# script to retrieve stock ticker historic price data (closing) from Yahoo finance for the trailing 12 month or more.
# and calculate the stock price moves and price percentage moves in X days, for the trailing 12 month or more.
# and determine largest moves and print on the screen.
# and generate CSV report for all the price movements.


#import libraries
from datetime import datetime
import csv
import numpy as np
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override() #<== to override pandas

#################### Enter Below the required data ################################
BUSINESS_DAYS = 20   # Enter here number of business days, every 5 days is equal to 1 week (20 business days = 4 weeks).
STOCK_PRICE_COLUMN = 5  # Enter here the CSV file column number that contains the stock prices.
DATE_COLUMN = 1         # Enter here the CSV file column number that contains the dates.
STOCK = 'GOOG'

OUTPUT_REPORT_NAME = STOCK + '_report.csv'
#####################Don't change anything below this line###############################
price_close_lst=[]
date_lst=[]
price_moves_lst=[]
percent_moves_lst=[]
moveDate_lst=[]
####################

data = web.get_data_yahoo(STOCK, start="2022-01-01")
print(data)

data_date = data.index.values  # convert the panda dataframe index (dates in this case) into array

data2 = data.to_numpy() # convert the panda dataframe floats into array

##########################
#load from the data data_frame to individual lists: price_close_lst and date_lst
for i in range(len(data_date)):
    #if data_date[i]!='Date':
    data_date_clean = str(data_date[i])
    data_date_clean = data_date_clean.replace('T00:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T01:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T02:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T03:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T04:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T05:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T06:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T07:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T08:00:00.000000000', '')
    data_date_clean = data_date_clean.replace('T09:00:00.000000000', '')
    #print(data_date_clean)
    date_lst.append(data_date_clean)  #convert numpy object to string so you can use replace()
    
    
print(date_lst[0])

for i in range(len(data2)):
    #if data2[i]!='Close':
    price_close_lst.append(round(data2[i][3],2))


## Start to calculate and compare the price moves
startPrice=0
priceRange=0
for i in range(len(price_close_lst)):
    startPrice=""
    endPrice=""
    if i%BUSINESS_DAYS == 0:
        startPrice = price_close_lst[i]
        endDate = date_lst[i]
        print(endDate," Start Price= ",startPrice)
        if i+BUSINESS_DAYS < len(price_close_lst):
            endPrice = price_close_lst[i+BUSINESS_DAYS]
            endDate = date_lst[i+BUSINESS_DAYS]
            moveDate_lst.append(date_lst[i+BUSINESS_DAYS])
        else:
            endPrice = price_close_lst[-1]
            endDate = date_lst[-1]
            moveDate_lst.append(date_lst[-1])
            
        print(endDate," End Price= ",endPrice)
        priceRange = endPrice - startPrice
        price_moves_lst.append(round(priceRange,2))
        if priceRange > 0:
            percentMove = (priceRange/startPrice)*100
            percent_moves_lst.append(round(percentMove,2))
            
        if priceRange < 0:
            percentMove = (priceRange/endPrice)*100
            percent_moves_lst.append(round(percentMove,2))
            
percentMoveDate=""
priceMoveDate=""
print(price_moves_lst,"\n")
print(percent_moves_lst,"\n")
print(moveDate_lst,"\n")

for x in range(len(percent_moves_lst)):
    if percent_moves_lst[x] == max(percent_moves_lst):
        percentMoveDate = moveDate_lst[x]

for y in range(len(price_moves_lst)):
    if price_moves_lst[y] == max(price_moves_lst):
        priceMoveDate = moveDate_lst[y]
        
print(priceMoveDate," Maximum Price Move= ", "$"+str(max(price_moves_lst)),"\n")
print(percentMoveDate," Maximum Price Percent Move= ", str(max(percent_moves_lst))+"%","\n")

print(priceMoveDate," Minimum Price Move= ", "$"+str(min(price_moves_lst)),"\n")
print(percentMoveDate," Minimum Price Percent Move= ", str(min(percent_moves_lst))+"%","\n")

### Output generated results into a CSV file
file_out = open(OUTPUT_REPORT_NAME, "w")
file_out.write("date")
file_out.write(",")
file_out.write("Price_Move")
file_out.write(",")
file_out.write("%Price_Move")
file_out.write("\n")
for i in range(len(moveDate_lst)):
    file_out.write(moveDate_lst[i])
    file_out.write(",")
    file_out.write(str(price_moves_lst[i]))
    file_out.write(",")
    file_out.write(str(percent_moves_lst[i])+"%")
    file_out.write("\n")
    
file_out.close()

print("Finished! Generated report is located in the same folder as the script: ",OUTPUT_REPORT_NAME )
