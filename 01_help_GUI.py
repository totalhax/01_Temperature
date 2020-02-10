from tkinter import *
import random


class TempCon:
    def __init__(self, parent):

        # Formatting variables
        background_color = "light blue"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=400, bg=background_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_coverter_label = Label(text="Temperature Converter",
                                         font=("Comic Sans MS", "16", "bold"),
                                         padx=10, pady=10)
        self.temp_coverter_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temp Converter")
    something = TempCon(root)
    root.mainloop()
