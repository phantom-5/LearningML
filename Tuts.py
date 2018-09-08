import pandas as pd
import quandl

quandl.ApiConfig.api_key=''
dataf = quandl.get("WIKI/GOOGL")
dataf=dataf[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
dataf['HL_PCT'] = (dataf['Adj. High']-dataf['Adj. Close'])/dataf['Adj. Close']*100.0
dataf['PCT_change'] = (dataf['Adj. Close']-dataf['Adj. Open'])/dataf['Adj. Open']*100.0
dataf=dataf[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
print(dataf.head())


