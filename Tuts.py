import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key='qTgCxDQQ8_TKMnzYPEVi'
dataf = quandl.get("WIKI/GOOGL")
dataf=dataf[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
dataf['HL_PCT'] = (dataf['Adj. High']-dataf['Adj. Close'])/dataf['Adj. Close']*100.0
dataf['PCT_change'] = (dataf['Adj. Close']-dataf['Adj. Open'])/dataf['Adj. Open']*100.0
dataf=dataf[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col='Adj. Close'
dataf.fillna(-99999,inplace=True)

print(len(dataf))   #no. of rows
forecast_out=int(math.ceil(0.001*len(dataf)))
print(str(forecast_out)+" days")

dataf['label']=dataf[forecast_col].shift(-forecast_out)
dataf.dropna(inplace=True)
x_features=np.array(dataf.drop(['label'],1))
y_labels=np.array(dataf['label'])

x_features=preprocessing.scale(x_features)
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x_features,y_labels,test_size=0.2)

clf=svm.SVR(kernel='poly')
clf.fit(x_train,y_train)
accuracy=clf.score(x_test,y_test)
print(accuracy*100)


