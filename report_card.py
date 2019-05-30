from src import *
from src.card import Card
from src.translate import Translate

#--- set card class for every word----
def set_up_card(word):
    # get translation first
    t = Translate(word)
    t.get_toeic()
    t.get_part()
    t.get_japanese()

    # if the japanese is too long restrict it
    if (len(t.japanese) >= 16):
        t.restrict_japanese()

    # set up card class with translation data
    c = Card(word)
    c.japanese = t.japanese
    c.toeic = t.toeic
    c.part = t.part
    
    return c

#--- main ---
start = time.time()

print('start...')
canvas = canvas.Canvas("card.pdf")
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

listOfWrods = [
    'Commission','commercial','irritating','radiation',
    'electromagnetic','cancer','sequence','infer'
    
]
    
index = 0
final_index = len(listOfWrods)
cards = [set_up_card(l) for l in listOfWrods]

print('\nstart printing...')
while (index < final_index):
    for x,y in itertools.product(range(2),range(5)):
        try:
            print(index,cards[index].word)
            cards[index].set_backgroud(canvas,x,y)
            cards[index].set_main_frame(canvas,x,y,0)
            index += 1
        except IndexError:
            break
        except:
            break
    print('finished one page')
    canvas.showPage()

canvas.save()
print('done...')
end = time.time()
print('time: {}[sec]'.format(end - start))

os.system('open card.pdf')
