# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:04:28 2024

@author: YenTrinh
"""
print("Bài 10")
a=int(input("Nhập biển số xe đầu của bạn: "))
if a>=1 and a<=9: 
    b=int(input("Nhập biển số xe thứ hai của bạn: "))
    if b>=1 and b<=9: 
        c=int(input("Nhập biển số xe thứ ba của bạn: "))
        if c>=1 and c<=9: 
            d=int(input("Nhập biển số xe cuối của bạn: "))
            if d>=1 and d<=9: 
                t=a+b+c+d
                if t%10==0:
                    print("Số nút là 0")
                else:
                    print("Số nút là ",t%10)
            else:
                print("Nhập số có một chữ số!")
        else:
            print("Nhập số có một chữ số!")
    else:
        print("Nhập số có một chữ số!")
else:
    print("Nhập số có một chữ số!")
                

    