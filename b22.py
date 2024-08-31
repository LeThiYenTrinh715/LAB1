# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:04:09 2024

@author: YenTrinh
"""
print("Bài 22")
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
if a==0 and b!=0:
    print("Phương trình vô nghiệm")
if a==0 and b==0:
    print("Phương trình có vô số nghiệm")
if a!=0:
    x=-b/a
    print("Phương trình có nghiệm duy nhất là ",x)