from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from googletrans import Translator


class MyBoxLayout(BoxLayout):
    """
    Classe responsável por estruturar a interface gráfica da aplicação.
    """
    def tradutor(self):
        if self.ids.tin1.text:
            tradutor = Translator()
            tpara = self.ids.sp_id2.text
            traduzido = tradutor.translate(self.ids.tin1.text, dest=tpara)
            self.ids.tin2.text = traduzido.text
            print(f"Tradução: {traduzido}")
        else:
            self.ids.tin2.text = self.ids.tin1.text
    
    def btn_on(self):
        self.ids.my_image.source = "img/btn1.png"

    def btn_off(self):
        self.ids.my_image.source = "img/btn2.png"


class MainApp(App):
    """
    Classe responsável por iniciar a aplicação.
    """
    def build(self):
        return MyBoxLayout()

MainApp().run()
