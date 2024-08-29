import tkinter as tk

def show_selection():
    selected_option = var.get()
    if selected_option == 1:
        print("Option 1 is selected")
    elif selected_option == 2:
        print("Option 2 is selected")
    elif selected_option == 3:
        print("Option 3 is selected")
window = tk.Tk()
window.title("Radio Button Example")


var = tk.IntVar()


radio_button1 = tk.Radiobutton(window, text="Option 1", variable=var, value=1)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="Option 2", variable=var, value=2)
radio_button2.pack()

radio_button3 = tk.Radiobutton(window, text="Option 3", variable=var, value=3)
radio_button3.pack()


button = tk.Button(window, text="Show Selection", command=show_selection)
button.pack()

p
window.mainloop()
