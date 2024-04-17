import tkinter as tk

root = tk.Tk()

root.geometry("500x500")  # window size
root.title("My First GUI")  # title setting

# create a label
label = tk.Label(master=root, text="Hello World!", font=('Arial', 18))

# set padding
label.pack(padx=20, pady=20)

# text box that you can write in
textBox = tk.Text(root, height=3, font=('Arial', 16))
textBox.pack()

root.mainloop()
