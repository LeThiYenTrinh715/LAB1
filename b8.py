# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:44:19 2024

@author: YenTrinh
"""
print("Bài 8")
a=float(input("Nhập chiều cao của bạn (m): "))
if a>0: 
    b=float(input("Nhập cân nặng của bạn (kg): "))
    if b>0: 
        c=b/(a**2)
        print("Chỉ số BMI của bạn là: ",c)

