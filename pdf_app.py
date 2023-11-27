from pypdf import PdfReader
#from PyPDF2 import PdfReader
#import streamlit as st
from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time

clicks = 0


#reader = PdfReader("C:/Users/yana5/Downloads/tutorial-example.pdf")
reader = PdfReader("C:/Users/yana5/Documents/Яна/ИТМО/example 2.pdf")
number_of_pages = len(reader.pages)
pageNum = 0
def click_next():
    global pageNum
    if pageNum+1<number_of_pages:
        pageNum+=1
        editor.delete('1.0', 'end')
        editor.insert('insert', reader.pages[pageNum].extract_text())

def click_prev():
    global pageNum
    if pageNum - 1 >= 0:
        pageNum -= 1
        editor.delete('1.0', 'end')
        editor.insert('insert', reader.pages[pageNum].extract_text())

#print(page.extract_text())
root = Tk()
root.title("pdf_app")
root.geometry("700x700+20+20")


editor = Text()
editor.pack(fill=BOTH, expand=1)
page = reader.pages[pageNum]
editor.insert("1.0", page.extract_text())  # вставка в начало
#editor.insert(END, "\nBye World")  # вставка в конец


def get_selection():
    #label["text"] = editor.selection_get()
    translated = GoogleTranslator(source='auto', target='en').translate(
        editor.selection_get())
    label["text"] = translated


def clear_selection():
    editor.selection_clear()


#editor = Text(height=5)
#editor.pack(fill=X)

label = ttk.Label()
label.pack(anchor=NW)

get_button = ttk.Button(text="Get selection", command=get_selection)
get_button.pack(side=LEFT)
clear_button = ttk.Button(text="Clear", command=clear_selection)
clear_button.pack(side=RIGHT)

btnNext = ttk.Button(text='следующая страница', command=click_next)
btnNext.pack()
btnPrev = ttk.Button(text='предыдущая страница', command=click_prev)
btnPrev.pack()

root.mainloop()
#st.write(root)



