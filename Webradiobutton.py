import tkinter as tk

def show_selection():
    selected_option = var.get()
    if selected_option == 1:
        print("Option 1 is selected")
    elif selected_option == 2:
        print("Option 2 is selected")
    elif selected_option == 3:
        print("Option 3 is selected")

# Create main window
window = tk.Tk()
window.title("Radio Button Example")

# Create tkinter variable to store selected option
var = tk.IntVar()

# Create radio buttons
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=var, value=1)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="Option 2", variable=var, value=2)
radio_button2.pack()

radio_button3 = tk.Radiobutton(window, text="Option 3", variable=var, value=3)
radio_button3.pack()

# Create a button to show selected option
button = tk.Button(window, text="Show Selection", command=show_selection)
button.pack()

# Start the main event loop
window.mainloop()
