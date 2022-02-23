import tkinter as tk
import _winapi
import keyboard
import sys
from tkinter import font
from tkinter import ttk

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Metre Conversion Software")
    root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.resizable(False, False)
    root.columnconfigure(0, weight=1)

    feetConverted = tk.StringVar()
    feetConverted.set("Feet shown here")

    def convertInfeet(*args):
        feetConverted.set(3.28084*int(metreEntry.get()))


    main = ttk.Frame(root, padding=(15,10))
    main.grid(column=0,row=0)

    metreLabel = ttk.Label(main, text="Metres", width=10)
    metreLabel.grid(column=0, row=0, sticky="EW", padx=5, pady=5)

    metreEntry = ttk.Entry(main)
    metreEntry.grid(column=1, row=0, padx=15, pady=10, sticky="W")

    feetLabel = ttk.Label(main, text="Feet")
    feetLabel.grid(column=0, row=1, sticky="EW", padx=5, pady=5)

    feetLabelfinal = ttk.Label(main, textvariable=feetConverted, font=("Segoi-ui",45))
    feetLabelfinal.grid(column=1, row=1, sticky="EW", padx=15, pady=10)

    submitButton = ttk.Button(main, text="Calculate", command=convertInfeet)
    submitButton.grid(column=0, row=2, columnspan=2, sticky="EW", padx=15, pady=10)

    metreEntry.focus()
    root.bind("<Return>", convertInfeet)
    root.bind("KP_enter", convertInfeet)
    root.bind("q", sys.exit)


    root.mainloop()