from gtts import gTTS
import PyPDF2
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import os

LIGHT_BLUE = "#a4ebf3"
BLUE = "#0a043c"
ORANGE = "#ff6701"


def choose():
    file_path = askopenfile(mode='r', filetypes=[('All files', '*.pdf')])
    if file_path is not None:
        speech(file_path.name)


def speech(file_path):
    pdf_path = file_path
    pdf = PyPDF2.PdfFileReader(str(pdf_path))
    name = file_path.split("/")[-1]
    new_path = "/".join(file_path.split("/")[:-1])
    temp_path = new_path + "/temp.txt"
    with open('temp.txt', mode="a") as output_file:
        for page in pdf.pages:
            text = page.extractText()
            output_file.write(text)
            tts = gTTS(text)
            tts.save(f"{new_path}/audio_{name}.mp3")
            delete(temp_path)
            showinfo(message=f"Your file has been converted into a mp3 file named 'audio_{name}'.",
                     title="Your file is ready!")


def delete(temp):
    if os.path.exists(temp):
        os.remove(temp)


window = Tk()
window.title("PDF To Speech")
window.config(padx=50, pady=50, bg=LIGHT_BLUE)
window.resizable(width=False, height=False)

label = Label(window, text="This program will create a single mp3 file for the pdf you submit.\nIt"
                           " will download the mp3 file to the same directory in which your submitted pdf is.",
              fg="#1b1a17", bg=LIGHT_BLUE, font=("Arial", 12), )
label.grid(row=0, column=0)

btn = Button(window, text="Upload PDF", bg=ORANGE, font=("Arial", 10), command=choose)
btn.grid(row=1, column=0, pady=30)

window.mainloop()
