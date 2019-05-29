from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.colors import Color,blue,white

from bs4 import BeautifulSoup
import requests
import re
import sys,os
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

#card color

r = 2.5

# ---- main thread from here ----
print('start...')
canvas = canvas.Canvas("form.pdf")
canvas.setLineWidth(.1)
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

canvas.rect(0,0,card_width *mm, card_height *mm)
my_green = Color(133/255,202/255,171/255)
my_white = Color(1,1,1)

# backgroug
canvas.setFillColor(my_green)
canvas.rect(0,0,card_width *mm,card_height *mm,fill=True,stroke=False)

# white space
canvas.setFillColor(my_white)

# center white
canvas.rect(5.7 *mm, (card_height - 45.7)*mm, 79.7 *mm, 42.5 *mm,fill=True,stroke=False)
# right rect
canvas.rect(85.4 *mm, (card_height - 43.2)*mm, 2.4 *mm, 37.5 *mm,fill=True,stroke=False )
# left rect
canvas.rect(3.2 *mm, (card_height - 43.2)*mm, 2.5 *mm, 37.5 *mm,fill=True,stroke=False)

# top right
canvas.circle(85.3 *mm, (card_height - 5.7) *mm , r *mm, fill=True,stroke=False)
# top left
canvas.circle(5.7 *mm, (card_height - 5.7) *mm , r *mm, fill=True,stroke=False)
# down rignt
canvas.circle(85.3 *mm, (card_height - 43.2) *mm , r *mm, fill=True,stroke=False)
# down left
canvas.circle(5.7 *mm, (card_height - 43.2) *mm , r *mm, fill=True,stroke=False)



canvas.save()
print('done...')
os.system('open form.pdf')
