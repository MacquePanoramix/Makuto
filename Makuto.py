import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from PIL import Image, ImageGrab
import sys
import subprocess
import os
a = 1
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

Essence = client.open("CardsDesign").worksheet("Essences")
Path = client.open("CardsDesign").worksheet("Paths")
Miracle = client.open("CardsDesign").worksheet("Miracles")
data_miracle = Miracle.get_all_records()
data_path = Path.get_all_records()
data_essence = Path.get_all_records()
print(data_miracle[3])

window = Tk()
window.title("Makuto cards")
window.geometry("750x1050")

def resetPath(i):
    for child in window.winfo_children():
        child.destroy()

        # Card name
    cardName = Label(window, text=data_path[i]['Card name'], font=("Century Gothic", 36))
    cardName.place(x=200, y=10)

    # Card type
    cardType = Label(window, text=data_path[i]['Card type'], font=("Century Gothic", 18))
    cardType.place(x=325, y=100)

    # image number
    global imageNumberPath
    imageNumberPath = i+1

    # save image
    window.update()
    # get window location
    x0 = 0
    y0 = 52
    x1 = 938
    y1 = 995
    ImageGrab.grab((x0, y0, x1, y1)).save("C:/Users/didiu/Documents/MakutoImages/" + data_path[i]['Card name'].replace(" ", "_") + ".png")
    # button path
    if imageNumberPath < len(data_path):
        bt = Button(window, text="Next image path", font=("Century Gothic", 12), command=lambda: resetPath(imageNumberPath))
        bt.place(x=0, y=500)


def resetMiracle(i):
    for child in window.winfo_children():
        child.destroy()
        # Card name

    cardName = Label(window, text=data_miracle[i]['Card name'], font=("Century Gothic", 36))
    cardName.place(x=200, y=10)

    # Card type
    cardType = Label(window, text=data_miracle[i]['Card type'], font=("Century Gothic", 18))
    cardType.place(x=325, y=100)

    # Description
    if len(data_miracle[i]['Description']) >=97: #------------------ perform line break if needed -----------------------
        index = (data_miracle[i]['Description'][-(len(data_miracle[i]['Description'])-96)::-1]).index(' ')
        print(data_miracle[i]['Description'][::-1])
        data_miracle[i]['Description'] = data_miracle[i]['Description'][:97-index] + '\n' + data_miracle[i]['Description'][97-index:]
#-----------------------------------------------------------------------------------------------------------------------
    cardType = Label(window, text=data_miracle[i]['Description'], font=("Century Gothic", 12))
    cardType.place(x=0, y=200)

    # image number
    global imageNumberMiracle
    imageNumberMiracle = i+1

    # save image
    window.update()
    # get window location
    x0 = 0
    y0 = 52
    x1 = 938
    y1 = 995
    ImageGrab.grab((x0, y0, x1, y1)).save("C:/Users/didiu/Documents/MakutoImages/" + data_miracle[i]['Card name'].replace(" ", "_") + ".png")
    # button miracle
    if imageNumberMiracle < len(data_miracle):
        bt = Button(window, text="Next image miracle", font=("Century Gothic", 12), command=lambda: resetMiracle(imageNumberMiracle))
        bt.place(x=0, y=500)

    # button path
    else:
        bt = Button(window, text="Next image path", font=("Century Gothic", 12), command=lambda: resetPath(imageNumberPath))
        bt.place(x=0, y=500)




# -------------------------------------------------------miracles-------------------------------------------------------
imageNumberMiracle = 0
imageNumberPath = 0
imageNumberEssence = 0 
bt = Button(window, text="Next image", font=("Century Gothic", 12), command=lambda: resetMiracle(imageNumberMiracle))
bt.place(x=0, y=500)



window.mainloop()
