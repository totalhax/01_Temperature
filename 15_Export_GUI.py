from tkinter import *
from functools import partial
import random


class Converter:
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
        self.export_button = Button(self.converter_frame, text="Export",
                                    font=("Terminal", "12"),
                                    padx=10, pady=-10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)



class Export:
    def __init__(self, partner):

        background = "#aaaaaa"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up Child Window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300,  bg=background)
        self.export_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font=("Terminal", "15", "bold"), bg=background)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "and press the Save "
                                                         "button to save your "
                                                         "calculation history "
                                                         "to a text file.",

                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your calculation "
                                                         "history",
                                 justify=LEFT, bg=background, wrap=225,
                                   font="Arial 10 italic", padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Terminal 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        self.save_cancel_frame = Frame(self.export_frame, bg=background)
        self.save_cancel_frame.grid(row=5, pady=10)

        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, pady=10)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temp Converter")
    something = Converter(root)
    root.mainloop()


