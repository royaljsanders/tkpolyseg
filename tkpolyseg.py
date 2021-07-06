from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import subprocess
import sys

class FeetToMeters:
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
    def selectinputdir(self, *args):
        dirname = fd.askdirectory()
        self.input.set(dirname)
        #showinfo(title='Selected Folder', message=dirname)

    def selectoutputdir(self, *args):
        dirname = fd.askdirectory()
        self.output.set(dirname)

    def gobutton(self, *args):
        print(self.input.get(), self.output.get(), self.split_value.get())
        if sys.platform.startswith('win32'):
            # run main_seg_win.py
            print("win!")
            #subprocess.run(["conda", "activate", "snapshot"])
            subprocess.run(["C:/ProgramData/Anaconda3/envs/snapshot/python.exe", "C:/Polygon_Segmentation_9_Classes/main_seg_win.py", self.input.get(), self.output.get(), self.split_value.get()])
        elif sys.platform.startswith('linux'):
            # run main_seg_linux.py
            print("lin!")

    def __init__(self, root):
        # "Trail Camera Polygon Segmentation Model Training Tool"
        root.title("Polyseg Trainer Tool")


        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Input Folder:").grid(column=1, row=1, sticky=W)

        self.input = StringVar("")
        input_text = ttk.Entry(mainframe, width=42, textvariable=self.input)
        input_text.grid(column=1, row=2, sticky=(W, E))

        input_button = ttk.Button(mainframe, text="Browse", command=self.selectinputdir).grid(column=2, row=2, sticky=E)

        ttk.Label(mainframe, text="Output Folder:").grid(column=1, row=3, sticky=W)

        self.output = StringVar()
        output_entry = ttk.Entry(mainframe, width=42, textvariable=self.output)
        output_entry.grid(column=1, row=4, sticky=(W, E))

        output_button = ttk.Button(mainframe, text="Browse", command=self.selectoutputdir).grid(column=2, row=4, sticky=E)

        split_label = ttk.Label(mainframe, text="Split:").grid(column=1, row=5, sticky=W)
        self.split_value = StringVar()
        self.split_value.set("0.9")
        s = ttk.Spinbox(mainframe, from_=0.0, to=1.0, increment=0.05, textvariable=self.split_value).grid(column=1, row=5)

        # self.go_value = StringVar()
        ttk.Button(mainframe, text="Go", command=self.gobutton).grid(column=2, row=5)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        input_text.focus()
        root.bind("<Return>", self.calculate)



root = Tk()

FeetToMeters(root)
root.mainloop()