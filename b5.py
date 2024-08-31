# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:24:57 2024

@author: YenTrinh
"""
print("Bài 5")
h=float(input("Nhập giờ: "))
if h>=0 and h<=24: 
    m=float(input("Nhập phút: "))
    if m>=0 and m<=60: 
        s=float(input("Nhập giay: "))
        if s>=0 and s<=60: 
            a=h*60*60+m*60+s
            print("Số giây được đổi ra là: ",a," giây")
