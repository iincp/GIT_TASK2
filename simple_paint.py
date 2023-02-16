from tkinter import *


class Paint:

    def __init__(self, window):
        self.window = window
        window.title("A Simple paint program")  # or self.window.title(), root.title()

        self.canvas = Canvas(window, width=1000, height=800)
        self.canvas.grid(row=1, column=1)

        self.label = Label(window, text="Drag the mouse to draw")
        self.label.grid(row=2, column=1)

        self.button = Button(window, width=10, text="Clear", command=self.clear)
        self.button.grid(row=3, column=1)

        self.canvas.bind("<B1-Motion>", self.mouse_event)