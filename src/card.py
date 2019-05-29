from src import *
from src.translate import Translate

class Card:
    def __init__(self,word):
        self.card_width = 91
        self.card_height = 55
        self.paper_margin_x = 12
        self.paper_margin_y = 7
        self.card_gap_x = 4
        self.card_gap_y = 2
        
        # get word translation data from Translate class
        self.translation =  Translate(word)
        self.word = word
        self.japanese = self.translation.japanese
        self.toeic = self.translation.toeic
        self.part = self.translation.part

        # card settings
        # rgb = [green,beige,yellow,orange,purpole]
        self.color_set = [[133,202,171], [256,198,176], [252, 209, 112], [251, 75, 61], [70, 10, 62]]
        
        # defult color
        self.color = [0,0,0]
        self.r = 2.5


    # --- generate card frame and place words ---
    def set_main_frame(self,canvas,cordX,cordY,frame_option=1):

        canvas.setFillColor(black)
        # calcuate the starting postion for printing the card
        posX = self.calculate_card_pos_x(cordX)
        posY = self.calculate_card_pos_y(cordY)

        # create frame
        if (frame_option != 1):
            pass
        else:
            canvas.setLineWidth(.1)
            canvas.rect(posX*mm, posY*mm, self.card_width*mm, self.card_height*mm)

        # calculate the center of the card
        half_x = (posX + posX + self.card_width) / 2
        half_y = (posY + posY + self.card_height) / 2

        # add English
        canvas.setFont('Times-Bold', 20)
        canvas.drawCentredString(half_x *mm, (half_y + 7.5) *mm, self.word)
        
        # add japanese
        canvas.setFont('HeiseiMin-W3', 15)
        canvas.drawCentredString(half_x *mm, (half_y - 7.5) *mm, self.japanese)

        # add sentence
        # self.get_sentence()
        # canvas.setFont('Times-Bold', 8)
        # canvas.drawCentredString(half_x *mm, (half_y - 20) *mm, self.sentence)

        canvas.setFillColor(white)
        # add toeic score
        canvas.setFont('Times-Bold', 14)
        canvas.drawString((posX + 77.7) *mm, (posY + self.card_height - 52.1) *mm, str(self.toeic))

        # add part
        canvas.setFont('HeiseiMin-W3', 12)
        canvas.drawString((posX + 7) *mm, (posY + self.card_height - 52.1) *mm, self.part)

        return None


    def set_color(self):
        toeic = self.toeic
        if 0 <= toeic and toeic < 300:
            selector = 0
        elif 301 <= toeic and toeic < 500:
            selector = 1
        elif 501 <= toeic and toeic < 600:
            selector = 2
        elif 601 <= toeic and toeic < 799:
            selector = 3
        elif 800 <= toeic and toeic <= 990:
            selector = 4

        try:
            r = self.color_set[selector][0] / 255
            g = self.color_set[selector][1] / 255
            b = self.color_set[selector][2] / 255
            self.color = [r,g,b]
            print('set_color({}) is {}'.format(self.word, str(selector)))
        except:
            print('set_color({}) failed'.format(self.word))


    # --- set backgroud ---
    def set_backgroud(self,canvas,cordX,cordY,offsetX=0, offsetY=0):
        self.set_color()
        posX = self.calculate_card_pos_x(cordX)
        posY = self.calculate_card_pos_y(cordY)
        
        # background
        canvas.setFillColor(self.color)
        canvas.rect((posX - offsetX)  *mm,(posY - offsetY) *mm,
                    (offsetX*2 + self.card_width) *mm, (offsetY*2 + self.card_height) *mm,
                    fill=True, stroke=False)

        # white space
        canvas.setFillColor(white)

        # center white
        canvas.rect((posX + 5.7) *mm, (posY + self.card_height - 45.7)*mm, 
                    79.7 *mm, 42.5 *mm, fill=True, stroke=False)
        # right rect
        canvas.rect((posX + 85.2) *mm, (posY + self.card_height - 43.2)*mm,
                    2.6 *mm, 37.5 *mm, fill=True, stroke=False )
        # left rect
        canvas.rect((posX + 3.2) *mm, (posY + self.card_height - 43.2)*mm,
                    2.6 *mm, 37.5 *mm, fill=True, stroke=False)

        # top right
        canvas.circle((posX + 85.3) *mm, (posY + self.card_height - 5.7) *mm,
                    self.r *mm, fill=True,stroke=False)
        # top left
        canvas.circle((posX + 5.7) *mm, (posY + self.card_height - 5.7) *mm,
                    self.r *mm, fill=True,stroke=False)
        # down rignt
        canvas.circle((posX + 85.3) *mm, (posY + self.card_height - 43.2) *mm,
                    self.r *mm, fill=True,stroke=False)
        # down left
        canvas.circle((posX + 5.7) *mm, (posY +  self.card_height - 43.2) *mm,
                    self.r *mm, fill=True,stroke=False)


    # --- calculate the init postion for the card
    def calculate_card_pos_x(self,XX):
        return (self.paper_margin_x + (self.card_width + self.card_gap_x) * XX) 
    
    # --- calculate the init postion for the card
    def calculate_card_pos_y(self,YY):
        return (self.paper_margin_y + (self.card_height + self.card_gap_y) * YY)


