# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import tkFileDialog
import os
import fnmatch
def search():
    text = entry_1.get()
    if not text:
        tkMessageBox.showinfo('出错了','请先输入关键字再搜索')#更简洁判断是不是空的
        return
    fn = tkFileDialog.askdirectory()#选择文件夹
    fnlist = os.walk(fn)#列出目录 尖括号列出来的是对象
    listbox.delete(0, END)
    for root,dirs,files in fnlist:
        for i in fnmatch.filter(files,entry_2.get()):
            filename = '%s/%s' %(root , i)
            listbox.insert(END,filename)
            print filename
def click(enve):
    index = listbox.curselection()[0]
    path = listbox.get(index)
    if not path:
        return
    window = Tk()
    window.title('查看文件')
    text = Text(window)#window的多行文本框
    text.grid()
    fn_text = open(path).read()
    text.insert(END,fn_text)


root = Tk()
root.title('文件查找程序')
root.geometry('+600+300')
Label(root,text='关键字:').grid()
entry_1 = Entry(root)
entry_1.grid(row=0,column=1)
Label(root,text='文件类型:').grid(row=0,column=2)
entry_2 = Entry(root)
entry_2.grid(row=0, column=3)
button = Button(root,text='搜索',command=search)
button.grid(row=0,column=4)
var1 = StringVar()
listbox = Listbox(root,width=80, listvariable=var1)
listbox.bind('<Double-Button-1>',click)
listbox.grid(row=1,column=0,columnspan=5)#columnspan用于整合列表框
root.mainloop()