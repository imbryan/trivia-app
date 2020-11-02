import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random, json
from model import Question


class View(tk.Tk):

    # Some default sizes for consistency
    PAD = 10
    BUTTON_WIDTH = 15

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.score = 0
        self.current_question = 0

        # variable for question
        self.question_var = tk.StringVar()

        # variables for options
        self.A_var = tk.StringVar()
        self.B_var = tk.StringVar()
        self.C_var = tk.StringVar()
        self.D_var = tk.StringVar()

        self.title("Trivia Training")

        self._make_main_frame()
        self._make_buttons()

    def main(self):
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        right = int(self.winfo_screenwidth()/2 - width/2)
        down = int(self.winfo_screenwidth()/2 - height/2)

        self.geometry(f'+{right}+{down}')

        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_buttons(self):
        frame = ttk.Frame(self.main_frame)

        question_frame = ttk.Frame(frame)
        answer_frame = ttk.Frame(frame)

        # Question frame widgets
        question_label = ttk.Label(question_frame, textvariable=self.question_var, justify="center")
        question_label.pack(side="left", expand=True,)

        # Answer frame widgets
        option_a = ttk.Button(answer_frame, textvariable=self.A_var,
                              command=lambda: self.controller.on_button_click("A"))
        option_a.pack(side="left", expand=True)

        option_b = ttk.Button(answer_frame, textvariable=self.B_var,
                              command=lambda: self.controller.on_button_click("B"))
        option_b.pack(side="left", expand=True)

        option_c = ttk.Button(answer_frame, textvariable=self.C_var,
                              command=lambda: self.controller.on_button_click("C"))
        option_c.pack(side="left", expand=True)

        option_d = ttk.Button(answer_frame, textvariable=self.D_var,
                              command=lambda: self.controller.on_button_click("D"))
        option_d.pack(side="left", expand=True)

        # Packing frames
        question_frame.pack(side="top")
        answer_frame.pack(side="top")
        frame.pack(side="top")

    @staticmethod
    def popup_window(title, message):
        showinfo(title, message)
