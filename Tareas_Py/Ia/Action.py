from os import strerror
from typing import Text
from speech_recognition import *
import Data as imports
import threading

""" Solo microfono """
def action_Listen():
    try:
        with imports.sr.Microphone() as source:
            imports.app.play()
            imports.sR.adjust_for_ambient_noise(source)
            audio = imports.sR.listen(source)  
        
        action_translateEng(audio)
    except LookupError:
        say_error()

    imports.app.reset()

""" Reconocedor a texto Ingles"""
def action_translateEng(voic:AudioData=None):
    try:
        text = imports.sR.recognize_google(voic, language="en-US",show_all=False)
        voice = imports.tr.translate(text,dest='es')
        if(voice.text != text):
            getSay(voice.text)
        else:
            action_translateEsp(voice.text)
    except UnknownValueError:
        action_translateEsp(voic)

""" Reconocedor a texto Español """
def action_translateTxEsp(tx:str=''):
    try:
        voice = imports.tr.translate(tx,dest='en')
        getSay(voice.text)
    except UnknownValueError:
        say_error()

""" Segundo traductor """
def action_translateEsp(voic:AudioData=None):
    try:
        text = imports.sR.recognize_google(voic, language="es",show_all=False)
        action_translateTxEsp(text)
    except UnknownValueError:
        say_error()

""" Diga un error """
def say_error(error:str = 'Lo siento, no te escuche.'):
    try:
        imports.tx_vc.say(error)
        imports.tx_vc.runAndWait()
    except strerror:
        say_error()

""" Metodo on clic """
def listen():
    try:
        th = threading.Thread(target=action_Listen)
        th.start()
    except threading.ThreadError:
        say_error()

""" Traduccion """
def getSay(tx:str = ''):
    try:
        imports.tx_vc.say(tx)
        print(tx)
        imports.tx_vc.runAndWait()
    except Exception:
        say_error()