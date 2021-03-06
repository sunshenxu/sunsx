import tkinter
from tkinter import ttk
import os
import json

class TreeWindows(tkinter.Frame):
	def __init__(self,win,iw):
		self.iw=iw
		frame = tkinter.Frame(win)
		frame.grid(row=0,column=0)
		self.tree = ttk.Treeview(frame)
		self.tree.pack(side=tkinter.LEFT,fill=tkinter.Y)
		path = 'D:\\Python\\xu\\day4'
		root = self.tree.insert('','end',text=os.path.basename(path),open=True,values=(json.dumps(path)))     #'end'表示往后添加
		self.loadTree(root,path)
		sr = tkinter.Scrollbar(frame)
		sr.pack(side=tkinter.RIGHT,fill=tkinter.Y)
		sr.config(command=self.tree.yview)
		self.tree.config(yscrollcommand=sr.set)

		self.tree.bind("<<TreeviewSelect>>",self.func)


	def func(self,event):
		self.sv = event.widget.selection() #返回被选中的下标 
		file = self.tree.item(self.sv)["text"]  #返回text的内容，这里不能用get只能用item
		self.iw.v.set(file)
		self.iw.text.delete(0.0,tkinter.END)
		filePath = self.tree.item(self.sv)["values"][0]
		if not os.path.isdir(filePath):	
			f = open(filePath,'r',encoding='utf-8')
			str = f.read()
			f.close()
			self.iw.text.insert(tkinter.INSERT,str)


	def loadTree(self,parent,path):
		for dirName in os.listdir(path):
			absPath = os.path.join(path,dirName)
			newRoot = self.tree.insert(parent,'end',text=dirName,values=(json.dumps(absPath)))
			if os.path.isdir(absPath):
				self.loadTree(newRoot,absPath)



		


