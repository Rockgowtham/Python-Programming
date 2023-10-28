# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:09:09 2023

@author: folkm
"""

import turtle
import colorsys
turtle.bgcolor("white")
t=turtle.Turtle()
t.speed(0)
n=70
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h, 1,0.8)
    h+=1/n
    t.color(c)
    t.left(1)
    t.fd(0)
    for j in range(2):
        t.left(2)
        t.circle(100)
turtle.done()