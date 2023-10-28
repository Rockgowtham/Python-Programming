# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:24:24 2023

@author: folkm
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
f=r'\Users\folkm\.spyder-py3\senti08.xlsx'
xl=pd.ExcelFile(f)
dfs=xl.parse(xl.sheet_names[0])
dfs = dfs['TimeLine'].dropna().astype(str).tolist()
print(dfs)
sid=SentimentIntensityAnalyzer()
for data in dfs:
    print()
    ss=sid.polarity_scores(data)
    print(data)
    for k in ss:
        print(k,ss[k])