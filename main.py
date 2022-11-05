from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time
r = Tk()
r.title("Time Zone Clock")
r.geometry("600x400")
r.config(bg="white")
indiaImage = ImageTk.PhotoImage(Image.open("india.png"))
usaImage = ImageTk.PhotoImage(Image.open("usa.png"))
parisImage = ImageTk.PhotoImage(Image.open("paris.png"))
dubaiImage = ImageTk.PhotoImage(Image.open("dubai.png"))

'''===============India=========='''
indiaLabel = Label(r,text="India",bg="white")
indiaLabel.place(relx=0.2,rely=0.05,anchor=CENTER)

indiaClock=Label(r)
indiaClock['image'] = indiaImage
indiaClock.place(relx=0.2,rely=0.25,anchor=CENTER)

indiaTime = Label(r,bg="white")
indiaTime.place(relx=0.2,rely=0.45,anchor=CENTER)
'''==============USA=============='''

usaLabel = Label(r,text="USA",bg="white")
usaLabel.place(relx=0.7,rely=0.05,anchor=CENTER)

usaClock=Label(r)
usaClock['image'] = usaImage
usaClock.place(relx=0.7,rely=0.25,anchor=CENTER)

usaTime = Label(r,bg="white")
usaTime.place(relx=0.7,rely=0.45,anchor=CENTER)
'''===============Paris=========='''
parisLabel = Label(r,text="Paris",bg="white")
parisLabel.place(relx=0.2,rely=0.55,anchor=CENTER)

parisClock=Label(r)
parisClock['image'] = parisImage
parisClock.place(relx=0.2,rely=0.75,anchor=CENTER)

parisTime = Label(r,bg="white")
parisTime.place(relx=0.2,rely=0.89,anchor=CENTER)
'''===============Dubai=========='''
dubaiLabel = Label(r,text="Dubai",bg="white")
dubaiLabel.place(relx=0.7,rely=0.65,anchor=CENTER)

dubaiClock=Label(r)
dubaiClock['image'] = dubaiImage
dubaiClock.place(relx=0.7,rely=0.75,anchor=CENTER)

dubaiTime = Label(r,bg="white")
dubaiTime.place(relx=0.7,rely=0.89,anchor=CENTER)

'''Functions'''
class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        indiaTime['text'] = "Time: "+current_time
        indiaTime.after(200,self.times)
class USA():
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usaTime['text'] = "Time: "+current_time
        usaTime.after(200,self.times)
class Paris():
    def times(self):
        home = pytz.timezone("Europe/Paris")
        local_time = datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        parisTime['text'] = "Time: "+current_time
        parisTime.after(200,self.times)
class Dubai():
    def times(self):
        home = pytz.timezone("Asia/Dubai")
        local_time = datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        dubaiTime['text'] = "Time: "+current_time
        dubaiTime.after(200,self.times)
objIndia = India()
objUsa = USA()
objParis = Paris()
objDubai = Dubai()
indiaBtn = Button(r,text="Show Time in",bg="white",,command=objIndia.times)
indiaBtn.place(relx=0.2,rely=0.5,anchor=CENTER)
usaBtn = Button(r,text="Show Time us",bg="white",command=objUsa.times)
usaBtn.place(relx=0.7,rely=0.5,anchor=CENTER)
ParisBtn = Button(r,text="Show Time pa",bg="white",command=objParis.times)
ParisBtn.place(relx=0.2,rely=0.95,anchor=CENTER)
dubaiBtn = Button(r,text="Show Time du",bg="white",command=objDubai.times)
dubaiBtn.place(relx=0.7,rely=0.95,anchor=CENTER)
warningLabel = Label(r,text="Please Go To FullScreen Mode!",fg="red",bg="white")
warningLabel.pack()
r.mainloop()