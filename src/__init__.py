from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color,blue,white,red,black

from bs4 import BeautifulSoup
import requests
import re
import sys,os,subprocess
import itertools
from PIL import Image

import time
from collections import Counter