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


# create main GUI window
window = tkinter.Tk()
window.title(" Directory Organizer")

# label for directory input line
directoryLabel = tkinter.Label(window, text="Directory: ")
directoryLabel.grid(row=0)

# create entry line for manual or automatic directory path
directoryLineText = tkinter.StringVar()
directoryLine = tkinter.Entry(window, width=36, textvariable=directoryLineText)
directoryLine.grid(row=0, column=1, columnspan=2)

# button activates automatic directory path output from OS File Explorer
directoryButton = tkinter.Button(window, width=8, text="...", command=select_directory)
directoryButton.grid(row=0, column=3)

# button to start organization of directory
startButton = tkinter.Button(window, text="Organize Directory", width=18, command=start_organizer)
startButton.grid(row=1, column=0)

# button to close window
closeButton = tkinter.Button(window, text="Close", width=18, command=window.destroy)
closeButton.grid(row=1, column=3)

# Main GUI loop
window.mainloop()
