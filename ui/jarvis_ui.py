import tkinter as tk

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LEO OS")
        self.root.geometry("600x400")
        self.root.configure(bg="black")

        self.label = tk.Label(self.root, text="LEO ACTIVE", fg="cyan", bg="black", font=("Arial", 16))
        self.label.pack(pady=20)

        self.text = tk.Label(self.root, text="", fg="white", bg="black", font=("Arial", 12))
        self.text.pack()

    def update(self, msg):
        self.text.config(text=msg)

    def run(self):
        self.root.mainloop()