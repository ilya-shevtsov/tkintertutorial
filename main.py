import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.menuBar = tk.Menu(self.root)
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Close", command=self.root.quit)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Close Without Question", command=self.root.quit)

        self.actionMenu = tk.Menu(self.menuBar, tearoff=0)
        self.actionMenu.add_command(label="Show Message", command=self.show_message)

        self.menuBar.add_cascade(label="Action", menu=self.actionMenu)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.root.config(menu=self.menuBar)

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearButton = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearButton.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def clear(self):
        self.textbox.delete('1.0',tk.END)

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


MyGUI()
