import tkinter as tk
import math
import random

class JarvisUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LEO JARVIS MODE")
        self.root.geometry("600x600")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(self.root, width=600, height=500, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.label = tk.Label(self.root, text="", fg="white", bg="black", font=("Arial", 12))
        self.label.pack()

        self.angle = 0
        self.wave = [0] * 20
        self.running = True

        self.animate()

    def update_wave(self, intensity):
        self.wave.pop(0)
        self.wave.append(intensity / 50)

    def set_text(self, text):
        self.label.config(text=text)

    def animate(self):
        self.canvas.delete("all")

        cx, cy = 300, 250

        # glowing orb (Jarvis core)
        r = 60 + math.sin(self.angle) * 10

        self.canvas.create_oval(
            cx - r, cy - r,
            cx + r, cy + r,
            outline="#00f0ff",
            width=3
        )

        # waveform bars
        x = 100
        for i, w in enumerate(self.wave):
            height = max(10, w * 100)
            self.canvas.create_rectangle(
                x, 450,
                x + 10, 450 - height,
                fill="#00f0ff"
            )
            x += 20

        self.angle += 0.1
        self.root.after(50, self.animate)

    def run(self):
        self.root.mainloop()