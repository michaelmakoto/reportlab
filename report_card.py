from src import *
from src.card import Card

print('start...')
canvas = canvas.Canvas("card.pdf")
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

listOfWrods = [
    'rumor','self',
    'feeling','harassment','rumor','self',
    'feeling','harassment'
]
    
count = 0
final_count = len(listOfWrods)

while (count < final_count):
    for x,y in itertools.product(range(2),range(5)):
        try:
            word = listOfWrods[count]
            print(count,word)

            card = Card(word)

            card.set_backgroud(canvas,x,y,2,1)
            card.set_main_frame(canvas,x,y)

            count += 1
        except IndexError:
            break
    print('finished one page')
    canvas.showPage()

canvas.save()
print('done...')
os.system('open card.pdf')