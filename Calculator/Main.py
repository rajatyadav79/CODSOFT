from tkinter import *

def button_press(num):
    equation_text.set(equation_text.get() + str(num))

def equals():
    try:
        total = str(eval(equation_text.get()))
        equation_text.set(total)
    except ZeroDivisionError:
        equation_text.set("Error")
    except SyntaxError:
        equation_text.set("Syntax Error")

def clear():
    equation_text.set("")

def backspace():
    equation_text.set(equation_text.get()[:-1])

def key_press(event):
    if event.char.isdigit() or event.char in "+-*/.":
        button_press(event.char)
    elif event.keysym == "Return":
        equals()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

window = Tk()
window.title("Calculator")
window.geometry("600x700")

equation_text = StringVar()

label = Label(window, textvariable=equation_text, font=('consolas', 20), bg="black", fg="white", width=24, height=2)
label.pack(pady=20)

frame = Frame(window)
frame.pack()

buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', '.', '=', '/',
]

row_val = 0
col_val = 0

for button in buttons:
    if button == "=":
        btn = Button(frame, text=button, height=4, width=4, font=35, command=equals)
    else:
        btn = Button(frame, text=button, height=4, width=4, font=35, command=lambda x=button: button_press(x))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = Button(window, text='Clear', height=4, width=12, font=35, command=clear)
clear_button.pack(side=LEFT, padx=20)

backspace_button = Button(window, text='Backspace', height=4, width=12, font=35, command=backspace)
backspace_button.pack(side=RIGHT, padx=20)

window.bind("<Key>", key_press)

window.mainloop()
