# import turtle
# import turtle as t
from turtle import forward, right # ideal
import math, random as r
from turtle import *

# forward(100)
# def forward(x):   
#      print("merhaba",x)

forward(100)
# right(90)
renkler=["red","green","blue"]
print(r.random())
print(r.randint(50,100))
print(r.choice(renkler))
# print(kenaru)
# color("red")
speed(10)
for ddd in range(10):
    kenaru = r.randint(50,200)
    color(r.choice(renkler))
    aa=r.randint(-300,300)
    ss=r.randint(-300,300)
    penup()
    goto(aa,ss)
    pendown()
    ks= r.randint(3,5)
    for a in range(ks):
        forward(kenaru); right(360/ks)
input()





#
