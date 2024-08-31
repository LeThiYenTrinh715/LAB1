# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:30:33 2024

@author: YenTrinh
"""
print("Bài 6")
a=int(input("Năm nay là năm mấy? "))
if a==2024: 
    b=int(input("Bạn sinh năm mấy? "))
    if b>=0 and b<=2024:
        t=a-b
        print("Vậy bạn ",t," tuổi")
    else:
        print("Sai năm sinh!")
else:
    print("Sai năm!")
        

