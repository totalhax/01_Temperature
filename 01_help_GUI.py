from tkinter import *
import random


class TempCon:
    def __init__(self, parent):

        # Formatting variables
        background_color = "#a8b8d0"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=400, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Comic Sans MS", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Comic Sans MS", "12"),
                                  padx=10, pady=-10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You Asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):

        background = "#aaaaaa"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up GUI Frame

        # Set up Help heading (row 0)

        # Help text (label, row 1)

        # Dismiss button (row 2)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temp Converter")
    something = TempCon(root)
    root.mainloop()
