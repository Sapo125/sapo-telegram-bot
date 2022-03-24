from cgitb import text
from threading import TIMEOUT_MAX
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import cv2
import PySimpleGUI as sg
token = "5104536132:AAH8vIQzth43uTkv3tBSW2-OeiGAoaBIsUY"

bot = telegram.Bot(token)

print (bot.get_me())

chat_ids = set()

chatActive = "-1001298875748"



sg.theme('DarkAmber')
#file_types=estensioni
estensioni = [("JPEG (*.jpg)", "*.jpg"),
              ("PNG (*.png)", "*.png"),
              ("All files (*.*)", "*.*")]

layout = [  [sg.Text('Inserisci un messaggio')],
            [sg.Multiline(no_scrollbar=True, size=(50,6), key="testo")],
            [sg.Button('invia testo'), sg.FileBrowse('invia foto',file_types=estensioni,key="image")] ]

def start(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("Attivato")
    print("start called from chat with id = {}".format(chat_id))
    chat_ids.add(chat_id)

def end(update, context):
    chat_id = update.effective_chat.id
    chat_ids.remove(chat_id)

def message(msg):
    try:
        bot.send_message(chat_id=chatActive, text=msg)
    except:
        sg.Popup("errore nell'invio")
        
#def img(msg):
    
    

def main():
    
    #LETTORE COMANDI
    #updater = Updater(token)
    #updater.dispatcher.add_handler(CommandHandler("start", start))
    #updater.dispatcher.add_handler(CommandHandler("msg", message))
    #updater.start_polling()
    #updater.idle()

    window = sg.Window('TEST', layout)
    while True:
        event, values = window.read(100)
        if event == sg.WIN_CLOSED:
            break
        elif event == "invia testo":
            message(values["testo"])
        elif event == "invia foto":
            img(values["image"])
        
        
    window.close()

main()


