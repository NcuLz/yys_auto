import tkinter as tk
from tkinter import messagebox
#import  opencv_compare
import yuhun
import jiacheng
import sys
import yuling
sys.setrecursionlimit(9000000)

window = tk.Tk()
window.title('阴阳师护肝小助手')
window.geometry('600x300')
#图片背景
#bg_pic = PhotoImage(file=)


l = tk.Label(window, text="阴阳师自强护肝计划!",bg='green', font=('Arial, 12'), width=100, height=2)
l.pack()

tk.Label(window, text="选择开启加成：", font=('Arial, 10')).place(x=10, y=40,anchor='nw')

#加成选择按钮
var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='御魂加成',variable=var1, onvalue=1, offvalue=0, command=jiacheng.yuhunjiacheng).place(x=10, y=60,anchor='nw')    # 传值原理类似于radiobutton部件
c2 = tk.Checkbutton(window, text='觉醒加成',variable=var2, onvalue=1, offvalue=0, command=jiacheng.juexingjiacheng).place(x=100, y=60,anchor='nw')

#entry窗口部件获取刷御魂次数，时间，魂十或者魂十一等
tk.Label(window, text="填入刷御魂的次数：", font=('Arial, 10')).place(x=150, y=100,anchor='nw')
tk.Label(window, text="说明：填写次数或时间后点击左侧“御魂”按钮即可自动刷魂！", font=('Arial, 10')).place(x=150, y=130,anchor='nw')
l1=tk.Label(window,text='（只能是数字）',font=('Arial, 10')).place(x=460, y=100, anchor='nw')

var = tk.StringVar()
entry_num = tk.Entry(window,textvariable=var)
entry_num.place(x=270, y=100, anchor='nw')
tk.Button(window, text='御魂', width=15, height=2,bg='yellow',command=lambda :yuhun.yuhun(int(var.get()))).place(x=10, y=100, anchor='nw')

#御灵窗口部件
tk.Label(window, text="填入刷御灵的次数：", font=('Arial, 10')).place(x=150, y=180,anchor='nw')
tk.Label(window, text="说明：填写次数或时间后点击左侧“御灵”按钮即可自动刷魂！", font=('Arial, 10')).place(x=150, y=210,anchor='nw')
l1=tk.Label(window,text='（只能是数字）',font=('Arial, 10')).place(x=460, y=180, anchor='nw')

yuling_var = tk.StringVar()
yuling_num = tk.Entry(window,textvariable=yuling_var)
yuling_num.place(x=270, y=180, anchor='nw')
tk.Button(window, text='御灵', width=15, height=2,bg='yellow',command=lambda :yuling.yuhun(int(yuling_var.get()))).place(x=10, y=180, anchor='nw')


window.mainloop()