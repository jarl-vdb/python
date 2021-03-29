from pytrends.request import TrendReq
import pandas as pd
import time
from datetime import datetime
startTime = time.time()
print(datetime.now())

pytrend = TrendReq(hl='en-GB', tz=360, timeout=(10,25))

colnames = ["keywords"]
df = pd.read_csv("keyword_list.csv", names=colnames,encoding = "utf-8")  #,encoding = "utf-16"
df2 = df["keywords"].astype(str).values.tolist()
df2.remove("keywords")

dataset = []

for x in range(0,len(df2)):
     keywords = [df2[x]]
     print('Keyword ' + str(x) + ': ' + str(keywords))
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2003-01-01 2019-01-01')  #,     geo='GB'
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)

result = pd.concat(dataset, axis=1)
result.to_csv('search_trends.csv')

executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))