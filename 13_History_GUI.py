from tkinter import *
from functools import partial
import random


class TempCon:
    def __init__(self, parent):

        # Formatting variables
        background_color = "#a8b8d0"

        self.all_calc_list = ['1 degrees F is -17.2 degrees C',
                              '12 degrees F is -11.1 degrees C',
                              '123456 degrees F is 68568.9 degrees C',
                              '1234567 degrees F is 685852.8 degrees C']

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

        # History Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Terminal", "12"),
                                     padx=10, pady=-10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):

        background = "#aaaaaa"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up Child Window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up History heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font=("Terminal", "15", "bold"), bg=background)
        self.how_heading.grid(row=0)
        # History text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are you most recent "
                                                           "calculations. Please use the "
                                                           "export button to create a text "
                                                           "file of all your calculations for "
                                                           "this session", wrap=250,
                               justify=LEFT, width=40, bg=background)
        self.history_text.grid(row=1)

        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                                - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                                calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")


        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background,font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)


        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0,column=0)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)


    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temp Converter")
    something = TempCon(root)
    root.mainloop()


