# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:56:40 2024

@author: YenTrinh
"""
print("Bài 18")
h=int(input("Nhập giờ thứ nhất: "))
m=int(input("Nhập phút thứ nhất: "))
s=int(input("Nhập giây thứ nhất: "))
h1=int(input("Nhập giờ thứ hai: "))
m1=int(input("Nhập phút thứ hai: "))
s1=int(input("Nhập giây thứ hai: "))
H=h+h1
M=m+m1
S=s+s1
H1=h-h1
M1=m-m1
S1=s-s1
print("Kết quả cộng là: ",H,"h",M,"p",S,"s")
print("Kết quả trừ là: ",H1,"h",M1,"p",S1,"s")
