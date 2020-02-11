from tkinter import *
from functools import partial
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
                                          font=("Terminal", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Terminal", "12"),
                                  padx=10, pady=-10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You Asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here",font=("Terminal", "8"))



class Help:
    def __init__(self, partner):

        background = "#aaaaaa"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up Child Window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font=("Terminal", "15", "bold"), bg=background)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)
        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="red", font=("Terminal", "12"),
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temp Converter")
    something = TempCon(root)
    root.mainloop()


