from src import *

class Translate:
    def __init__(self,word):
        self.word = word
        self.url = 'https://ejje.weblio.jp/content/' + word
        self.res = requests.get(self.url)
        self.soup = BeautifulSoup(self.res.content,features="html5lib")

        self.japanese = 'None'
        self.toeic = '---'
        self.sentence = 'None'
        self.part = '不明'

        self.get_toeic()
        self.get_japanese()
        self.get_part()

        if (len(self.japanese) >= 16): 
            self.restrict_japanese()

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


    # --- control the length of the Japanese translation ---
    def restrict_japanese(self):
        new_translation= input('new translation for {}:'.format(self.word))
        
        if (len(new_translation) >= 16):
            print('must be under 16 words....')
            return self.restrict_japanese()
        else:
            self.japanese =  new_translation
            print('done...')


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


    # --- get 品詞 ---
    def get_part(self):
        part = self.soup.find("div", attrs={"class","KnenjSub"})
        try:
            self.part = part.get_text().split(' ')[0]
        except:
            print('get_part({}) failed'.format(self.word))