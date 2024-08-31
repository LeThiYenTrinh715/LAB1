# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:20:35 2024

@author: YenTrinh
"""
print("Bài 24")
h=int(input("Nhập giờ: "))
if h>=0 and h<=24: 
    m=int(input("Nhập phút: "))
    if m>=0 and m<=59: 
        s=int(input("Nhập giây: "))
        if s>=0 and s<=59:
            print("Hợp lệ")
        else:
            print("Sai giây!")
    else:
        print("Sai phút!")
else:
    print("Sai giờ!")
   
    