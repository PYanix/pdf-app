from pypdf import PdfReader
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
from transformers import pipeline
'''from parrot import Parrot
import warnings
warnings.filterwarnings("ignore")'''

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
'parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)'

reader = PdfReader("C:/Users/yana5/Documents/Яна/ИТМО/1469_ud.pdf")
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

root = Tk()
root.title("pdf_app")
root.geometry("700x700+20+20")


editor = Text()
editor.pack(fill=BOTH, expand=1)
page = reader.pages[pageNum]
editor.insert("1.0", page.extract_text())

def translate_text():
    text = editor.selection_get()
    translated = GoogleTranslator(source='auto', target='ru').translate(
        text)
    #label["text"] = translated
    window = Tk()
    window.title("Translated text")
    window.geometry("350x300")
    extra_editor = Text(window)
    extra_editor.pack(fill=BOTH, expand=1)
    extra_editor.insert("1.0", text+'\n\n'+translated)
    close_button = ttk.Button(window, text="Close window", command=lambda: window.destroy())
    close_button.pack(anchor="center", expand=1)

def summary_text():
    text = editor.selection_get()
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0].get('summary_text')
    window = Tk()
    window.title("Summary")
    window.geometry("350x300")
    extra_editor = Text(window)
    extra_editor.pack(fill=BOTH, expand=1)
    extra_editor.insert("1.0", summary)
    close_button = ttk.Button(window, text="Close window", command=lambda: window.destroy())
    close_button.pack(anchor="center", expand=1)

'''def paraphrase_text():
    text = editor.selection_get()
    para_phrases = parrot.augment(input_phrase=text, max_return_phrases=2)
    while(type(para_phrases)== 'NoneType'):
        para_phrases = parrot.augment(input_phrase=text, max_return_phrases=2)

    paraphrase = para_phrases[0][0]
    label["text"] = paraphrase'''


label = ttk.Label()
label.pack(anchor=NW)

btnTranslate = ttk.Button(text="translate", command=translate_text)
btnTranslate.pack(side=LEFT)
btnSummary = ttk.Button(text="summary", command=summary_text)
btnSummary.pack(side=LEFT)
'''btnParaphrase = ttk.Button(text="paraphrase", command=paraphrase_text)
btnParaphrase.pack(side=LEFT)'''

btnNext = ttk.Button(text='next page', command=click_next)
btnNext.pack(side=RIGHT)
btnPrev = ttk.Button(text='previous page', command=click_prev)
btnPrev.pack(side=RIGHT)

root.mainloop()

