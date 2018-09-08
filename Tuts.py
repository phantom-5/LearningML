import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key=''
dataf = quandl.get("WIKI/GOOGL")
dataf=dataf[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
dataf['HL_PCT'] = (dataf['Adj. High']-dataf['Adj. Close'])/dataf['Adj. Close']*100.0
dataf['PCT_change'] = (dataf['Adj. Close']-dataf['Adj. Open'])/dataf['Adj. Open']*100.0
dataf=dataf[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col='Adj. Close'
dataf.fillna(-99999,inplace=True)

print(len(dataf))
forecast_out=int(math.ceil(0.001*len(dataf))) #use 10% of previous data to predict

dataf['label']=dataf[forecast_col].shift(-forecast_out)
dataf.dropna(inplace=True)
print(dataf.head())




