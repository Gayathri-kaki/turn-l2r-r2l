# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:29:34 2020

@author: kakig
"""

from PIL import Image
img=Image.open("amma.png")
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save("mom.png")
print("completed")

