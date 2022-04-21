myStyle = """
ScreenManager:
    MDScreen1:
        name:"listscreen"
        MDBoxLayout:
            orientation:"vertical"
            MDToolbar:
                title: "ASCSHC"
                # left_action_items: [["menu"]]
                elevation: 10
                # icon:"git"
            MDTextField:
                id:myTextField
                icon_left: 'magnify'
                mode: "rectangle"
                hint_text: "Search"
                helper_text_mode: "on_focus"
                helper_text: "Type here"
                size_hint: .8,None
                height:"10dp"
                pos_hint: {"center_x": .5, "y": .7}
                on_text:app.myOnText()
            MDBoxLayout:
                orientation:"vertical"
                ScrollView:
                    MDList:                        
                        id: myMdList
                        hovering:"true"
    MDScreen2:
        name:"viewscreen"
        MDBoxLayout:
            orientation:"vertical"
            MDToolbar:
                title: "ASCSHC"
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.myGo_back()]]
                
                
#Hymn Title, number and description                    
            MDCard:
                # id: myMdCard
                orientation:"vertical"
                padding: "10dp"
                size_hint: 1, .2
                # height: "180dp"
                # pos_hint: {"center_x": .5, "center_y": 1}
                MDBoxLayout:
                    MDFlatButton:
                        text:"Prev"
                        size_hint:None,1
                        width:self.parent.width/10
                        on_press:app.prev_hymn()
                    MDBoxLayout:
                        orientation:"vertical" 
                        size_hint:.8,1    
                        MDLabel:
                            id: myMdLabelNumber
                            font_style:"H5"
                            halign:"center"                    
                        MDLabel:
                            id: myMdLabelTitle
                            font_style:"Subtitle1"
                            halign:"center"
                        MDSeparator:
                            height: "1dp"
                            pos_hint: {"center_x": .5, "center_y": 1}
                        MDLabel:
                            id: myMdLabelDescription
                            font_style:"Caption"
                            halign:"center"
                    MDFlatButton:
                        text:"Next"
                        size_hint:None,1
                        width:self.parent.width/10
                        on_press:app.next_hymn()
          
#Body Card                    
            MDCard:
                # id: myMdCardBody
                orientation:"vertical"
                padding: "20dp"
                margin:"10dp"
                size_hint: 1, .65
                # height: "180dp"
                # pos_hint: {"center_x": .5, "center_y": 1} 
                ScrollView:
                    pos_hint: {'center_y': .5, 'center_x': .5}
                    size_hint: .9, .8            
                    MDLabel:
                        id: myMdLabelBody
                        font_style:"Subtitle1"
                        adaptive_height:"true"
                        markup:"true"
                        halign:"left"
           
           
#ComposedBY           
            MDCard:
                orientation:"vertical"
                padding: "20dp"
                size_hint: 1, .05
                # height: "50dp"
                # pos_hint: {"center_x": .5, "center_y": 1}                    
                MDLabel:
                    id: myMdLabelComposedBy
                    font_style:"Caption"
                    halign:"right"

"""