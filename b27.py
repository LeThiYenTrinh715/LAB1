# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:37:50 2024

@author: YenTrinh
"""
print("Bài 27")
a=str(input("Nhập hình: "))
if a=="n":
    print("Tính Chu vi và Diện tích hình chữ nhật.")
    d=int(input("Nhập chiều dài: "))
    r=int(input("Nhập chiều rộng: "))
    P=(d+r)*2
    S=d*r
    print("Hình chữ nhật có chu vi là: ",P,". Diện tích là: ",S)
if a=="v":
    print("Tính Chu vi và Diện tích hình vuông.")
    d=int(input("Nhập chiều dài: "))
    P=d*4
    S=d**2
    print("Hình vuông có chu vi là: ",P,". Diện tích là: ",S)
if a=="t":
    print("Tính Chu vi và Diện tích hình tròn")
    r=int(input("Nhập bán kính: "))
    P=r*2*3.14
    S=(r**2)*3.14
    print("Hình tròn có chu vi là: ",P,". Diện tích là: ",S)

    
    