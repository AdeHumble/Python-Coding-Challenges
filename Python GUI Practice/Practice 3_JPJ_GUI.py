from tkinter import *

window=Tk()
window.resizable(width=False, height=False)
window.title('DEM0 4')



def full_name():
    fname=entry_1.get()
    lname=entry_2.get()
    flname=fname+" "+lname
    x.set(flname)


label_1=Label(text='First name')
label_2=Label(text='Last name')

x=StringVar()
label_3=Label(textvariable=x)


entry_1=Entry()
entry_2=Entry()

button_1=Button(text='SUBMIT',
              command=full_name)


label_1.grid(row=0, column=0)
label_2.grid(row=0, column=2)
label_3.grid(row=1, column=2)
entry_1.grid(row=0, column=1)
entry_2.grid(row=0, column=3)
button_1.grid(row=1, column=1)


window.mainloop()
