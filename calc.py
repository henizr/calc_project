import tkinter as tk

result = ""
window = tk.Tk()

def plus():
    global result
    if True:
        sign = "+"
    entry.insert(
        1, {sign}
    )
    result = entry.get() + "+"

def equal():
    global result
    result += entry.get()
    print(eval(result))
    result = ""

entry = tk.Entry(
    window,
)
entry.place(
    x = 0,
    y = 0
)

button = tk.Button(
    window, 
    text=":)", 
    width=15, 
    height=4,
    command=plus
)
button.place(
    x = 0,
    y = 25
)
button_equal = tk.Button(
    window, 
    text="=", 
    width=15, 
    height=4,
    command=equal
)
button_equal.place(
    x = 0,
    y = 100
)



window.mainloop()