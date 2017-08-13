# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 23:03:23 2017

@author: shimizu
"""

import Tkinter

counter = 0
font = ("Helevetica", 32, "bold")
button = Tkinter.Button(font=font, text=str(counter))

def clicked():
    global counter, button
    counter = counter + 1
    button.config(text=str(counter))
    
button.config(command=clicked)
button.pack()
button.mainloop()
