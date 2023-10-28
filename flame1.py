# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:51:35 2023

@author: folkm
"""

def predict(c):
    f="flames"
    len3=len(f)
    i=0
    index=0
    while(i<=4):
        c=c-index
        k=c%len3
        f=f.replace(f[k],'')
        len3=len(f)
        index=k-1
        i=i+1
    print(f)
predict(12)