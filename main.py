import sqlite3

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.screen import MDScreen

from style import myStyle

class MDScreen1(MDScreen):
    pass

class MDScreen2(MDScreen):
    pass

class DemoApp(MDApp):
    conn = sqlite3.connect('ascshc_data.db')
    print("[!]Connection to database established")
    c = conn.cursor()
    c.execute("SELECT number FROM tblHymns")
    numberHymns = c.fetchall()
    c.execute("SELECT title FROM tblHymns")
    titleHymns = c.fetchall()
    conn.commit()

    def build(self):
        self.theme_cls.primary_palette ="Purple"
        screen = Builder.load_string(myStyle)
        return screen

    def on_start(self):
        for self.number in self.numberHymns:
            self.c.execute("SELECT title FROM tblHymns where number = %s" % (self.number))
            titleHymns = self.c.fetchall()
            self.conn.commit()
            self.items = TwoLineListItem(text=str(self.number)[1:-2], secondary_text=str(titleHymns)[3:-4],
                                    on_release=self.show_hymn, _txt_left_pad="30dp",
                                    pos_hint={"x":0, "y": .5}, size_hint=(.8,1),font_style="H5")
            self.root.ids.myMdList.add_widget(self.items)


    def myOnText(self):
        self.root.ids.myMdList.clear_widgets()
        myFieldtext=self.root.ids.myTextField.text
        if myFieldtext == "":
            self.on_start()
            print("MainList Loaded")
        else:
            filteredText=self.root.ids.myTextField.text
            self.c.execute(
                "SELECT number FROM tblHymns where number LIKE '%{}%' OR title like '%{}%'".format(filteredText,
                                                                                                   filteredText))
            number = self.c.fetchall()
            self.conn.commit()
            for num in number:
                # print("num: " + str(num))
                numn=str(num)[1:-2]
                # print("striped: "+ numn)

                self.c.execute("SELECT title FROM tblHymns where number LIKE '{}' ".format(numn))
                titleHymns = self.c.fetchall()
                self.conn.commit()
                # print("title: " + str(titleHymns))
                self.itemsFiltered = TwoLineListItem(text=str(num)[1:-2], secondary_text=str(titleHymns)[3:-4],
                                                 on_release=self.show_hymn, _txt_left_pad="30dp",
                                                 pos_hint={"x": 0, "y": .5}, size_hint=(.8, 1))
                self.root.ids.myMdList.add_widget(self.itemsFiltered)


    def show_hymn(self, twolinelistitem):
        self.root.current = "viewscreen"
        self.myText = twolinelistitem.text

        self.c.execute("SELECT title FROM tblHymns where number = %s" % (self.myText))
        self.titleHymns = self.c.fetchone()
        self.conn.commit()

        self.c.execute("SELECT description FROM tblHymns where number = %s" % (self.myText))
        self.descriptionHymns = self.c.fetchone()
        self.conn.commit()
        self.descriptionHymns = str(self.descriptionHymns).replace('\\n', '\n').replace('\\t', '\t')


        self.c.execute("SELECT body FROM tblHymns where number = %s" % (self.myText))
        self.bodyHymns = self.c.fetchall()
        self.conn.commit()

        formattedBody = str(self.bodyHymns).replace('\\n', '\n').replace('\\t', '\t')
        self.c.execute("SELECT composedby FROM tblHymns where number = %s" % (self.myText))
        self.composedbyHymns = self.c.fetchone()
        self.conn.commit()

        self.root.ids.myMdLabelNumber.text = "ASCSHC " + self.myText
        self.root.ids.myMdLabelTitle.text = str(self.titleHymns)[2:-3]
        self.root.ids.myMdLabelDescription.text = str(self.descriptionHymns)[2:-3]
        self.root.ids.myMdLabelBody.text = str(formattedBody)[2:-3]
        self.root.ids.myMdLabelComposedBy.text = str(self.composedbyHymns)[2:-3]

    def myGo_back(self):
        self.root.current="listscreen"

    def prev_hymn(self):
        twolinelistitem=TwoLineListItem(text=str(int(self.myText)-1))
        if int(twolinelistitem.text) >=1:
            self.show_hymn(twolinelistitem)

    def next_hymn(self):
        twolinelistitem = TwoLineListItem(text=str(int(self.myText) + 1))
        if int(twolinelistitem.text) <= len(self.numberHymns):
            self.show_hymn(twolinelistitem)

DemoApp().run()