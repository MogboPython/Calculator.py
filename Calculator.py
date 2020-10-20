import tkinter as tk
from tkinter import *
from tkinter import font

def buttons(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def ClearBtn():  
    global operator
    operator = ''
    text_Input.set(operator)

def EqualsBtn():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''

HEIGHT = 450
WIDTH = 330
calc = tk.Tk()
calc.title('My Calculator Program')

operator = ''       #This is a global variable to store inputs in form of numbers and operators, +, -, /, * and so on, and perform the operations
text_Input = StringVar()   # This helps in displaying results on the entry box as buttons are pressed


calc.resizable(False,False)  #This is to make sure the gui frame isn't resizable, so as not to lose the shape of my program since I used place
canvas = tk.Canvas(calc,height=HEIGHT, width=WIDTH)
canvas.pack()
frame = tk.Frame(calc,bg = '#66e0ff')
frame.place(relheight=1, relwidth = 1)
disp = tk.Entry(calc, font = ('arial', 20, 'bold'), textvariable = text_Input, justify = 'right', bd =6)
disp.place(x = 10, y = 10, relheight=0.15, relwidth = 0.95)#, relx = 0.02)

#Buttons on the 1st row
# The buttons are named according to the output/operation they should carry out
btn1 = tk.Button(text = 1, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'), command = lambda: buttons(1), bd=6)
btn1.place(x = 10, y = 100) #relx = 0.02)
btn2 = tk.Button(text = 2, bg = '#cccccc', fg = '#000000', height = 4, width =8, font = ('arial', 9,'bold'),command = lambda: buttons(2), bd =6)
btn2.place(x = 90, y = 100)
btn3 = tk.Button(text = 3, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(3), bd =6)
btn3.place(x = 170, y = 100)
Multiplication = tk.Button(text = 'X', bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons('*'), bd =6)
Multiplication.place(x = 250, y = 100)

#===================================================================================================================
#Buttons on the Second row
btn4 = tk.Button(text = 4, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(4), bd=6)
btn4.place(x = 10, y = 185) #relx = 0.02)
btn5 = tk.Button(text = 5, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(5), bd =6)
btn5.place(x = 90, y = 185)
btn6 = tk.Button(text = 6, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(6), bd =6)
btn6.place(x = 170, y = 185)
Division = tk.Button(text = '/', bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons('/'), bd =6)
Division.place(x = 250, y = 185)

#==================================================================================================================
#Buttons on the third row
btn7 = tk.Button(text = 7, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(7), bd =6 )
btn7.place(x = 10, y = 270) #relx = 0.02)
btn8 = tk.Button(text = 8, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(8), bd =6)
btn8.place(x = 90, y = 270)
btn9 = tk.Button(text = 9, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(9), bd =6)
btn9.place(x = 170, y = 270)
Clear_Button = tk.Button(text = 'C', bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = ClearBtn, bd =6)
Clear_Button.place(x = 250, y = 270)

#====================================================================================================================
#Buttons on the fourth row
Subtraction = tk.Button(text = '-', bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons('-'),bd =6)
Subtraction.place(x = 10, y = 355) #relx = 0.02)
btn0 = tk.Button(text = 0, bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons(0), bd =6)
btn0.place(x = 90, y = 355)
Addition = tk.Button(text = '+', bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'),command = lambda: buttons('+'), bd =6)
Addition.place(x = 170, y = 355)
Equals_Button = tk.Button(text = '=', bg = '#cccccc', fg = '#000000', height = 4, width =8,font = ('arial', 9,'bold'), command = EqualsBtn, bd =6)
Equals_Button.place(x = 250, y = 355)




calc.mainloop()