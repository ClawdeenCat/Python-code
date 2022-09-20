# from re import A, I


# press=float(input("二进制："))
# a=10
# i=0
# none=True
# while none:
#     i=i+1
#     a=a*10
#     if a>press:
#         none=False
#         print(i)





# 计算位数方法1：比大小

# def num(press):
#     a=10
#     i=0
#     none=True
#     while none:
#         i=i+1
#         a=a*10
#         if a>press:
#             none=False
#             print(i)

# a=float(input())
# num(a)




# 计算位数方法2：字节长度

# from operator import length_hint
# a=input()
# b=length_hint(a)
# print(b-1) 
from tkinter import N
def num2(press):
    from operator import length_hint
    n=length_hint(press)
    n=n-1
    return n




# 乘方的计算
def cfang(a,b):
    c=a
    if b==0:
        c=1
        return c
    else:
        for i in range(1,int(b)):
            c=c*a
        return c  

# press=float(input("pe："))
# f=input()
# d=cfang(press,f)
# print(d)



press=input("输入二进制：")
n=num2(press)
b=0
b1=0
num=0
none=True
while none:
    # print(n)
    c=cfang(10,n)
    

    for s in range(0,2):
        b1=s*c
   
        if b1<(float(press)-c):
            b=s
        print(float(press)-c)



    num=b*c+num
    n=n-1


    if n<0:#判定循环结束
        none=False
