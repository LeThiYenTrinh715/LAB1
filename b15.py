# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:45:23 2024

@author: YenTrinh
"""
print("Bài 15")
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
A=(((a+b)/(a**(1/3)+b**(1/3)))-(a*b)**(1/3))/((a**(1/3)-b**(1/3))**2)
print("Kết quả phép tính A=(((a+b)/(a^(1/3)+b^(1/3)))-(a*b)^(1/3))/((a^(1/3)-b^(1/3))^2)",A)
