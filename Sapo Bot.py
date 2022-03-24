from cgitb import text
from threading import TIMEOUT_MAX
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import cv2
import PySimpleGUI as sg
#tengo il token, tanto cancellerò il bot
token = "5104536132:AAH8vIQzth43uTkv3tBSW2-OeiGAoaBIsUY"

#dichiarazione bot
bot = telegram.Bot(token)

#stampa info
print (bot.get_me())

#id della chat in cui deve agire (modificare in base alla chat da utilizzare)
chatActive = "-1001298875748"

#elenco estensioni supportate per l'invio immagini
estensioni = [("JPEG (*.jpg)", "*.jpg"),
              ("PNG (*.png)", "*.png"),
              ("All files (*.*)", "*.*")]
#layout GUI           
sg.theme('DarkTeal7')
layout = [  [sg.Text('Inserisci un messaggio, un immagine o entrambi')],
            [sg.Multiline(no_scrollbar=True, size=(10,8), key="testo", expand_x=True, expand_y=True)],
            [sg.Button('Invia messaggio'), sg.FileBrowse("Aggiungi foto",file_types=estensioni, key = "img", target="path"), sg.Button("Rimuovi foto")],
            [sg.Text('',key = "check"), sg.Input('', key="path", visible=False)] ]

#funzione per inviare il messaggio
def message(txt,img):
    if img == "":
        try:
            bot.send_message(chat_id=chatActive, text=txt)
        except:
            sg.Popup("errore nell'invio del testo, controlla e riprova\n(il messaggio potrebbe essere vuoto)")
    else:
        try:
            #lettura immagine in byte
            imgbyte = open(img, 'rb')
            bot.send_photo(chat_id=chatActive, photo=imgbyte, caption=txt)
        except:
            sg.Popup("errore nell'invio del messaggio, controlla e riprova")
        
#main
def main():
    window = sg.Window('TelePonti', layout, resizable=True, element_justification='center')

    while True:
        event, values = window.read(100)
        #visualizzazione percorso foto (se presente)
        if values["path"] != '':
            window["check"].update("Foto inserita: \n{}".format(values["path"]))
        else:
            window["check"].update("")

        #selezione funzione
        if event == sg.WIN_CLOSED:
            break
        elif event == "Invia messaggio":
            message(values["testo"],values["path"])
        elif event == "Rimuovi foto":
            window["path"].update("")

    window.close()

main()        
    
    #LETTORE COMANDI E ESEMPIO DI COMANDI (li tengo che non si sa mai)
    #updater = Updater(token)
    #updater.dispatcher.add_handler(CommandHandler("start", start))
    #updater.dispatcher.add_handler(CommandHandler("msg", message))
    #updater.start_polling()
    #updater.idle()
    
    #def start(update, context):
    #    chat_id = update.effective_chat.id
    #    update.message.reply_text("Attivato")