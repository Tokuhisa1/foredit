# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 13:24:55 2014

@author: wyh
"""

import wx
app=wx.App()
win=wx.Frame(None,title="for beauty",size=(300,300))
win.Show()
bt1=wx.Button(win,label='open',pos=(30,40))
bt2=wx.Button(win,label='save',pos=(30,100))
app.MainLoop()
