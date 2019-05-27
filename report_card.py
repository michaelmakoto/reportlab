from src import *
from src.card import Generate_card

print('start...')
canvas = canvas.Canvas("form.pdf")
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

listOfWrods = [
    'flap','icy','ugliest',
    'unknown','crowded','attack','ink','apple',
    'participate','alien','process','ambition',
    'flap','icy','ugliest','unknown',
    'crowded','attack','ink','apple'
    ]
    
count = 0
final_count = len(listOfWrods)

while (count < final_count):
    for x,y in itertools.product(range(2),range(5)):
        try:
            word = listOfWrods[count]
            print(count,word)
            cards = Generate_card(word)
            cards.set_frame(canvas,x,y)
            count += 1
        except IndexError:
            break
    print('finished one page')
    canvas.showPage()

canvas.save()
print('done...')
os.system('open form.pdf')