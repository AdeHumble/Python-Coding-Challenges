from tkinter import *


def color_1():
    label_1['bg']='red'    
def color_2():
    label_1['bg']='green'         
def color_3():
    label_1['bg']='blue'


window=Tk()
window.configure(bg='yellow')
window.title('DEMO 3')
window.resizable(width=False, height=False)

label_1=Label(bg='white',
            relief='solid',
            bd=1,
            width=20,
            height=3)

button_1=Button(text='RED',
                font='times 12 bold',
                relief='groove',
                bd=5,
                bg='black',
                fg='white',
                command=color_1)

button_2=Button(text='GREEN',
                font='times 12 bold',
                relief='groove',
                bd=5,
                bg='black',
                fg='white',
                command=color_2)      

button_3=Button(text='BLUE',
                font='times 12 bold',
                relief='groove',
                bd=5,
                bg='black',
                fg='white',
                command=color_3)

label_1.grid(row=0,column=1)
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

window.mainloop()
