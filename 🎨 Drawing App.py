from tkinter import*   #importibg tkinter

win = Tk()
win.geometry("1100x600")                 # window 
win.resizable(False,False)                

frame1 = Frame(win,height=100,width=1100)   #commond Frame creating
frame1.grid(row = 0,column=0,sticky= NW)



dframe = Frame(frame1,height =100 ,width=100,bg ="grey")
dframe.grid(row=0,column =1)

size_list = Listbox(dframe,)


tframe = Frame(frame1,height =100 ,width=100,bg ="grey")
tframe.grid(row=0,column =0)

def use_pencil():
    stroke_colour.set("black")
    

def use_erasser():
    stroke_colour.set("white")
    can["cursor"] = DOTBOX

pencil = Button(tframe,text="Pencil",width=10, command= use_pencil)
pencil.grid(row =0,column= 0)

eraser = Button(tframe,text="eraser",width=10, command= use_erasser )
eraser.grid(row =1,column= 0)

tlabel = Label(tframe,text ="Tools",width=10)
tlabel.grid(row =3,column =0)

frame2 = Frame(win,height= 500,width=1100)  #canvas Frame Creating 
frame2.grid(row = 1,column =0 )

can = Canvas(frame2,height= 500 ,width = 1100,bg = "white", )  # Canvas 
can.grid(row = 1,column =0 )

stroke_colour = StringVar()
stroke_colour.set("red")


prevPoint =[0,0]                                                        #for making pencil we create two var prevpoint and current point defalt set 0,0 
currPoint = [0,0]                                                       #then we create function with argument event then we make our 2 variable global to local 

def paint(event):                                                       #another variable x,y for mouse cordinates then
    print(event.type)                                                   #at mouse currrent location that point is set in current point variable 
    global prevPoint
    global currPoint                                                    #conditon i prevPoint is not equal to 0,0 then it will form a line  bet prevpoint and current point 
    x = event.x                                                         #after making ;ine the value of current point is stored in prev point for next moveee
    y = event.y
    currPoint = [x,y]
    if prevPoint != [0,0]:
        can.create_line(prevPoint[0], prevPoint[1],currPoint[0],currPoint[1],fill= stroke_colour.get())
    prevPoint =currPoint

    if event.type == "5":                                               #for stopping line production when button is relased we use buttonrelease bind  and when its value equal
        prevPoint = [0,0]                                               #equal to 5 then automatically the prevpoint value is set to be 0,0 prevPoint = [0,0]   


can.bind("<B1-Motion>",paint)
can.bind("<ButtonRelease-1>",paint)










win.mainloop()
