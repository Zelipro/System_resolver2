from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView

from kivy.uix.boxlayout import BoxLayout
import Outils.Cramer as Cr
import Outils.Gauss as Gu
import Outils.LU 
#Window.size = (350,600)


style = """
#:import NoTransition kivy.uix.screenmanager.NoTransition
MDBoxLayout:
    orientation:"vertical"
    FloatLayout:
        size_hint:(1,0.1)
        # MDTopAppBar (La barre d'outils en bas)
        MDTopAppBar:
            id: Appui
            title: "Cramer"
            left_action_items: [["swap-horizontal", lambda x: app.refrech()]]
            elevation: 3
            pos_hint: {"top": 1}  # Positionne la barre en haut

        # MDCard (La carte avec l'image)
        MDCard:
            size_hint: (None, None)
            height: Appui.height  # Correspond à la hauteur de la barre
            width: Appui.height  # Rendre la carte carrée
            elevation: 3
            radius: [Appui.height / 2]  # Bordure arrondie pour un cercle parfait
            #md_bg_color:(103 / 255, 58 / 255, 183 / 255, 1)
            md_bg_color:(1,1,1,1)
            pos_hint: {"right": 1, "top": 1}  # Aligné à droite sur la barre

            AsyncImage:
                source: "Img.png"
                size_hint: (None, None)
                size: (Appui.height , Appui.height - 15)  # Ajustement de l'image
                pos_hint: {"center_x": 0.5, "center_y": 0.5}  # Centrage dans le MDCard

    ScreenManager:
        id:cr
        transition:NoTransition()
        MDScreen:
            name:"Page_1"
            MDBoxLayout:
                orientation:"vertical"
                pos_hint:{"center_y":1}
                MDTextField:
                    id:Taille
                    mode:'line'
                    input_filter:"int"
                    hint_text:'Taille de La Matrix'
                    halign:"center"
                    
                
                MDRaisedButton:
                    text:'Valider'
                    size_hint:(None,None)
                    width:Taille.width-10
                    pos_hint:{"center_x":.5}
                    on_press:app.Valider1(root)
                    
        MDScreen:
            name:"Page_2"
            MDBoxLayout:
                orientation:"vertical"
                MDLabel:
                    text:'Matrice A'
                    size_hint:(1,0.1)
                    pos_hint:{"center_y":.5}
                    bold:True
                    color:(1,1,0,1)
                MDScrollView:
                    do_scroll_x:False
                    do_scroll_y:True
                    MDBoxLayout:
                        orientation:'vertical'
                        adaptive_height:True
                        MDGridLayout:
                            id:Page2
                            adaptive_height:True
                            cols:1
                            spacing:5
                            padding:5
                            
                MDRaisedButton:
                    text:'Valider'
                    size_hint_x:.9
                    pos_hint:{"center_x":.5}
                    on_press:app.Appui2()
        MDScreen:
            name:"Page_3"
            MDBoxLayout:
                orientation:'vertical'
                MDLabel:
                    text:'Matrice B'
                    size_hint:(1,0.1)
                    pos_hint:{"center_y":.5}
                    bold:True
                    color:(1,1,0,1)
                MDScrollView:
                    do_scroll_x:False
                    do_scroll_y:True
                    MDBoxLayout:
                        orientation:'vertical'
                        adaptive_height:True
                        MDGridLayout:
                            id:Page3
                            adaptive_height:True
                            cols:1
                            spacing:5
                            padding:5
                            
                MDRaisedButton:
                    text:'Valider'
                    size_hint_x:.9
                    pos_hint:{"center_x":.5}
                    on_press:app.Appui3()
                          
        MDScreen:
            name:'Page_4'
            MDBoxLayout:
                orientation:'vertical'
                pos_hint:{"center_x":.5,"center_y":.5}
                id:Pge4        
            
"""
class ZeliApp(MDApp):
    def build(self):
        self.ind = 0
        self.List = ["Cramer","LU","Gauss"]
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(style)

    
    def refrech(self):
        self.ind += 1
        self.ind %= 3
        self.root.ids.Appui.title = self.List[self.ind]
        self.root.ids.cr.current = "Page_1"
        self.root.ids.Taille.text = ""
        
    
    def Valider1(self,instance):
        val = self.root.ids.Taille.text
        if val == "":
            self.Po = self.show_info(title = "Error",Message = "Ce champs est Obligatoire !",fonct = self.Ok)
        else:
            self.root.ids.cr.current = "Page_2"
            self.Valider2()
    
    def Ok(self,instance):
        self.Po.dismiss()
    
    def show_info(self,title,Message,fonct):
        #Box = MDBoxLayout(orientation = 'vertical')
        #Box.add_widget(Label(text = Message))
        
        Pop = MDDialog(
            title = title,
            text = Message,
            buttons = [
                MDRaisedButton(
            text = "OK",
            on_press = fonct)
            ]
               )
        Pop.open()
        
        return Pop
    
    def Valider2(self):
        FLo = self.root.ids.Page2
        
        size  = int(self.root.ids.Taille.text)
        self.List2 = [[0 for i in range(size) ]for j in range(size)]
        FLo.clear_widgets()
        
        FLo.cols = size
        for i in range(size):
           for j in range(size):
                Text = MDTextField(
                    #hint_text = f"A[{i+1}][{j+1}]",
                    halign = "center",
                )
                self.List2[i][j] = Text
                FLo.add_widget(Text)
    
    def verifier(self,List):
        for elmt in List:
            for elmt2 in elmt:
                if elmt2.text == "":
                    return False
        return True
    
    def Appui2(self):
        pge = self.root.ids.cr
        if not self.verifier(self.List2):
            self.Pop2 = self.show_info(title = "Error",Message="Tous les Champs sont Obligatoire",fonct = self.Ok2)
        else:
            pge.current = "Page_3"
            self.Valider3()
    
    def Ok2(self,instance):
        self.Pop2.dismiss()
    
    
    def Valider3(self):
        FLo = self.root.ids.Page3
    
        size  = int(self.root.ids.Taille.text)
        self.List3 = [0 for i in range(size)]
        FLo.clear_widgets()
    
        for i in range(size):
            Text = MDTextField(
                halign = "center",
            )
            self.List3[i] = Text
            FLo.add_widget(Text)
    
    def Appui3(self):
        Pge = self.root.ids.cr
        if "" in [elmt.text for elmt in self.List3]:
            self.Pop3 = self.show_info(title="Error",Message="Tous les Champs sont Obligatoires !",fonct = self.Ok3)
        else:
            Pge.current = "Page_4"
            self.Valider4()
    
    def Ok3(self,instance):
        self.Pop3.dismiss()
    
    def veri(self,rep):
        for elmt in rep:
            if isinstance(elmt,str):
                return True
        return False
    
    def Valider4(self):
        #dic = {"Cramer":self.Crame,"LU":self.LU,"Gauss":self.GA}
        #do = dic.get(self.List[self.ind])
        
        List = []
        for elmt in self.List2:
            Lis = []
            for elmt2 in elmt:
                Lis.append(int(elmt2.text))
            List.append(Lis)

        List2 = []
        for elmt in self.List3:
            List2.append(int(elmt.text))
        
        
        if self.List[self.ind] == "Cramer":
            rep = Cr.MAIN(List,List2)
        elif self.List[self.ind] == "Gauss":
            rep = Gu.MAIN(List,List2)
        elif self.List[self.ind] == "LU":
            rep = LU.MAIN(List,List2)
        
        FLo = self.root.ids.Pge4
        FLo.clear_widgets()
        FLo.size_hint = (1,0.5)
        FLo.pos_hint = {"center_y":.5}
        if "Impossible" not in rep[0]:
            for i,elmt in enumerate(rep[0]):
                Lb = MDLabel(
                    text = f"X{i+1}={elmt}",
                    #size_hint = (1,0.01),
                    pos_hint = {"center_x":.9}
                    )
                FLo.add_widget(Lb)
        else:
            Lb = MDLabel(
                    text = "Impossible !",
                    bold = True,
                    size_hint = (1,0.3),
                    pos_hint = {"center_x":.9,"center_y":.5}
                    )
            FLo.add_widget(Lb)
if __name__ == "__main__":
    ZeliApp().run()
