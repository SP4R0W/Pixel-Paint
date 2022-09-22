#====================================
#IMPORTS
import pickle
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#Initialize the main window
root = Tk()
root.title("Pixel Paint")
root.iconbitmap('icon.ico')

#====================================
#VARIABLES
#====================================


#Set variables and a dictionary...
size = IntVar()
size.set(0)

loaded = StringVar()
loaded.set("")

color = StringVar()
color.set("")

fillcolor = StringVar()
fillcolor.set("")

filledcolor = StringVar()
filledcolor.set("")

global buttons
buttons = {}

#====================================
#PROGRAM FUNCTIONS
#====================================

def changeColor(x,y,index):
    print(x,y,index)
    
    #Get the color variable
    c = color.get()

    #Draw the button with the current color option set and change the value in dictionary
    button = Button(root,text="",padx=6,pady=0.1,bg=c,command=lambda x=x,y=y:changeColor(x,y,index))
    button.grid(columnspan=1,row=x,column=y)
    buttons["Button"+str(index)] = [c]

def drawScreen():
    global buttons
    #Get the size of an image and add it to dictionary
    s = size.get()

    buttons["Size"] = s
    
    count = 1

    gridx = 0   
    gridy = 0

    for x in range(0,s):

        for x in range(0,s):
            #Draw the buttons
            button = Button(root,text="",padx=6,pady=0.1,bg='snow',command=lambda x=gridx,y=gridy,index=count:changeColor(x,y,index))
            button.grid(columnspan=1,row=gridx,column=gridy)
            buttons["Button"+str(count)] = ['snow']
            count +=1
            gridx += 1

        gridy += 1
        gridx = 0

def drawLoadedScreen():
    #This is the same as drawButton function, but it is only used when loading an image.
    global buttons
    s = size.get()

    buttons["Size"] = s
    
    count = 1

    gridx = 0   
    gridy = 0

    for x in range(0,s):

        for x in range(0,s):
            print(buttons["Button"+str(count)])
            button = Button(root,text="",padx=6,pady=0.1,bg=buttons["Button"+str(count)],command=lambda x=gridx,y=gridy,index=count:changeColor(x,y,index))
            button.grid(columnspan=1,row=gridx,column=gridy)
            count +=1
            gridx += 1

        gridy += 1
        gridx = 0

#====================================
#MENU FUNCTIONS
#====================================

def saveMenu():
    s = size.get()
    l = loaded.get()

    if s == 0:
        #If size of the image = 0; basically it isnt drawed
        messagebox.showwarning("Warning","You must draw an image first.")
    else:
        if l == "":
            #If there was a file loaded before, then it will save to that file. If not, it will create a new file.
            root.filename =  filedialog.asksaveasfilename(initialdir="C:/",title="Choose where to save",filetypes=(("Pickle files","*.pickle"),("All files","*.*")))
            saveFile = open(root.filename,'wb')
            pickle.dump(buttons,saveFile)
            saveFile.close()
        else:
            saveFile = open(l,'wb')
            pickle.dump(buttons,saveFile)
            saveFile.close()

def saveasMenu():
    s = size.get()
    #Same as saveMenu, but there is only save as function here.
    if s == 0:
        messagebox.showwarning("Warning","You must draw an image first.")
    else:
        root.filename =  filedialog.asksaveasfilename(initialdir="C:/",title="Choose where to save",filetypes=(("Pickle files","*.pickle"),("All files","*.*")))
        saveFile = open(root.filename,'wb')
        pickle.dump(buttons,saveFile)
        saveFile.close()

def loadMenu():
    global buttons
    #Load files.
    root.filename = filedialog.askopenfilename(initialdir="C:/",title="Choose a file to open",filetypes=(("Pickle files","*.pickle"),("All files","*.*")))
    loadFile = open(root.filename,'rb')
    buttons = pickle.load(loadFile)
    print(buttons)
    
    #Set loaded to the current file path.
    print(loadFile)
    loaded.set(root.filename)
    l = loaded.get()
    print("The l is:"+l)

    size.set(buttons["Size"])
    drawLoadedScreen()


def sisMenu():
    #The function for changing the size of an image
    sizeMenu = Toplevel()

    labelHelp = Label(sizeMenu,text="Please choose the size of the image.").pack()

    button4 = Checkbutton(sizeMenu,text="4x4 size",variable=size,offvalue=0,onvalue=4).pack()
    button8 = Checkbutton(sizeMenu,text="8x8 size",variable=size,offvalue=0,onvalue=8).pack()
    button12 = Checkbutton(sizeMenu,text="12x12 size",variable=size,offvalue=0,onvalue=12).pack()
    button16 = Checkbutton(sizeMenu,text="16x16 size",variable=size,offvalue=0,onvalue=16).pack()
    button24 = Checkbutton(sizeMenu,text="24x24 size",variable=size,offvalue=0,onvalue=24).pack()
    button32 = Checkbutton(sizeMenu,text="32x32 size",variable=size,offvalue=0,onvalue=32).pack()
    button40 = Checkbutton(sizeMenu,text="40x40 size",variable=size,offvalue=0,onvalue=40).pack()
    button56 = Checkbutton(sizeMenu,text="56x56 size",variable=size,offvalue=0,onvalue=56).pack()
    button64 = Checkbutton(sizeMenu,text="64x64 size",variable=size,offvalue=0,onvalue=64).pack()

    button = Button(sizeMenu,text="Draw the image",command=drawScreen).pack()

def spcMenu():
    #The function for changing the color of paint tool
    sizeMenu = Toplevel()

    labelHelp = Label(sizeMenu,text="Please choose the color of the paint tool.").pack()

    buttonWhite = Checkbutton(sizeMenu,text="White",fg='Snow',variable=color,onvalue='Snow').pack()
    buttonBlack = Checkbutton(sizeMenu,text="Black",fg='black',variable=color,onvalue='black').pack()
    buttonSilver = Checkbutton(sizeMenu,text="Silver",fg='snow4',variable=color,onvalue='snow4').pack()
    buttonGray = Checkbutton(sizeMenu,text="Gray",fg='gray',variable=color,onvalue='gray').pack()
    buttonBrown = Checkbutton(sizeMenu,text="Brown",fg='sienna4',variable=color,onvalue='sienna4').pack()
    buttonRed = Checkbutton(sizeMenu,text="Red",fg='red',variable=color,onvalue='red').pack()
    buttonPink = Checkbutton(sizeMenu,text="Pink",fg='deeppink',variable=color,onvalue='deeppink').pack()
    buttonYellow = Checkbutton(sizeMenu,text="Yellow",fg='yellow2',variable=color,onvalue='yellow2').pack()
    buttonOrange = Checkbutton(sizeMenu,text="Orange",fg='orange',variable=color,onvalue='orange').pack()
    buttonGreen = Checkbutton(sizeMenu,text="Green",fg='forestgreen',variable=color,onvalue='forestgreen').pack()
    buttonLime = Checkbutton(sizeMenu,text="Lime",fg='limegreen',variable=color,onvalue='limegreen').pack()
    buttonBlue = Checkbutton(sizeMenu,text="Blue",fg='blue',variable=color,onvalue='blue').pack()
    buttonIndigo = Checkbutton(sizeMenu,text="Indigo",fg='navy',variable=color,onvalue='navy').pack()
    buttonPurple = Checkbutton(sizeMenu,text="Purple",fg='purple',variable=color,onvalue='purple').pack()
    buttonViolet = Checkbutton(sizeMenu,text="Violet",fg='violet',variable=color,onvalue='violet').pack()
    buttonGold = Checkbutton(sizeMenu,text="Gold",fg='gold',variable=color,onvalue='gold').pack()

def helpMenu():
    messagebox.showinfo("Help",'''To clear an image, restart the program.
To save an image, you must create it first. 
Create it by clicking Edit cascade, then Set Image Size option. 
Please note that there is currently no way to open saved images in other graphical programs such as Paint.
Currently, in order to do that, you must take a screenshot of the drawing using programs such as Lightshot.
Also, please remember to add .pickle at the end of a file. Python sometimes doesnt do that.
More options such as custom colors and size of the image soon!
If you need any extra help, contact me on Github!''')

def aboutMenu():
    messagebox.showinfo("About","Pixel Paint program. Version 1.0. Created by @xXx_Bain_xXx#1237, aka SP4R0W")

#====================================
#PROGRAM GUI
#====================================

#Draw main GUI.

paintMenu = Menu(root)

paintMenuFile = Menu(paintMenu,tearoff=0)
paintMenuEdit = Menu(paintMenu,tearoff=0)
paintMenuInfo = Menu(paintMenu,tearoff=0)

paintMenu.add_cascade(label="File",menu=paintMenuFile)
paintMenu.add_cascade(label="Edit",menu=paintMenuEdit)
paintMenu.add_cascade(label="Info",menu=paintMenuInfo)

paintMenuFile.add_command(label="Save",command=saveMenu)
paintMenuFile.add_command(label="Save As",command=saveasMenu)
paintMenuFile.add_separator()
paintMenuFile.add_command(label="Load",command=loadMenu)

paintMenuEdit.add_command(label="Set Image Size",command=sisMenu)
paintMenuEdit.add_command(label="Set Paint Color",command=spcMenu)

paintMenuInfo.add_command(label="Help",command=helpMenu)
paintMenuInfo.add_command(label="About",command=aboutMenu)


root.config(menu=paintMenu)
root.mainloop()
