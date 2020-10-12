#!/usr/bin/env python
#########################################################################
# -*- coding: utf-8 -*-
# File Name: test.py
# Author :kite
# QQ : 987324339
# Email:987324339@qq.com
# Created Time: Mon 12 Oct 2020 08:52:29 PM CST
#########################################################################
import tkinter as tk


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('ArchLinux')


root = Root()
root.mainloop()

print("hello world")
