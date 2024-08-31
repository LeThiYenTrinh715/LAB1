# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:42:52 2024

@author: YenTrinh
"""
print("Bài 26b")
N=int(input("Nhập số nguyên N: "))
if N>=0 and N<=9:
    print(N)
else:
    a=N%10
    b=N//10
    c=b%10
    d=b//10
    e=d%10
    f=d//10
    i=[a,c,e,f]
    k=sorted(i)
    print(k)
    
        

    
