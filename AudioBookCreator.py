# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 10:58:17 2022

@author: Pierre-Henri Rossouw

Create audio book from PDF


"""

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))

import pyttsx3
speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()

