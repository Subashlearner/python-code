import tkinter as tk

def get_text_content():
    content = text_box.get("1.0", tk.END)  # Retrieve all text from line 1, character 0 to end
    print("Text content:")
    print(content)


window = tk.Tk()
window.title("Text Box Example")


text_box = tk.Text(window, height=10, width=50)
text_box.pack()


button = tk.Button(window, text="Get Text", command=get_text_content)
button.pack()

window.mainloop()
