import tkinter
import os

class InfoWindows(tkinter.Frame):
	def __init__(self,win):
		frame = tkinter.Frame(win)
		frame.grid(row=0,column=1)
		self.v = tkinter.Variable()
		entry = tkinter.Entry(frame,textvariable=self.v)
		entry.pack()
		self.text = tkinter.Text(frame)
		self.text.pack()



