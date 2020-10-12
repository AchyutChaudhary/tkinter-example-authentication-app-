import tkinter as tk
from tkinter import *
from auth import *
from math import pow
window = tk.Tk()
window.attributes('-fullscreen',True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
#window.geometry("%dx%d+100+100" % (w, h))
window.title("Welcome to SAVJ Bank")    
window.configure(background = "LightSeaGreen")

hashDir = {'f5b2cbcdae494fa0bc1185ae5fb31776b701426770ad3346143b101a90ea3cd7':'Yash', #7828
           '58a006a8a514887a9bdb3eaa870e6c30bf5a29a18e309d883953741491f06079':'Aditi', #6774
           '15c599a15a73eacbb47a9f42ac4e219a093b613de02a44c872ce8c394209a947':'Vinay', #8367
           'f711c71f3a1a3692e36b6fb8902fcd32c2ff89a8e76da0bccb77729cd9a29604':'Jagriti'} #5046

hashDirLen = len(hashDir)
hashList = list(hashDir.keys())
#nameList = list(hashDir.values())
def authenticate():
        newWin = Toplevel(window)
        newWin.attributes('-fullscreen',True)
        newWin.title("Authentication")
        newWin.configure(background = "LightSeaGreen")
        Label(
                newWin,
                text = " Welcome to SAVJ Bank ",
                bg = "LightSeaGreen",
                fg = "DarkCyan",
                font = "Consolas 72"
        ).place(
                x = 90,
                y = 50
        )
        P = PINEntry.get()
        PINEntry.delete(0,END)
        if len(P) == 4 and P.isdigit():
                q = 123456789987654321234567898 #random.randint(pow(10,20),pow(10,50))
                g = 23931164504956447807213117212663825326210289577470
                key = gen_key(q) #Receiver_Private_key
                h = power(g,key,q)
                out = encrypt(P,q,h,g)
                #dr_msg = decrypt(en_msg,p,key,q)
                #dmsg = ''.join(dr_msg)
                #print("Decrypted Message: ",dmsg)
                flag = 0
                for i in range(len(hashList)):
                        if out == hashList[i]:
                                flag = 1
                                pos = i
                                break
                if flag == 1:
                        Label(
                                newWin,
                                text = "PIN Matched. Hello, " + hashDir[hashList[pos]] + "!",
                                bg = "LightSeaGreen",
                                fg = "Navy",
                                font = "Consolas 20"
                        ).place(
                                x = 430,
                                y = 300
                        )
                        Button(
                                newWin,
                                text = "Back",
                                width = 20,
                                font = "Calibri 15",
                                bg = "LightSeaGreen",
                                fg = "White",
                                command = newWin.destroy
                        ).place(
                                x = 550,
                                y = 425
                        )
                else:
                        Label(
                                newWin,
                                text = "No match found. Please try again.",
                                bg = "LightSeaGreen",
                                fg = "Maroon",
                                font = "Consolas 20"
                        ).place(
                                x = 430,
                                y = 300
                        )
                        Button(
                                newWin,
                                text = "Back",
                                width = 20,
                                font = "Calibri 15",
                                bg = "LightSeaGreen",
                                fg = "White",
                                command = newWin.destroy
                        ).place(
                                x = 550,
                                y = 425
                        )
        else:
                Label(
                        newWin,
                        text = "Invalid PIN. Please try again.",
                        bg = "LightSeaGreen",
                        fg = "Maroon",
                        font = "Consolas 20"
                ).place(
                        x = 430,
                        y = 300
                )
                Button(
                        newWin,
                        text = "Back",
                        width = 20,
                        font = "Calibri 15",
                        bg = "LightSeaGreen",
                        fg = "White",
                        command = newWin.destroy
                ).place(
                        x = 550,
                        y = 425
                )
Label(
	text = " Welcome to SAVJ Bank ",
	bg = "LightSeaGreen",
	fg = "DarkCyan",
	font = "Consolas 72"
).place(
	x = 90,
	y = 50
)
Label(
	text = "Enter your 4-digit PIN:",
	bg = "LightSeaGreen",
	fg = "White",
	font = "SegoeUILight 20",
).place(
	x = 525,
	y = 250
)
PINEntry = Entry(
	window,
	width = 4,
	font = "Consolas 50",
	show = "*"
)
PINEntry.place(
	x = 582,
	y = 300
)

window.bind('<Return>', authenticate)
PINEntry.focus_set()

Button(
	window,
	text = "Proceed",
	width = 20,
	font = "Calibri 15",
	bg = "LightSeaGreen",
	fg = "White",
	command = authenticate
).place(
	x = 550,
	y = 425
)
Button(
	window,
	text = "Quit",
	width = 20,
	font = "Calibri 15",
	bg = "LightSeaGreen",
	fg = "White",
	command = window.destroy
).place(
	x = 550,
	y = 475
)
window.mainloop()