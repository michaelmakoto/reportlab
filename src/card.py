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

    # --- generate card frame and place words ---
    def set_frame(self,canvas,cordX,cordY,frame_option=1):
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
        
        canvas.setFont('HeiseiMin-W3', 15)
        canvas.drawCentredString(half_x *mm, (half_y - 7.5) *mm, self.japanese)

        # add sentence
        # self.get_sentence()
        # canvas.setFont('Times-Bold', 8)
        # canvas.drawCentredString(half_x *mm, (half_y - 20) *mm, self.sentence)

        # add toeic score
        canvas.setFont('Times-Bold', 8)
        canvas.drawCentredString((half_x + 40)*mm, (half_y - 25) *mm, str(self.toeic))

        return None

    # --- calculate the init postion for the card
    def calculate_card_pos_x(self,XX):
        return (self.paper_margin_x + (self.card_width + self.card_gap_x) * XX) 
    
    # --- calculate the init postion for the card
    def calculate_card_pos_y(self,YY):
        return (self.paper_margin_y + (self.card_height + self.card_gap_y) * YY)


