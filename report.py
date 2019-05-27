from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from bs4 import BeautifulSoup
import requests
import re
import sys,os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import itertools

from PIL import Image

# card size
card_width = 91
card_height = 55

#A4 paper margin
margin_x = 12
margin_y = 7

#card gap
gap_x = 4
gap_y = 2

#list of words
listOfWrods = [
    'sweltering','outgoing','flap','icy','ugliest',
    'unknown','crowded','attack','ink','apple',
    'participate','alien'
    ]

#soup object

# ---- main thread from here ----
print('start...')
canvas = canvas.Canvas("form.pdf")
canvas.setLineWidth(.1)
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

filename = './img/card.png'
im = Image.open(filename)
width, height = im.size

print(width, height)

canvas.drawImage(filename,(12 + 0)*mm,(7 + 0)*mm)
canvas.drawImage(filename,(12 + 4 + 91)*mm,(7 + 2 + 55)*mm)
canvas.drawImage(filename,(12 + 0)*mm,(7 + 2 + 55)*mm)
canvas.drawImage(filename,(12 + 4 + 91)*mm,(7 + 0)*mm)

canvas.save()
print('done...')
os.system('open form.pdf')
