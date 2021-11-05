from tkinter.constants import ACTIVE, DISABLED
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
""" Windows, bottons, Labels """
from tkinter import StringVar, Tk, Label, Button, mainloop
from typing import Any
""" Frame for class """
from tkinter import ttk
""" Font for letters """
from tkinter.font import Font 
""" Acciones """
import Action as imports

""" Clase de interfaz """
class MyFrameTranslate(ttk.Frame):
    
    wdw = Tk()
    tx_btn_trans = StringVar()
    
    font_main = Font(family='Segoe UI', size=20)

    def construct(self):
        """ Cambiar dependiendo la voz """
        self.wdw.title('Javian')
        self.wdw.configure(width= 500, height= 400)
        self.wdw['bg'] = '#2596be'
        self.wdw.minsize(500,400)
        self.wdw.maxsize(800,600)
        self.reset()

        self._init_Label()
        self._init_button()

        self.wdw.mainloop()

    """ Label creation """
    def _init_Label(self):
        self.lbTitle = Label(self.wdw, text='Traducir ---><--- Translate',bg='green',font= self.font_main)
        self.lbTitle.place(relwidth=1,relheight=0.17)

    """ Boton creation """
    def _init_button(self):
        """ Boton main """
        self.btnChat = Button(self.wdw, textvariable=self.tx_btn_trans ,width=100, height=70, font= self.font_main,
        command=imports.listen)
        self.btnChat.place(relwidth=0.48, relheight=0.4, relx= 0.1,rely=0.3)

    """ Replace labels """
    def play(self):
        self.name_btn('Listening')
    
    """ Replace labels """
    def reset(self):
        self.name_btn('Start Translate: ')
  
    """ Establecer text en boton """
    def name_btn(self,name:str=''):
        self.tx_btn_trans.set(name)

""" Voz """
tx_vc = pyttsx3.init()
tx_vc.setProperty("voice", tx_vc.getProperty("voices")[2].id)
tx_vc.setProperty('rate', 98)
""" Microfono """
sR = sr.Recognizer()
""" Traductor """
tr = Translator()
""" Windows """
app = MyFrameTranslate()


""" Aqui solo son varibles, clases """