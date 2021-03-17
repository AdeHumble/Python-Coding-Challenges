from tkinter import *

my_window=Tk()
my_window.configure(bg='blue')
my_window.title('DEMO')

width_of_window=400
height_of_window=100

screen_width=my_window.winfo_screenwidth()
screen_height=my_window.winfo_screenheight()

x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)

my_window.geometry('%dx%d+%d+%d'%(width_of_window, height_of_window, x_coordinate, y_coordinate))




def input_1():
    name=input('Please, enter your name: ')

    n=StringVar()
    label_1=Label(textvariable=n,
                  bg='white',
                  fg='red',
                  relief='solid',
                  anchor=SE)
    n.set('Your name is' + " " +name)
    #label_1.pack()
    label_1.grid(row=0, column=1)
                  
button_1=Button(text='Click to enter your name',
                bg='white',
                bd=10,
                fg='red',
                relief='raised',
                command=input_1,
                anchor=NW)


#button_1.pack()
button_1.grid(row=0, column=0)


