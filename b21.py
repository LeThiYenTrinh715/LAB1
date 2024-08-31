# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:14:58 2024

@author: YenTrinh
"""
print("Bài 21")
a=int(input("Nhập số có một chữ số: "))
b={1:"một", 2:"hai", 3:"ba", 4:"bốn", 5:"năm", 6:"sáu", 7:"bảy", 8:"tám", 9:"chín"}
if 0<= a <= 9: 
    print(b[a])
else:
    print("Không đọc được")