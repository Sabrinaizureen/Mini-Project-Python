import imghdr
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
combostyle=ttk.Style

#-------------------------------BUTTON FUNCTION------------------------
def clear_command(): 

    entryname.delete(0,END)
    entrypnum.delete(0,END)
    entryage.delete(0,END)
    infoticket2.delete(0,END)
    cbodate.set("")
    cboorigin.set("")
    cbodestination.set("")
    cboseat.set("")
    cbopax.set("")
    totalcus.set("")

#-----------------------------CONNECT DATABASE-------------------------------
con = sqlite3.connect("BusTiketBooking.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS customer(name TEXT,pnumber TEXT,age TEXT,date TEXT,origin TEXT,destination TEXT,seat TEXT,pax TEXT,price TEXT )")
con.commit()
con.close()

#-------------------------------ORDER-------------------------------
def add_command():

    if namecus.get() == '' or pnumbercus.get() == '' or agecus.get() == '' or datecus.get() == '':
        messagebox.showerror('Return','ENTER CORRECT DETAIL')

    else:
        con = sqlite3.connect("BusTiketBooking.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM customer WHERE seat = ?", (seatcus.get(),))
        result = cur.fetchall()

        if len (result) == 1:
            messagebox.showinfo('Seat selection','SEAT ALREADY SELECTED ! PLEASE ENTER ANOTHER SEAT')
        else:
            con = sqlite3.connect("BusTiketBooking.db")
            cur = con.cursor()
            cur.execute("INSERT INTO customer VALUES(?,?,?,?,?,?,?,?,?)",(namecus.get(),pnumbercus.get(),agecus.get(),datecus.get(),origincus.get(),destinationcus.get(),seatcus.get(),paxcus.get(),totalcus.get()))
            con.commit()
            con.close()
            infoticket2.insert(END, "", "=======================================",  "PASSENGER'S NAME : " + namecus.get(),"PHONE NUMBER : " + pnumbercus.get(),"AGE : " + agecus.get(),"DATE : " + datecus.get(),"ORIGIN : " + origincus.get(),"DESTINATION : " + destinationcus.get(),"SEAT NUMBER : " + seatcus.get(),"PAX : " + paxcus.get(),"PRICE : " + totalcus.get(), "=======================================")
            #display_command()
            messagebox.showinfo('Order','RECORD ENTERED SUCCESSFULLY')

#-------------------------------SEE ALL-------------------------------
def display_command():
    con = sqlite3.connect("BusTiketBooking.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM customer")
    result = cur.fetchall()
    if len (result) != 0:
        ticket_record.delete(*ticket_record.get_children())
        for row in result:
            ticket_record.insert('',END,values=row)
    display_command()
    con.commit()
    con.close()

#-------------------------------SEAT SELECTION-------------------------------
def TraineeInfo(ev):
    viewinfor = ticket_record.focus()
    learnerdata = ticket_record.item(viewinfor)
    row = learnerdata ['values'] 
    namecus.set(row[0])
    pnumbercus.set(row[1])
    agecus.set(row[2])
    datecus.set(row[3])
    origincus.set(row[4])
    destinationcus.set(row[5])
    seatcus.set(row[6])
    paxcus.set(row[7])
    totalcus.set(row[8])

#-------------------------------UPDATE------------------------------
def update_command():
    con = sqlite3.connect("BusTiketBooking.db")
    cur = con.cursor()
    cur.execute("UPDATE customer SET name=?,pnumber=?,age=?,date=?,origin=?,destination=?,pax=?,price=? WHERE seat=?",(namecus.get(),pnumbercus.get(),agecus.get(),datecus.get(),origincus.get(),destinationcus.get(),paxcus.get(),totalcus.get(),seatcus.get()))
    con.commit()
    con.close()
    display_command()
    messagebox.showinfo('Update','RECORD UPDATED SUCCESSFULLY')

#-------------------------------DROP-------------------------------
def drop_command():
    con = sqlite3.connect("BusTiketBooking.db")
    cur = con.cursor()
    cur.execute("DELETE FROM customer WHERE seat=?",(seatcus.get(),))
    for item in ticket_record.get_children():
            ticket_record.delete(item)
    con.commit()
    con.close()
    display_command()
    messagebox.showinfo('Drop','PASSENGER DROP')

#-------------------------------DELETE ALL DATABASE-------------------------------
def delete_display():
    msgBox=messagebox.askquestion('Delete','ARE YOU SURE TO DELETE PERMANENTLY?',icon='warning')

    if msgBox=='yes':
        con = sqlite3.connect("BusTiketBooking.db")
        cur = con.cursor()
        cur.execute("DELETE FROM customer")
        for item in ticket_record.get_children():
            ticket_record.delete(item)
        con.commit()
        con.close()

def price_command(ev):

    if destinationcus.get() == 'ARAU':
        totalcus.set('RM 8.00')
    
    elif destinationcus.get() == 'PAUH':
        totalcus.set('RM 8.00')
    
    elif destinationcus.get() == 'KANGAR':
        totalcus.set('RM 15.00')
    
    elif destinationcus.get() == 'BINTONG':
        totalcus.set('RM 10.00')
    
    elif destinationcus.get() == 'SIMPANG EMPAT':
        totalcus.set('RM 12.00')
    
    elif destinationcus.get() == 'TIMAH TASOH':
        totalcus.set('RM 4.00')
    
    else :
        totalcus.set('RM 18.00')

#-------------------------------CALENDAR-------------------------------
def grad_date():
    #date.config(text = cal.get_date())
    cbodate['value']= cal.get_date()
    
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
labeltittle = Label (topframe, font =('arial',10,'bold'), text = "Welcome to Bus Online Ticket !", justify= 'center',width=169,bg = "black", fg = 'white')
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

labeldate1 = Label (centerinfo, text = "DATE                    :", font =('Bahnschrift Light',17,'bold'), justify='left', bg='black', fg='dark goldenrod')
labeldate1.grid(row=2,column=0)
cbodate = ttk.Combobox (centerinfo, font =('Bahnschrift Light',14,'bold'),width=24, state="readonly", textvariable=datecus)
cbodate ['value']=('','')
cbodate.current(0)
cbodate.grid(row=2, column=2)

labelorigin = Label (centerinfo, text = "ORIGIN                 :", font =('Bahnschrift Light',17,'bold'), justify='left', bg='black', fg='dark goldenrod')
labelorigin.grid(row=3,column=0)
cboorigin = ttk.Combobox (centerinfo, font =('arial',14,'bold'),width=24, state="readonly", textvariable=origincus)
cboorigin ['value']=('','UNICITI ALAM')
cboorigin.current(0)
cboorigin.grid (row = 3, column= 2, sticky='w')

labeldestination = Label (centerinfo, text = "DESTINATION       :", font =('Bahnschrift Light',17,'bold'), justify='left',bg='black', fg='dark goldenrod')
labeldestination.grid(row=4,column=0)
cbodestination = ttk.Combobox (centerinfo,width=24, font =('arial',14,'bold'), state="readonly", textvariable = destinationcus)
cbodestination ['value']=('','PAUH','KANGAR','ARAU','KUALA PERLIS','BINTONG','SIMPANG EMPAT', 'TIMAH TASOH')
cbodestination.current(0)
cbodestination.grid (row = 4, column= 2, sticky='w')
cbodestination.bind('<<ComboboxSelected>>', price_command)

labelseat = Label(centerinfo, text = "SEAT                    :", font =('Bahnschrift Light',17,'bold'), justify='left',bg='black', fg='dark goldenrod')
labelseat.grid(row=5,column=0)
cboseat = ttk.Combobox (centerinfo,width=24, font =('arial',14,'bold'), state="readonly", textvariable = seatcus)
cboseat ['value']=('','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
cboseat.current(0)
cboseat.grid (row = 5, column= 2, sticky='w')

labelpax = Label(centerinfo, text = "PAX                      :", font =('Bahnschrift Light',17,'bold'), justify='left',bg='black', fg='dark goldenrod')
labelpax.grid(row=6,column=0)
cbopax = ttk.Combobox (centerinfo,width=24, font =('arial',14,'bold'), state="readonly", textvariable=paxcus)
cbopax ['value']=('','1 PAX' )
cbopax.current(0)
cbopax.grid (row = 6, column= 2, sticky='w')

total = Label (centerinfo, text = "AMOUNT               :", font =('Bahnschrift Light',17,'bold'),bg='black', fg='dark goldenrod')
total.grid(row=7,column=0)
price = Label (centerinfo, font =('arial',16,'bold'), textvariable=totalcus,bg='black', fg='white')
price.grid(row=7,column=2)

infotittle = Label(centerinfo, text = "", font =('Bahnschrift Light',5,'bold'), bg='black', fg='dark goldenrod')
infotittle.grid(row=8,column=0, sticky='w')

#------------------------CALENDER--------------------------------------
cal = Calendar(rightinfo, selectmode = 'day',year = 2022, month = 8,day = 1)
cal.grid(padx = 34,pady =40)

#---------------------------LIST OF BUTTON--------------------------------
clrbtn = Button (btnframe, text = "CLEAR",font =('arial',17,'bold'), width=13, command=clear_command, bg='gold', fg='black')
clrbtn.grid(row=0, column=0)

addbtn = Button (btnframe, text = "ORDER",font =('arial',17,'bold'),width=13, command = add_command, bg='gold', fg='black')
addbtn.grid(row=0, column=1)

dropbtn = Button (btnframe, text = "DROP",font =('arial',17,'bold'),width=13, command=drop_command, bg='gold', fg='black')
dropbtn.grid(row=0, column=2)

updatebtn = Button (btnframe, text = "UPDATE",font =('arial',17,'bold'),width=13, command=update_command, bg='gold', fg='black')
updatebtn.grid(row=0, column=3)

allbtn = Button (btnframe, text = "SEE ALL",font =('arial',17,'bold'),width= 13, command = display_command, bg='gold', fg='black')
allbtn.grid(row=0, column=4)

dltbtn = Button (btnframe, text = "DELETE",font =('arial',17,'bold'),width=13, command = delete_display, bg='gold', fg='black')
dltbtn.grid(row=0, column=5)

datebtn = Button(btnframe, text = "GET DATE",command = grad_date, font =('arial',17,'bold'),width=13, bg='gold', fg='black')
datebtn.grid(row=0, column=6)

#-----------------------------LIST BOX-------------------------
labelinfoticket2= Label (dspframe, text = "TICKET", width='26', font =('Ebrima',17,'bold'),bg='black', fg='dark goldenrod')
labelinfoticket2.grid(row=3,column=0)
infoticket2=Listbox (dspframe,width=60, height=12, bg='black', fg='white', justify='center') 
infoticket2.grid(row=4, column=0)

#----------------------------TABLE TREEVIEW---------------------
scroll_y= Scrollbar (ticketinfo, orient = VERTICAL, background='black')
scroll_y.pack(side=RIGHT, fill=Y)
style=ttk.Style()

style.configure('Treeview', background='black', foreground='white')
ticket_record = ttk.Treeview(ticketinfo,height=10,columns=("NAME","P.NUMBER","AGE","DATE","ORIGIN","DESTINATION","SEAT","PAX","PRICE"), yscrollcommand=scroll_y.set)

style.theme_use('alt')
style.configure('Treeview', background='black', foreground='white', fieldbackground='black')
style.map('Treeview', background=[('selected', 'dark goldenrod')])
ticket_record = ttk.Treeview(ticketinfo, height=10,columns=("NAME","PHONE NUMBER","AGE","DATE","ORIGIN","DESTINATION","SEAT","PAX","PRICE"), yscrollcommand=scroll_y.set)


ticket_record.heading ("NAME", text ="NAME")
ticket_record.heading ("PHONE NUMBER", text ="PHONE NUMBER")
ticket_record.heading ("AGE", text ="AGE")
ticket_record.heading ("DATE", text ="DATE")
ticket_record.heading ("ORIGIN", text ="ORIGIN")
ticket_record.heading ("DESTINATION", text ="DESTINATION")
ticket_record.heading ("SEAT", text ="SEAT")
ticket_record.heading ("PAX", text ="PAX")
ticket_record.heading ("PRICE", text ="PRICE")

ticket_record['show']='headings'

ticket_record.column ("NAME", width=125)
ticket_record.column ("PHONE NUMBER", width=125)
ticket_record.column ("AGE", width=50)
ticket_record.column ("DATE", width=115)
ticket_record.column ("ORIGIN", width=125)
ticket_record.column ("DESTINATION", width=125)
ticket_record.column ("SEAT", width=50)
ticket_record.column ("PAX", width=90)
ticket_record.column ("PRICE", width=125)

ticket_record.pack(fill=BOTH, expand=1)
ticket_record.bind("<ButtonRelease-1>",TraineeInfo)
#display_command()

window.mainloop()