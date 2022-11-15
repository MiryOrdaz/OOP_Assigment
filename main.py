import sys

from TShapes import Shape3D
from TShapes import Octahedron
from TShapes import Hexagonal
from tkinter import *
from tkinter import font as tkFont
import tkinter as tk
from tkinter import ttk


# ---------------------------------------Start-up Option Legend---------------------------------------------------------
print('----------------------Option Menu--------------------' + '\n')
print('Legend of acessor/mutator methods in derived classes: \n\n 1.Get/set method for type and colour(RBG) \n 2.ASCII \
drawing method (.draw())\n 3.Get/set edge of Octahedron(set_edge or get_edge()) \n 4.Print coordinates(.get_coordinates())'
      '\n 5.Set specific coordinate points of Octahedron (e.g set_A2()) \n 6.Volume and SurfaceArea (volume() \
and surface_area())\n\n')

obj1 = Shape3D('sphere', (3, 4, 5))
obj1.set_type('butterfly')
obj1.set_colour((4, 5, 5))
print(obj1.get_type())

obj1 = Octahedron('diamond', 4, (2, 3, 4))
obj1.set_A2((1, 2, 3))  # Put a tuple insid
obj1.get_coordinates()


obj2 = Hexagonal('ddddd',4,5,(3,4,5))
obj2.get_coordinates()

#print(obj2.surface_area())
print(obj2.volume())
#obj2.draw()

#print(obj1.get_colour())


#print(obj1.surface_area())
#obj1.draw()



root = Tk()
root.title('3D Shapes')
root.configure(background='#6fabb7')
root.geometry('700x500')
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(5, weight=1)

helv = tkFont.Font(family='Garamond', weight='bold', size=20)
title = Label(root, text='3D Shapes OOP', font=helv, fg='#6fabb7')
title.grid(row=0, column=1,columnspan = 7)
title.grid(pady= 10)
title['compound'] = tk.CENTER




#Type of Shape
variable1 = StringVar()
frame1 = LabelFrame(root,text = 'Type of Shape', width = 200, height = 50, padx = 5, pady = 5)
occupy_space = Label(root, width = 20, height = 10, background = '#6fabb7').grid(row = 3, column =1)
frame1.grid(row = 4, column = 1)
combobox1 = ttk.Combobox(frame1, textvariable = variable1,
values = ['Hexagonal Pyramid', 'Octahedron'], state = 'readonly').grid()

#Edge Value
variable2 = StringVar()
frame2 = LabelFrame(root,text = 'Edge-value', width = 200, height = 50, padx = 5, pady = 5)
frame2.grid(row = 4, column = 2)
combobox2 = ttk.Combobox(frame2, textvariable = variable2,
values = ['----']).grid()

#A-Value
variable3 = StringVar()
frame3 = LabelFrame(root,text = 'A-Value', width = 200, height = 50, padx = 5, pady = 5)
frame3.grid(row = 4, column = 3)
combobox3 = ttk.Combobox(frame3, textvariable = variable3,
values = ['----']).grid()

#H-Value
variable4 = StringVar()
frame4 = LabelFrame(root,text = 'H-Value', width = 200, height = 50, padx = 5, pady = 5)
frame4.grid(row = 4, column = 4)
combobox4 = ttk.Combobox(frame4, textvariable = variable4,
values = ['----']).grid()

def main():
    try:
        if (variable1.get() == 'Octahedron'):
            obj1 = Octahedron(variable1.get(), float(variable2.get()))
            obj1.draw()
            answer.configure(text = f'Volume = {obj1.volume():,.2f}cm^3 \n Surface Area = {obj1.surface_area():,.2f}cm^2 \n\n')

        elif(variable1.get() == 'Hexagonal Pyramid'):
            obj2 = Hexagonal(variable1.get(), float(variable3.get()), float(variable4.get()))
            obj2.draw()
            answer.configure(text=f'Volume = {obj2.volume():,.2f}cm^3 \n Surface Area = {obj2.surface_area():,.2f}cm^2')

            button2 = Button(root, text='Show ASCII DRAWING', command=lambda: obj2.draw())
            button2.grid(row=7, column=1)

    except ValueError:
        print('Please enter correct numerical value')


#Button and Results Ouptut in Tkinter
btn_submit =  Button(root, text = 'Submit',command = main,
bg = '#F4FFDC').grid(row = 5, column  = 1 )

answer =Label(root, text="", pady=10, padx= 100, bg = '#F4FFDC')
answer.grid(row=5, column=2, columnspan = 3)


root.mainloop()

