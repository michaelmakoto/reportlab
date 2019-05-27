from src import *

class Generate_card:
    def __init__(self,word):
        self.word = word
        self.url = 'https://ejje.weblio.jp/content/' + word
        self.res = requests.get(self.url)
        self.soup = BeautifulSoup(self.res.content,features="html5lib")

        self.japanese = 'None'
        self.toeic = 0
        self.sentence = 'None'

        self.card_width = 91
        self.card_height = 55
        self.paper_margin_x = 12
        self.paper_margin_y = 7
        self.card_gap_x = 4
        self.card_gap_y = 2
    
    #--- change url ---
    def switch_source(self,option='sentence'):
        if (option is 'sentence'):
            url = 'https://sentence.yourdictionary.com/' + self.word
        else:
            url = 'https://ejje.weblio.jp/content/' + self.word
            
        self.res = requests.get(url)
        self.soup = BeautifulSoup(self.res.content,features="html5lib")
    
    # ---- get an example sentence ---
    def get_sentence(self):
        self.switch_source()
        try:
            self.sentence = self.soup.find("div", class_ = 'li_content').get_text()
        except:
            pass
        # swith aoup back to weblio
        self.switch_source(option='translation')

    # --- translation func ---
    def get_japanese(self):
        translation = self.soup.find("td", attrs={"class":"content-explanation"})
        try:
            # extract only the frist translation
            oneJWord = translation.get_text().split('、')
            self.japanese = oneJWord[0]
        except:
            print('get_japanese({}) failed'.format(self.word))
    
     # --- toeic func ---
    def get_toeic(self):
        learningContent = self.soup.find_all("span", attrs={"class":"learning-level-content"})
        try:
            learningContentText = [C.get_text() for C in learningContent]
            check_toeic = re.compile("(\d\d\d)点以上")
            toeic = [e for e in learningContentText if check_toeic.match(e)]
            self.toeic =  int(toeic[0].replace('点以上の単語',""))
        except:
            print('get_toeic({}) failed'.format(self.word))

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

        # add Japanese
        self.get_japanese()
        canvas.setFont('HeiseiMin-W3', 15)
        canvas.drawCentredString(half_x *mm, (half_y - 7.5) *mm, self.japanese)

        # add sentence
        # self.get_sentence()
        # canvas.setFont('Times-Bold', 8)
        # canvas.drawCentredString(half_x *mm, (half_y - 20) *mm, self.sentence)

        # add toeic score
        self.get_toeic()
        canvas.setFont('Times-Bold', 8)
        canvas.drawCentredString((half_x + 40)*mm, (half_y - 25) *mm, str(self.toeic))

        return None


    # --- calculate the init postion for the card
    def calculate_card_pos_x(self,XX):
        return (self.paper_margin_x + (self.card_width + self.card_gap_x) * XX) 
    
    # --- calculate the init postion for the card
    def calculate_card_pos_y(self,YY):
        return (self.paper_margin_y + (self.card_height + self.card_gap_y) * YY)


