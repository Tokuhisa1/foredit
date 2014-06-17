# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:54:57 2014

@author: wyh
"""

import wx
app=wx.App()
win=wx.Frame(None,title="for one")
btn=wx.Button(win,label="first start")
win.Show()
app.MainLoop()