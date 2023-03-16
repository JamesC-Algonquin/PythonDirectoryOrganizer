import os
import tkinter
from tkinter import filedialog as fd
import organizer


def select_directory():
    # select directory when button pressed
    directory_text = fd.askdirectory()
    directoryLineText.set(directory_text)


def start_organizer():
    # start the organizer methods
    path = directoryLine.get()
    organizer.sort_files(file_path=path)


def config_json():
    # open json file
    os.startfile("config.json")


# create main GUI window
window = tkinter.Tk()
window.title(" Directory Organizer")
window.configure(background="#dfe0e0")

# label for directory input line
directoryLabel = tkinter.Label(window, text="Directory: ", background="#dfe0e0")
directoryLabel.grid(row=0, column=0, pady=15, sticky="e")

# create entry line for manual or automatic directory path
directoryLineText = tkinter.StringVar()
directoryLine = tkinter.Entry(window, width=36, textvariable=directoryLineText)
directoryLine.grid(row=0, column=1, columnspan=3)

# button activates automatic directory path output from OS File Explorer
directoryButton = tkinter.Button(window, width=8, text="...", command=select_directory)
directoryButton.grid(row=0, column=4)

# button to start organization of directory
startButton = tkinter.Button(window, text="Organize Directory", width=18, command=start_organizer)
startButton.grid(row=1, column=0, pady=5, padx=5)

configButton = tkinter.Button(window, text="Config", width=18, command=config_json)
configButton.grid(row=1, column=2, pady=5, padx=5)

# button to close window
closeButton = tkinter.Button(window, text="Close", width=18, command=window.destroy)
closeButton.grid(row=1, column=4, pady=5, padx=5)

# Main GUI loop
window.mainloop()
