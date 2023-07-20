# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:22:56 2023

@author: user
"""

###함수 선언부
def add_func(n1,n2):
    return n1+n2

def sub_func(n1,n2):
    return n1-n2

def mul_func(n1,n2):
    return n1*n2

###전역 변수부
num1, num2, res = 100,200,0

###메인 코드부
res=add_func(num1, num2)
print(num1,'+',num2,'=',res)

###빼기 함수 추가
res=sub_func(num1, num2)
print(num1,'-',num2,'=',res)

###곱하기 함수 추가
res=mul_func(num1, num2)
print(num1,'*',num2,'=',res)
