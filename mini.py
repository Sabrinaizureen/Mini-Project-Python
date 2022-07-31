from msilib.schema import Font
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from turtle import right
from tkcalendar import Calendar
import sqlite3
from PIL import Image, ImageTk

window = Tk()
window['bg']='black'
window.geometry("1350x700")
window.title("Bus Online Booking")

#----------------------WINDOW AND FRAME--------------------------
topframe = Frame (window, width = 1350, height=100, bd=6, relief='raise', bg = 'dark goldenrod')
topframe.pack(side= TOP)

bottomframe = Frame (window,width = 1350, height=600,bd=6, relief='raise', bg = 'black')
bottomframe.pack(side= BOTTOM)

infoframe = Frame(bottomframe,width = 1350, height=250,bd=2, relief='raise', bg = 'dark goldenrod')
infoframe.pack(side= TOP)
ticketframe = Frame(bottomframe,width = 1350, height=200,bd=6, relief='raise', bg = 'dark goldenrod')
ticketframe.pack(side= BOTTOM)
btnframe = Frame(bottomframe,width = 1350, height=70,bd=6, relief='raise', bg = 'dark goldenrod')
btnframe.pack(side= BOTTOM)

leftinfo = Frame (infoframe,width = 450, height=250,bd=6, relief='raise', bg = 'black')
leftinfo.pack(side= LEFT)
rightinfo = Frame (infoframe,width = 300, height=250,bd=6, relief='raise', bg = 'black')
rightinfo.pack(side= RIGHT)
centerinfo = Frame (infoframe,width = 550, height=250,bd=6, relief='raise',bg = 'black')
centerinfo.pack(side= RIGHT)

dspframe = Frame (ticketframe,width = 300, height=200,bd=6, relief='raise', bg = 'dark goldenrod')
dspframe.pack(side= LEFT)
ticketinfo = Frame (ticketframe,width = 1050, height=200,bd=6, relief='raise', bg = 'dark goldenrod')
ticketinfo.pack(side= RIGHT)

#------------------------ALL VARIABLE-------------------------------
namecus = StringVar()
pnumbercus = StringVar()
agecus = StringVar()
datecus = StringVar()
origincus = StringVar()
destinationcus = StringVar()
seatcus = StringVar()
paxcus = StringVar()
totalcus = StringVar()

#------------------------LABEL TITTLE-----------------------------
labeltittle = Label (topframe, font =('System',40,'bold'), text = "BUS ONLINE TICKET", justify='center', width=41,bg = "black", fg = 'dark goldenrod')
labeltittle.grid(row=0,column=0)
labeltittle = Label (topframe, font =('arial',10,'bold'), text = "Welcome to Bus Online Ticket!", justify= 'center',width=169,bg = "black", fg = 'white')
labeltittle.grid(row=1,column=0)

#------------------------INFORMATION------------------------------
infotittle = Label(leftinfo, text = "INFORMATION ", font =('Bahnschrift Light',17,'bold'), bg='black', fg='dark goldenrod')
infotittle.grid(row=0,column=0)
infotittle = Label(leftinfo, text = "(Please fill in the correct details) ", font =('Bahnschrift Light',9,'bold'), justify='right', bg='black', fg='white')
infotittle.grid(row=0,column=2)

infotittle = Label(leftinfo, text = "", font =('Bahnschrift Light',35,'bold'), bg='black', fg='dark goldenrod')
infotittle.grid(row=1,column=0)

name1 = Label (leftinfo, text = "NAME              :", font =('Bahnschrift Light',17,'bold'), bg='black', fg='dark goldenrod')
name1.grid(row=2,column=0)
entryname = Entry (leftinfo, width= 25, font =('Bahnschrift Light',15,'bold'), textvariable=namecus, bd='1', bg='black', fg='white')
entryname.grid (row = 2, column= 2, sticky='w')

phone1 = Label (leftinfo, text = "P. NUMBER     :", font =('Bahnschrift Light',17,'bold'), bg='black', fg='dark goldenrod')
phone1.grid(row=3,column=0)
entrypnum = Entry (leftinfo, width= 25, font =('arial',16,'bold'), textvariable=pnumbercus, bd='1', bg='black', fg='white')
entrypnum.grid (row = 3, column= 2, sticky='w')

age = Label (leftinfo, text = "AGE                 :", font =('Bahnschrift Light',17,'bold'), bg='black', fg='dark goldenrod')
age.grid(row=4,column=0)
entryage = Entry (leftinfo, width= 25, font =('arial',16,'bold'), textvariable=agecus, bd='1', bg='black', fg='white')
entryage.grid (row = 4, column= 2, sticky='w')

infotittle = Label(leftinfo, text = "", font =('Bahnschrift Light',35,'bold'), bg='black', fg='dark goldenrod')
infotittle.grid(row=5,column=0)

#-----------------------------DESTINATION----------------------------------------
infotittle = Label(centerinfo, text ="JOURNEY", font =('Bahnschrift Light',17,'bold'), bg='black', fg='dark goldenrod')
infotittle.grid(row=0,column=0)
infotittle = Label(centerinfo, text ="(Please select the correct details)", font =('Bahnschrift Light',9,'bold'), justify='right', bg='black', fg='white')
infotittle.grid(row=0,column=2)

infotittle = Label(centerinfo, text = "", font =('Bahnschrift Light',5,'bold'), bg='black', fg='dark goldenrod')
infotittle.grid(row=1,column=0)

labeldate1 = Label (centerinfo, text = "  DATE                   :", font =('Bahnschrift Light',17,'bold'), justify='left', bg='black', fg='dark goldenrod')
labeldate1.grid(row=2,column=0)
cbodate = ttk.Combobox (centerinfo, font =('Bahnschrift Light',14,'bold'),width=24, state="readonly", textvariable=datecus)
cbodate ['value']=('','')
cbodate.current(0)
cbodate.grid(row=2, column=2)

labelorigin = Label (centerinfo, text = "  ORIGIN                 :", font =('Bahnschrift Light',17,'bold'), justify='left', bg='black', fg='dark goldenrod')
labelorigin.grid(row=3,column=0)
cboorigin = ttk.Combobox (centerinfo, font =('arial',14,'bold'),width=24, state="readonly", textvariable=origincus)
cboorigin ['value']=('','UNICITI ALAM')
cboorigin.current(0)
cboorigin.grid (row = 3, column= 2, sticky='w')

labeldestination = Label (centerinfo, text = "  DESTINATION       :", font =('Bahnschrift Light',17,'bold'), justify='left',bg='black', fg='dark goldenrod')
labeldestination.grid(row=4,column=0)
cbodestination = ttk.Combobox (centerinfo,width=24, font =('arial',14,'bold'), state="readonly", textvariable = destinationcus)
cbodestination ['value']=('','PAUH','KANGAR','ARAU','KUALA PERLIS','BINTONG','SIMPANG EMPAT', 'TIMAH TASOH')
cbodestination.current(0)
cbodestination.grid (row = 4, column= 2, sticky='w')
cbodestination.bind('<<ComboboxSelected>>', price_command)

labelseat = Label(centerinfo, text = "   SEAT                   :", font =('Bahnschrift Light',17,'bold'), justify='left',bg='black', fg='dark goldenrod')
labelseat.grid(row=5,column=0)
cboseat = ttk.Combobox (centerinfo,width=24, font =('arial',14,'bold'), state="readonly", textvariable = seatcus)
cboseat ['value']=('','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
cboseat.current(0)
cboseat.grid (row = 5, column= 2, sticky='w')

labelpax = Label(centerinfo, text = "   PAX                     :", font =('Bahnschrift Light',17,'bold'), justify='left',bg='black', fg='dark goldenrod')
labelpax.grid(row=6,column=0)
cbopax = ttk.Combobox (centerinfo,width=24, font =('arial',14,'bold'), state="readonly", textvariable=paxcus)
cbopax ['value']=('','1 PAX' )
cbopax.current(0)
cbopax.grid (row = 6, column= 2, sticky='w')

total = Label (centerinfo, text = "  AMOUNT               :", font =('Bahnschrift Light',17,'bold'),bg='black', fg='dark goldenrod')
total.grid(row=7,column=0)
price = Label (centerinfo, font =('arial',16,'bold'), textvariable=totalcus,bg='black', fg='dark goldenrod')
price.grid(row=7,column=2)

infotittle = Label(centerinfo, text = "", font =('Bahnschrift Light',5,'bold'), bg='black', fg='dark goldenrod')
infotittle.grid(row=8,column=0, sticky='w')