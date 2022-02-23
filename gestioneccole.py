from tkinter import  *
import sqlite3
import tkinter.ttk as ttk
from tkinter import  ttk, Tk, StringVar
import time;
from  PIL import *


AttendanceReg = Tk()
AttendanceReg.geometry('1300x720')
AttendanceReg.resizable(0, 0)
AttendanceReg.title('Gestion des abscenses')
AttendanceReg.config(bg='white')

AHframe = Frame(AttendanceReg, height=40, width=1280, bg='sky blue').place(relx=0, y=0)
AHHeading = Label(AttendanceReg, text='Gestion des abscenses', font=('impact', 18), bg='sky blue', fg='white').place(relx=0.4, rely=0)

LeftMayFrame = Frame(AttendanceReg, width=1002, height=650, bd=2, relief="raise", bg='white')
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(AttendanceReg, width=350, height=650, bd=2, relief="raise", bg='white')
RightMayFrame.pack(side=RIGHT)

LeftMayFrame1 = Frame(LeftMayFrame, width=1000, height=100, bd=2, relief="raise", bg='white')
LeftMayFrame1.place(y=0.70)
LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=546, bd=2, relief="raise", bg='white')
LeftMayFrame2.place(y=101)

RightMayFrame1 = Frame(RightMayFrame, width=350, height=350,bd=2, relief="raise", bg='white')
RightMayFrame1.place(y=0.100)
RightMayFrame2 = Frame(RightMayFrame, width=350, height=350, bd=2, relief="raise", bg='white')
RightMayFrame2.place(y=300)
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ VARIABLES @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

DateofOrder = StringVar()

value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()
value13 = StringVar()
value14 = StringVar()
value15 = StringVar()
value16 = StringVar()
value17 = StringVar()
value18 = StringVar()
value19 = StringVar()
value20 = StringVar()
value21 = StringVar()
value22 = StringVar()
value23 = StringVar()
value24 = StringVar()
value25 = StringVar()
value26 = StringVar()
value27 = StringVar()
value28 = StringVar()
value29 = StringVar()


def ResetButton():
    image0 = PhotoImage(file="")
    image = cont.create_image(100, 150, image=image0)
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")
    value13.set("")
    value14.set("")
    value15.set("")
    value15.set("")
    value17.set("")
    value18.set("")
    value19.set("")
    value20.set("")
    value21.set("")
    value22.set("")
    value23.set("")
    value24.set("")
    value25.set("")
    value26.set("")
    value27.set("")
    value28.set("")
    value29.set("")
    

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ IMAGES @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


cont = Canvas(RightMayFrame1, width = 450, height = 550, bg='white')
cont.place(relx=0.1, y=0)
name = ''
stname_L = Label(RightMayFrame2).place(relx=0.5 , rely=0.5)
image0 = PhotoImage(file = "stdeomo.png")
image =  cont.create_image(100, 150, image = image0)

image1 = PhotoImage(file = "")
def pic1():
    image = cont.create_image(100,150,image = image1)
    lstName = Label(RightMayFrame2, text=VStNam1, font=('arial black', 20, 'bold'), bg ='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress1, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact1, font=('arial', 12, 'bold'), bg='white').place(x=100, rely=0.25)


image2 = PhotoImage(file = "")
def pic2 ():
    image = cont.create_image(100, 150, image = image2)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam2, font=('arial black', 20, 'bold'), bg ='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress2, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact2, font=('arial', 12, 'bold'), bg='white').place(x=100, rely=0.25)


image3 = PhotoImage(file = "")
def pic3():
    image = cont.create_image(100, 150, image=image3)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam3, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress3, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact3, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image4 = PhotoImage(file = "")
def pic4():
    image = cont.create_image(100, 150, image=image4)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam4, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress4, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact4, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image5 = PhotoImage(file = "")
def pic5():
    image = cont.create_image(100, 150, image=image5)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam5, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress5, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact5, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image6 = PhotoImage(file = "")
def pic6():
    image = cont.create_image(100, 150, image=image6)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam6, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress6, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact6, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

    image7 = PhotoImage(file = "")
def pic7():
    image = cont.create_image(100, 150, image=image7)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam7, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress7, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact7, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image8 = PhotoImage(file = "")
def pic8():
    image = cont.create_image(100, 150, image=image8)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam8, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress8, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact8, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image9 = PhotoImage(file = "")
def pic9():
    image = cont.create_image(100, 150, image=image9)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam9, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress9, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact9, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image10 = PhotoImage(file = "")
def pic10():
    image = cont.create_image(100, 150, image=image10)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam10, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress10, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact10, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image11 = PhotoImage(file = "")
def pic11():
    image = cont.create_image(100, 150, image=image11)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam11, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress11, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact11, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image12 = PhotoImage(file = "")
def pic12():
    image = cont.create_image(100, 150, image=image12)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam12, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress12, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact12, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image13 = PhotoImage(file = "")
def pic13():
    image = cont.create_image(100, 150, image=image13)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam13, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress13, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact13, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image14 = PhotoImage(file = "")
def pic14():
    image = cont.create_image(100, 150, image=image14)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam14, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress14, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact14, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image15 = PhotoImage(file = "")
def pic15():
    image = cont.create_image(100, 150, image=image15)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam15, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress15, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact15, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image16 = PhotoImage(file = "")
def pic16():
    image = cont.create_image(100, 150, image=image16)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam16, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress16, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact17, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image17 = PhotoImage(file = "")
def pic17():
    image = cont.create_image(100, 150, image=image18)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam18, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress18, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact18, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image18 = PhotoImage(file = "")
def pic18():
    image = cont.create_image(90, 100, image=image19)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam19, font=('arial black', 18, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress19, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact19, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image19 = PhotoImage(file = "")
def pic19():
    image = cont.create_image(100, 150, image=image19)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam19, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress19, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact19, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image20 = PhotoImage(file = "")
def pic20():
    image = cont.create_image(100, 150, image=image20)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam20, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress20, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact20, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image21 = PhotoImage(file = "")
def pic21():
    image = cont.create_image(100, 150, image=image21)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam21, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress21, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact21, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image22 = PhotoImage(file = "")
def pic22():
    image = cont.create_image(100, 150, image=image22)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam22, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress22, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact22, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image23 = PhotoImage(file = "")
def pic23():
    image = cont.create_image(100, 150, image=image23)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam23, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress23, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact23, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image24 = PhotoImage(file = "")
def pic24():
    image = cont.create_image(100, 150, image=image24)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam24, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress24, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact24, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image25 = PhotoImage(file = "")
def pic25():
    image = cont.create_image(100, 150, image=image25)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam25, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress25, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact25, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image26 = PhotoImage(file = "")
def pic26():
    image = cont.create_image(100, 150, image=image26)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam26, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress26, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact26, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image27 = PhotoImage(file = "")
def pic27():
    image = cont.create_image(100, 150, image=image27)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam27, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress27, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact27, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image28 = PhotoImage(file = "")
def pic28():
    image = cont.create_image(100, 150, image=image28)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam28, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress28, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact28, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

image29 = PhotoImage(file = "")
def pic29():
    image = cont.create_image(100, 150, image=image29)
    lstName = Label(RightMayFrame2, text="").place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text="").place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text="").place(x=100, rely=0.25)

    lstName = Label(RightMayFrame2, text=VStNam29, font=('arial black', 20, 'bold'), bg='white').place(x=80, y=0.5)
    lstName = Label(RightMayFrame2, text=VStAddress29, font=('arial', 15, 'bold'), bg='white').place(x=80, rely=0.16)
    lstName = Label(RightMayFrame2, text=VstContact29, font=('arial', 12, 'bold'), bg='white').place(x=105, rely=0.25)

            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ FUNCTIONS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ExitButton():
    AttendanceReg.destroy()

def FillButton():
    if value0.get() == "Present":
        value1.set("Present")
        value2.set("Present")
        value3.set("Present")
        value4.set("Present")
        value5.set("Present")
        value6.set("Present")
        value7.set("Present")
        value8.set("Present")
        value9.set("Present")
        value10.set("Present")
        value11.set("Present")
        value12.set("Present")
        value13.set("Present")
        value14.set("Present")
        value15.set("Present")
        value16.set("Present")
        value17.set("Present")
        value18.set("Present")
        value19.set("Present")
        value20.set("Present")
        value21.set("Present")
        value22.set("Present")
        value23.set("Present")
        value24.set("Present")
        value25.set("Present")
        value26.set("Present")
        value27.set("Present")
        value28.set("Present")
        value29.set("Present")
        

    elif value0.get() == "Absent":
        value1.set("Absent")
        value2.set("Absent")
        value3.set("Absent")
        value4.set("Absent")
        value5.set("Absent")
        value6.set("Absent")
        value7.set("Absent")
        value8.set("Absent")
        value9.set("Absent")
        value10.set("Absent")
        value11.set("Absent")
        value12.set("Absent")
        value13.set("Absent")
        value14.set("Absent")
        value15.set("Absent")
        value16.set("Absent")
        value17.set("Absent")
        value18.set("Absent")
        value19.set("Absent")
        value20.set("Absent")
        value21.set("Absent")
        value22.set("Absent")
        value23.set("Absent")
        value24.set("Absent")
        value25.set("Absent")
        value26.set("Absent")
        value27.set("Absent")
        value28.set("Absent")
        value29.set("Absent")

    elif value0.get() == "Rentré":
        value1.set("Rentré")
        value2.set("Rentré")
        value3.set("Rentré")
        value4.set("Rentré")
        value5.set("Rentré")
        value6.set("Rentré")
        value7.set("Rentré")
        value8.set("Rentré")
        value9.set("Rentré")
        value10.set("Rentré")
        value11.set("Rentré")
        value12.set("Rentré")
        value13.set("Rentré")
        value14.set("Rentré")
        value15.set("Rentré")
        value16.set("Rentré")
        value17.set("Rentré")
        value18.set("Rentré")
        value19.set("Rentré")
        value20.set("Rentré")
        value21.set("Rentré")
        value22.set("Rentré")
        value23.set("Rentré")
        value24.set("Rentré")
        value25.set("Rentré")
        value26.set("Rentré")
        value27.set("Rentré")
        value28.set("Rentré")
        value29.set("Rentré")



    elif value0.get() == "En retard":
        value1.set("En retard")
        value2.set("En retard")
        value3.set("En retard")
        value4.set("En retard")
        value5.set("En retard")
        value6.set("En retard")
        value7.set("En retard")
        value8.set("En retard")
        value9.set("En retard")
        value10.set("En retard")
        value11.set("En retard")
        value12.set("En retard")
        value13.set("En retard")
        value14.set("En retard")
        value15.set("En retard")
        value16.set("En retard")
        value17.set("En retard")
        value18.set("En retard")
        value19.set("En retard")
        value20.set("En retard")
        value21.set("En retard")
        value22.set("En retard")
        value23.set("En retard")
        value24.set("En retard")
        value25.set("En retard")
        value26.set("En retard")
        value27.set("En retard")
        value28.set("En retard")
        value29.set("En retard")

    elif value0.get() == "Malade":
        value1.set("Malade")
        value2.set("Malade")
        value3.set("Malade")
        value4.set("Malade")
        value5.set("Malade")
        value6.set("Malade")
        value7.set("Malade")
        value8.set("Malade")
        value9.set("Malade")
        value10.set("Malade")
        value11.set("Malade")
        value12.set("Malade")
        value13.set("Malade")
        value14.set("Malade")
        value15.set("Malade")
        value16.set("Malade")
        value17.set("Malade")
        value18.set("Malade")
        value19.set("Malade")
        value20.set("Malade")
        value21.set("Malade")
        value22.set("Malade")
        value23.set("Malade")
        value24.set("Malade")
        value25.set("Malade")
        value26.set("Malade")
        value27.set("Malade")
        value28.set("Malade")
        value29.set("Malade")
   
   
   
   
   

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ VARIABLES END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

DateofOrder.set(time.strftime("%d/%m/%y"))

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ COMPONENTS END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LeftMayFrame 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

lblNo = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="No", bg='white').place(x=50, rely=0.3)
lblStudentNo = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Student No.", bg='white').place(x=120, rely=0.3)
lblStudentName = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Student Name", bg='white').place(x=240,rely=0.3)
lblCourseCode = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Course Code", bg='white').place(x=400, rely=0.3)
box = ttk.Combobox(LeftMayFrame1, textvariable=value0, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, rely=0.3)
btnFill = ttk.Button(LeftMayFrame1, text='Fill', command = FillButton).place(x=720, rely=0.27)
btnReset = ttk.Button(LeftMayFrame1, text='Reset', command = ResetButton).place(x=815, rely=0.27)
lblDateofOrder = Label(LeftMayFrame1, font=('arial', 10, 'bold'), textvariable=DateofOrder, padx=2, pady=2, bd=2,fg='black', bg='white', relief='sunken').place(x=900, rely=0.3)

VStNam1 = 'M. ADAMA MBENGUE'
VStAddress1 = 'DAKAR KEUR MASSAR'
VstContact1 = '777464277'
SNo1 = Label(LeftMayFrame2, text='1', font =('arial', 10, 'bold'), bg='white').place(x=53, y=10)
StID1 = Label(LeftMayFrame2, text='4115', font =('arial', 10, 'bold'), bg='white').place(x=122, y=10)
StName1 = Label(LeftMayFrame2, text='M. ADAMA MBENGUE', font=('arial', 10, 'bold'), bg='white').place(x=240, y=10)
CourseCode1 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=10)
box = ttk.Combobox(LeftMayFrame2, textvariable=value1, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=10)
StDetails1 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic1).place(x=720, y=10)

VStNam2 = 'M. Saliou Faye'
VStAddress2 = 'DAKAR pikine'
VstContact2 = '777464377'
SNo2 = Label(LeftMayFrame2, text='2', font=('arial', 10, 'bold'), bg='white').place(x=53, y=48)
StID2 = Label(LeftMayFrame2, text='4116', font=('arial', 10, 'bold'), bg='white').place(x=122, y=48)
StName2 = Label(LeftMayFrame2, text='M. Saliou Faye', font=('arial', 10, 'bold'), bg='white').place(x=240, y=48)
CourseCode2 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=48)
box = ttk.Combobox(LeftMayFrame2, textvariable=value2, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=48)
StDetails2 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic2).place(x=720, y=48)

VStNam3 = 'M. Abdoulaye Ndiaye'
VStAddress3 = 'DAKAR Thiaroye'
VstContact3 = '774100946'
SNo3 = Label(LeftMayFrame2, text='3', font=('arial', 10, 'bold'), bg='white').place(x=53, y=86)
StID3 = Label(LeftMayFrame2, text='4117', font=('arial', 10, 'bold'), bg='white').place(x=122, y=86)
StName3 = Label(LeftMayFrame2, text='M. Abdoulaye Ndiaye', font=('arial', 10, 'bold'), bg='white').place(x=240, y=86)
CourseCode3 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=86)
box = ttk.Combobox(LeftMayFrame2, textvariable=value3, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=86)
StDetails3 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic3).place(x=720, y=86)

VStNam4 = 'M. Massart Ndiaye'
VStAddress4 = 'DAKAR Thiaroye'
VstContact4 = '766764500'
SNo4 = Label(LeftMayFrame2, text='4', font=('arial', 10, 'bold'), bg='white').place(x=53, y=124)
StID4 = Label(LeftMayFrame2, text='4118', font=('arial', 10, 'bold'), bg='white').place(x=122, y=124)
StName4 = Label(LeftMayFrame2, text='M. Massar Ndiaye', font=('arial', 10, 'bold'), bg='white').place(x=240, y=124)
CourseCode4 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=124)
box = ttk.Combobox(LeftMayFrame2, textvariable=value4, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=124)
StDetails4 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic4).place(x=720, y=124)

VStNam5 = 'Mme.Ndéye Fatou Faty Aidara'
VStAddress5 = 'DAKAR Keur Massar'
VstContact5 = '774132961'
SNo5 = Label(LeftMayFrame2, text='5', font=('arial', 10, 'bold'), bg='white').place(x=53, y=162)
StID5 = Label(LeftMayFrame2, text='4119', font=('arial', 10, 'bold'), bg='white').place(x=122, y=162)
StName5 = Label(LeftMayFrame2, text='Mme.Ndéye Fatou  Aidara', font=('arial', 10, 'bold'), bg='white').place(x=240, y=162)
CourseCode5 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=162)
box = ttk.Combobox(LeftMayFrame2, textvariable=value5, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=162)
StDetails5 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic5).place(x=720, y=162)

VStNam6 = 'M. Thiérno Bocar Ba'
VStAddress6 = 'DAKAR Diamniadio'
VstContact6 = '778601993'
SNo6 = Label(LeftMayFrame2, text='6', font=('arial', 10, 'bold'), bg='white').place(x=53, y=200)
StID6 = Label(LeftMayFrame2, text='4120', font=('arial', 10, 'bold'), bg='white').place(x=122, y=200)
StName6 = Label(LeftMayFrame2, text='M. Thiérno Bocar Ba', font=('arial', 10, 'bold'), bg='white').place(x=240, y=200)
CourseCode6 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=200)
box = ttk.Combobox(LeftMayFrame2, textvariable=value6, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=200)
StDetails6 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic6).place(x=720, y=200)

VStNam7 = 'Mme. Khady Ciss'
VStAddress7 = 'DAKAR Diamniadio'
VstContact7 = '781668691'
SNo7 = Label(LeftMayFrame2, text='7', font=('arial', 10, 'bold'), bg='white').place(x=53, y=238)
StID7 = Label(LeftMayFrame2, text='4121', font=('arial', 10, 'bold'), bg='white').place(x=122, y=238)
StName7 = Label(LeftMayFrame2, text='Mme. Mme. Khady Ciss', font=('arial', 10, 'bold'), bg='white').place(x=240, y=238)
CourseCode7 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=238)
box = ttk.Combobox(LeftMayFrame2, textvariable=value7, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=238)
StDetails7 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic7).place(x=720, y=238)

VStNam8 = 'M. Assane Diop'
VStAddress8 = 'DAKAR Diamniadio'
VstContact8 = '777904487'
SNo8 = Label(LeftMayFrame2, text='8', font=('arial', 10, 'bold'), bg='white').place(x=53, y=276)
StID8 = Label(LeftMayFrame2, text='4122', font=('arial', 10, 'bold'), bg='white').place(x=122, y=276)
StName8 = Label(LeftMayFrame2, text='M. Assane Diop', font=('arial', 10, 'bold'), bg='white').place(x=240, y=276)
CourseCode8 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=276)
box = ttk.Combobox(LeftMayFrame2, textvariable=value8, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=276)
StDetails8 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic8).place(x=720, y=276)

VStNam9 = 'Mme.Fatou Diome  '
VStAddress9 = 'DAKAR Rufisque'
VstContact9 = '771683955'
SNo9 = Label(LeftMayFrame2, text='9', font=('arial', 10, 'bold'), bg='white').place(x=53, y=314)
StID9 = Label(LeftMayFrame2, text='4123', font=('arial', 10, 'bold'), bg='white').place(x=122, y=314)
StName9 = Label(LeftMayFrame2, text='M. Assane Diop', font=('arial', 10, 'bold'), bg='white').place(x=240, y=314)
CourseCode9 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=314)
box = ttk.Combobox(LeftMayFrame2, textvariable=value9, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=314)
StDetails9 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic9).place(x=720, y=314)

VStNam10 = 'M. Younousse Niassy '
VStAddress10 = 'DAKAR Tiaroye'
VstContact10 = '772644140'
SNo10 = Label(LeftMayFrame2, text='10', font=('arial', 10, 'bold'), bg='white').place(x=53, y=352)
StID10 = Label(LeftMayFrame2, text='4124', font=('arial', 10, 'bold'), bg='white').place(x=122, y=352)
StName10 = Label(LeftMayFrame2, text='M. Younousse Niassy', font=('arial', 10, 'bold'), bg='white').place(x=240, y=352)
CourseCode10 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=352)
box = ttk.Combobox(LeftMayFrame2, textvariable=value10, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=352)
StDetails10 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic2).place(x=720, y=352)

VStNam11 = 'M. Armand Seydou Séye '
VStAddress11 = 'DAKAR Diamniadio'
VstContact11 = '773706502'
SNo11 = Label(LeftMayFrame2, text='11', font=('arial', 10, 'bold'), bg='white').place(x=53, y=390)
StID11 = Label(LeftMayFrame2, text='4125', font=('arial', 10, 'bold'), bg='white').place(x=122, y=390)
StName11 = Label(LeftMayFrame2, text='M. Armand Seydou Séye', font=('arial', 10, 'bold'), bg='white').place(x=240, y=390)
CourseCode11 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=390)
box = ttk.Combobox(LeftMayFrame2, textvariable=value11, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=390)
StDetails11 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic10).place(x=720, y=390)


VStNam12 = 'Mme. Coumba Diallo '
VStAddress12 = 'DAKAR Diamniadio'
VstContact12 = '784744182'
SNo12 = Label(LeftMayFrame2, text='12', font=('arial', 10, 'bold'), bg='white').place(x=53, y=428)
StID12 = Label(LeftMayFrame2, text='4126', font=('arial', 10, 'bold'), bg='white').place(x=122, y=428)
StName12 = Label(LeftMayFrame2, text='Mme. Coumba Diallo', font=('arial', 10, 'bold'), bg='white').place(x=240, y=428)
CourseCode12 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=428)
box = ttk.Combobox(LeftMayFrame2, textvariable=value12, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=428)
StDetails12 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic12).place(x=720, y=428)


VStNam13 = 'M. Modou Diop '
VStAddress13 = 'DAKAR Colobane'
VstContact13 = '782205978'
SNo13 = Label(LeftMayFrame2, text='13', font=('arial', 10, 'bold'), bg='white').place(x=53, y=466)
StID13 = Label(LeftMayFrame2, text='4127', font=('arial', 10, 'bold'), bg='white').place(x=122, y=466)
StName13 = Label(LeftMayFrame2, text='M. Modou Diop', font=('arial', 10, 'bold'), bg='white').place(x=240, y=466)
CourseCode13 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=466)
box = ttk.Combobox(LeftMayFrame2, textvariable=value13, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=466)
StDetails13 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic13).place(x=720, y=466)

StNam14 = 'M. Babacar Déme'
VStAddress14 = 'DAKAR Dimniadio'
VstContact14 = '772226964'
SNo14 = Label(LeftMayFrame2, text='14', font=('arial', 10, 'bold'), bg='white').place(x=53, y=504)
StID14 = Label(LeftMayFrame2, text='4128', font=('arial', 10, 'bold'), bg='white').place(x=122, y=504)
StName14 = Label(LeftMayFrame2, text='M. Babacar Déme', font=('arial', 10, 'bold'), bg='white').place(x=240, y=504)
CourseCode14 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=504)
box = ttk.Combobox(LeftMayFrame2, textvariable=value14, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=504)
StDetails14 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic14).place(x=720, y=504)


StNam15 = 'M. Abdoulay Diallo'
VStAddress15 = 'DAKAR Colobane'
VstContact15 = '775234863'
SNo15 = Label(LeftMayFrame2, text='15', font=('arial', 10, 'bold'), bg='white').place(x=53, y=542)
StID15 = Label(LeftMayFrame2, text='4129', font=('arial', 10, 'bold'), bg='white').place(x=122, y=542)
StName15 = Label(LeftMayFrame2, text='M. Abdoulay Diallo', font=('arial', 10, 'bold'), bg='white').place(x=240, y=542)
CourseCode15 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=542)
box = ttk.Combobox(LeftMayFrame2, textvariable=value15, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=542)
StDetails15 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic15).place(x=720, y=542)

StNam15 = 'M. Moussa Diéry Diaw'
VStAddress16 = 'DAKAR Colobane'
VstContact16 = '778364424'
SNo16 = Label(LeftMayFrame2, text='16', font=('arial', 10, 'bold'), bg='white').place(x=53, y=580)
StID16 = Label(LeftMayFrame2, text='4130', font=('arial', 10, 'bold'), bg='white').place(x=122, y=580)
StName16 = Label(LeftMayFrame2, text='M. Moussa Diéry Diaw', font=('arial', 10, 'bold'), bg='white').place(x=240, y=580)
CourseCode16 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=580)
box = ttk.Combobox(LeftMayFrame2, textvariable=value16, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=580)
StDetails16 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic16).place(x=720, y=580)


VStNam17 = 'M. Cheikh Diop '
VStAddress17 = 'DAKAR Keur Massar'
VstContact17 = '781564446'
SNo17 = Label(LeftMayFrame2, text='17', font=('arial', 10, 'bold'), bg='white').place(x=53, y=618)
StID17 = Label(LeftMayFrame2, text='4131', font=('arial', 10, 'bold'), bg='white').place(x=122, y=618)
StName17 = Label(LeftMayFrame2, text='M. Cheikh Diop', font=('arial', 10, 'bold'), bg='white').place(x=240, y=618)
CourseCode17 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=618)
box = ttk.Combobox(LeftMayFrame2, textvariable=value17, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=618)
StDetails17 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic17).place(x=720, y=618)


StNam18 = 'M. Moussa Guissé'
VStAddress18 = 'DAKAR Foire'
VstContact18 = '774201893'
SNo18 = Label(LeftMayFrame2, text='18', font=('arial', 10, 'bold'), bg='white').place(x=53, y=656)
StID18 = Label(LeftMayFrame2, text='4132', font=('arial', 10, 'bold'), bg='white').place(x=122, y=656)
StName18 = Label(LeftMayFrame2, text='M. Moussa Guissé', font=('arial', 10, 'bold'), bg='white').place(x=240, y=656)
CourseCode18 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=656)
box = ttk.Combobox(LeftMayFrame2, textvariable=value18, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=656)
StDetails18 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic18).place(x=720, y=656)

StNam19 = 'Mme. Mossane Sarr'
VStAddress19 = 'DAKAR Diamniadio'
VstContact19 = '774964287'
SNo19 = Label(LeftMayFrame2, text='19', font=('arial', 10, 'bold'), bg='white').place(x=53, y=694)
StID19 = Label(LeftMayFrame2, text='4133', font=('arial', 10, 'bold'), bg='white').place(x=122, y=694)
StName19 = Label(LeftMayFrame2, text='Mme. Mossane Sarr', font=('arial', 10, 'bold'), bg='white').place(x=240, y=694)
CourseCode19 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=694)
box = ttk.Combobox(LeftMayFrame2, textvariable=value19, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=694)
StDetails19 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic19).place(x=720, y=694)

StNam20 = 'Mme. Ramatoulaye Sow'
VStAddress20 = 'DAKAR Diamniadio'
VstContact20 = '778906586'
SNo20 = Label(LeftMayFrame2, text='20', font=('arial', 10, 'bold'), bg='white').place(x=53, y=732)
StID20 = Label(LeftMayFrame2, text='4134', font=('arial', 10, 'bold'), bg='white').place(x=122, y=732)
StName20 = Label(LeftMayFrame2, text='Mme. Ramatoulaye Sow', font=('arial', 10, 'bold'), bg='white').place(x=240, y=732)
CourseCode20 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=732)
box = ttk.Combobox(LeftMayFrame2, textvariable=value20, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=732)
StDetails20 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic20).place(x=720, y=732)

StNam21 = 'Mme. Sanou Ndiaye'
VStAddress21 = 'DAKAR Diamniadio'
VstContact21 = '786123853'
SNo21 = Label(LeftMayFrame2, text='21', font=('arial', 10, 'bold'), bg='white').place(x=53, y=770)
StID21 = Label(LeftMayFrame2, text='4135', font=('arial', 10, 'bold'), bg='white').place(x=122, y=770)
StName21 = Label(LeftMayFrame2, text='Mme. Sanou Ndiaye', font=('arial', 10, 'bold'), bg='white').place(x=240, y=770)
CourseCode21 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=770)
box = ttk.Combobox(LeftMayFrame2, textvariable=value21, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=770)
StDetails21 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic21).place(x=720, y=770)

StNam22 = 'Mme. Khary Sarr'
VStAddress22 = 'DAKAR Diamniadio'
VstContact22 = '762922793'
SNo22 = Label(LeftMayFrame2, text='22', font=('arial', 10, 'bold'), bg='white').place(x=53, y=808)
StID22 = Label(LeftMayFrame2, text='4136', font=('arial', 10, 'bold'), bg='white').place(x=122, y=808)
StName22 = Label(LeftMayFrame2, text='Mme. Khary Sarr', font=('arial', 10, 'bold'), bg='white').place(x=240, y=808)
CourseCode22 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=808)
box = ttk.Combobox(LeftMayFrame2, textvariable=value22, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=808)
StDetails22 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic22).place(x=720, y=808)



StNam23 = 'Mme. Rokhaya Diagne'
VStAddress23 = 'DAKAR Diamniadio'
VstContact23 = '703139528'
SNo23 = Label(LeftMayFrame2, text='23', font=('arial', 10, 'bold'), bg='white').place(x=53, y=846)
StID23 = Label(LeftMayFrame2, text='4136', font=('arial', 10, 'bold'), bg='white').place(x=122, y=846)
StName23 = Label(LeftMayFrame2, text='Mme. Rokhaya Diagne', font=('arial', 10, 'bold'), bg='white').place(x=240, y=846)
CourseCode23 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=846)
box = ttk.Combobox(LeftMayFrame2, textvariable=value23, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=846)
StDetails23 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic23).place(x=720, y=846)


StNam24 = 'Mme. Ndeye khady '
VStAddress24 = 'DAKAR Thiaroye'
VstContact24 = '786143364'
SNo24 = Label(LeftMayFrame2, text='24', font=('arial', 10, 'bold'), bg='white').place(x=53, y=884)
StID24 = Label(LeftMayFrame2, text='4137', font=('arial', 10, 'bold'), bg='white').place(x=122, y=884)
StName24 = Label(LeftMayFrame2, text='Mme. Ndeye khady', font=('arial', 10, 'bold'), bg='white').place(x=240, y=884)
CourseCode24 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=884)
box = ttk.Combobox(LeftMayFrame2, textvariable=value24, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=884)
StDetails24 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic24).place(x=720, y=884)


StNam25 = 'Mme. Pongui Soumaré'
VStAddress25 = 'DAKAR Rufisque'
VstContact25 = '777473887'
SNo25 = Label(LeftMayFrame2, text='25', font=('arial', 10, 'bold'), bg='white').place(x=53, y=922)
StID25 = Label(LeftMayFrame2, text='4138', font=('arial', 10, 'bold'), bg='white').place(x=122, y=922)
StName25 = Label(LeftMayFrame2, text='Mme. Pongui Soumaré', font=('arial', 10, 'bold'), bg='white').place(x=240, y=922)
CourseCode25 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=922)
box = ttk.Combobox(LeftMayFrame2, textvariable=value25, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=922)
StDetails25 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic25).place(x=720, y=922)


StNam26 = 'M. Mensour Kairé'
VStAddress26 = 'DAKAR '
VstContact26 = '765956463'
SNo26 = Label(LeftMayFrame2, text='26', font=('arial', 10, 'bold'), bg='white').place(x=53, y=960)
StID26 = Label(LeftMayFrame2, text='4139', font=('arial', 10, 'bold'), bg='white').place(x=122, y=960)
StName26 = Label(LeftMayFrame2, text='M. Mensour Kairé', font=('arial', 10, 'bold'), bg='white').place(x=240, y=960)
CourseCode26 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=960)
box = ttk.Combobox(LeftMayFrame2, textvariable=value26, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=960)
StDetails26 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic26).place(x=720, y=960)


StNam27 = 'M.Seydou Sow'
VStAddress27 = 'DAKAR Colobane'
VstContact27 = '773671741'
SNo27 = Label(LeftMayFrame2, text='27', font=('arial', 10, 'bold'), bg='white').place(x=53, y=998)
StID27 = Label(LeftMayFrame2, text='4140', font=('arial', 10, 'bold'), bg='white').place(x=122, y=998)
StName27 = Label(LeftMayFrame2, text='M.Seydou Sow', font=('arial', 10, 'bold'), bg='white').place(x=240, y=998)
CourseCode27 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402, y=998)
box = ttk.Combobox(LeftMayFrame2, textvariable=value27, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=998)
StDetails27 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic27).place(x=720, y=998)


VStNam28 = 'Mme Marane Ndao'
VStAddress28 = 'DAKAR Diamniadio'
VstContact28 = '777464277'
SNo28 = Label(LeftMayFrame2, text='28', font=('arial', 10, 'bold'), bg='white').place(x=53, y=1036)
StID28 = Label(LeftMayFrame2, text='4141', font=('arial', 10, 'bold'), bg='white').place(x=122, y=1036)
StName28 = Label(LeftMayFrame2, text='Mme Marane Ndao', font=('arial', 10, 'bold'), bg='white').place(x=240,y=1036)
CourseCode28 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=1036)
box = ttk.Combobox(LeftMayFrame2, textvariable=value28, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=1036)
StDetails28 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic28).place(x=720, y=1036)

VStNam29 = 'Mme Edith Gomis'
VStAddress29 = 'DAKAR Rufisque'
VstContact29 = '784799122'
SNo29 = Label(LeftMayFrame2, text='29', font=('arial', 10, 'bold'), bg='white').place(x=53, y=1074)
StID29 = Label(LeftMayFrame2, text='4142', font=('arial', 10, 'bold'), bg='white').place(x=122, y=1074)
StName29 = Label(LeftMayFrame2, text='Mme Edith Gomis', font=('arial', 10, 'bold'), bg='white').place(x=240,y=1074)
CourseCode29 = Label(LeftMayFrame2, text='1234', font=('arial', 10, 'bold'), bg='white').place(x=402,y=1074)
box = ttk.Combobox(LeftMayFrame2, textvariable=value29, state='readonly')
box['values'] = ('', 'Present', 'Absent', 'Rentré', 'En retard', 'Malade')
box.current(0)
box.place(x=550, y=1074)
StDetails29 = ttk.Button(LeftMayFrame2, text='View Details', width=27, command = pic29).place(x=720, y=1074) 



AFframe = Frame(AttendanceReg, height=35, width=1280, bg='sky blue').place(relx=0, y=685)


AttendanceReg.mainloop()
