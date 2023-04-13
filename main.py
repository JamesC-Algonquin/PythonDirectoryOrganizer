import os
import tkinter
import tkinter.messagebox
from tkinter import filedialog as fd
from tkinter import scrolledtext as st
import organizer


def select_directory():
    # select directory when button pressed
    directory_text = fd.askdirectory()
    directoryLineText.set(directory_text)


def start_organizer():
    # start the organizer methods
    path = directoryLine.get()
    if not path:
        append_log("Please Select a Directory\n")
    else:
        organizer.sort_files(file_path=path, exception_callback=append_log)


def config_json():
    # open json file
    os.startfile("config.json")


def append_log(text):
    logText.configure(state='normal')
    logText.insert(tkinter.INSERT, "\n --")
    logText.insert(tkinter.INSERT, text)
    logText.see("end")
    logText.configure(state='disabled')


def restore_default():
    restore = tkinter.messagebox.askyesno(title="Confirm",
                                          message="Are you sure you want to restore default configuration?")
    if restore:
        organizer.restore_default(append_log)
    else:
        return


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

logText = st.ScrolledText(window, width=80, height=10, font=("Times New Roman", 9))
logText.grid(columnspan=5, padx=2, pady=4)
logText.configure(state='disabled')

# button to start organization of directory
startButton = tkinter.Button(window, text="Organize Directory", width=18, command=start_organizer)
startButton.grid(row=2, column=0, pady=5, padx=5)

configButton = tkinter.Button(window, text="Config", width=18, command=config_json)
configButton.grid(row=2, column=2, pady=5, padx=5)

# button to close window
closeButton = tkinter.Button(window, text="Restore Defaults", width=18, command=restore_default)
closeButton.grid(row=2, column=4, pady=5, padx=5)

# Main GUI loop
window.mainloop()
