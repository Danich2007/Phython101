Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk #theme of tk
>>> from tkinter import messagebox
>>> 
>>> Gui = Tk() # นี่คือหน้าจอหลักของโปรแกรม
>>> GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
NameError: name 'GUI' is not defined. Did you mean: 'Gui'?
>>> Gui.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
''
>>> Gui.geometry('500x400') #นี่คือขนาดโปรแกรม
''
>>> L1 = Label(Gui,text='โปรแกรมบันทึดความรู้',font=('Angsana New',30),fg='green')
>>> L1.place(x=30,y=20)
>>> ####################
>>> def Button2():
...     text = 'ตอนนี้มีเงินในบัญชีอยู่ 15,000 บาท'
...     massagebox.showinfo('เงินในบัญชี',text)
... 
...     
>>> FB1 = Frame(Gui) #คล้ายกระดาน
>>> FB1.place(x=100,y=80)
>>> B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
>>> B2.pack(ipadx=20,ipady=20)
>>> ####################
>>> def Button3():
...     text = 'Python 101, Math'
...     messagebox.showinfo('300,000',text)
... 
...     
>>> FB2 = Frame(Gui) #คล้ายกระดาน
>>> FB2.place(x=100,y=180)
>>> B3 =ttk.Button(FB1,text='เงินเข้า',command=Button3)
>>> B3.pack(ipadx=20,ipady=20)
>>>
>>> Gui.mainloop()






