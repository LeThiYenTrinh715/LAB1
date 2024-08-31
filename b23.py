# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:12:23 2024

@author: YenTrinh
"""
print("Bài 23")
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
delta=b**2-4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
else:
    x1=(-b+(delta**(1/2)))/2*a
    x2=(-b-(delta**(1/2)))/2*a
    print("Phương trình có nghiệm x1 = ",x1,",x2 = ",x2)
if delta==0:
    x=-b/2*a
    print("Phương trình có nghiệm kép x1 = x2 = ",x)