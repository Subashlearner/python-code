import tkinter as tk

def show_selection():
    if var1.get() == 1:
        print("Option 1 is selected")
    else:
        print("Option 1 is not selected")

    if var2.get() == 1:
        print("Option 2 is selected")
    else:
        print("Option 2 is not selected")


window = tk.Tk()
window.title("Check Button Example")


var1 = tk.IntVar()
check_button1 = tk.Checkbutton(window, text="Option 1", variable=var1)
check_button1.pack()

var2 = tk.IntVar()
check_button2 = tk.Checkbutton(window, text="Option 2", variable=var2)
check_button2.pack()


button = tk.Button(window, text="Show Selection", command=show_selection)
button.pack()


window.mainloop()
