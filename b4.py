# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:21:00 2024

@author: YenTrinh
"""
print("Bài 4")
N=int(input("Nhập N: "))
if N>=10 and N<=99:
    t=(N%10)+(N//10)
    print("Tổng các chữ số của N là: ",t)
