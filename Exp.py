python name=🎨 Drawing App.py url=https://github.com/Prathamesh0729/Ms-paint-/blob/02cbfe05b6b66b6ce06aef53037eecd7b7389fd1/🎨%20Drawing%20App.py
from tkinter import*   # Importing all modules from Tkinter (used for GUI applications)

# Creating the main application window
win = Tk()
win.geometry("1100x600")  # Setting window dimensions
win.resizable(False, False)  # Disabling resizing of the window

# Creating a top frame (frame1) for tools and settings
frame1 = Frame(win, height=100, width=1100)
frame1.grid(row=0, column=0, sticky=NW)

# Adding a drawing frame inside the top frame
dframe = Frame(frame1, height=100, width=100, bg="grey")
dframe.grid(row=0, column=1)

size_list = Listbox(dframe)  # Placeholder for size (not yet fully implemented)

# Adding a tools frame inside the top frame
tframe = Frame(frame1, height=100, width=100, bg="grey")
tframe.grid(row=0, column=0)

# Tool selection functions
def use_pencil():
    stroke_colour.set("black")  # Sets drawing color to black

def use_erasser():
    stroke_colour.set("white")  # Sets drawing color to white (erases on white canvas)
    can["cursor"] = DOTBOX  # Changes the cursor appearance

# 'Pencil' and 'Eraser' tool buttons
pencil = Button(tframe, text="Pencil", width=10, command=use_pencil)
pencil.grid(row=0, column=0)

eraser = Button(tframe, text="eraser", width=10, command=use_erasser)
eraser.grid(row=1, column=0)

# Label to indicate tools section
tlabel = Label(tframe, text="Tools", width=10)
tlabel.grid(row=3, column=0)

# Creating Frame (frame2) for the main drawing canvas
frame2 = Frame(win, height=500, width=1100)
frame2.grid(row=1, column=0)

# Creating the drawing Canvas with a white background
can = Canvas(frame2, height=500, width=1100, bg="white")
can.grid(row=1, column=0)

# Dynamic stroke color, initialized to red
stroke_colour = StringVar()
stroke_colour.set("red")

# Variables to store the previous and current paint (drawing) points
prevPoint = [0, 0]
currPoint = [0, 0]

# Painting function - used to draw while clicking/dragging the mouse
def paint(event):
    print(event.type)  # Prints event type for debugging
    global prevPoint
    global currPoint
    x = event.x  # Current x-coordinate of the mouse
    y = event.y  # Current y-coordinate of the mouse
    currPoint = [x, y]
    
    # If a previous point exists, draw a line from prevPoint to currPoint
    if prevPoint != [0, 0]:
        can.create_line(
            prevPoint[0], prevPoint[1],
            currPoint[0], currPoint[1],
            fill=stroke_colour.get()  # Line color based on the selected tool
        )
    prevPoint = currPoint  # Update prevPoint with current point
    
    # Reset prevPoint when the mouse button is released
    if event.type == "5":
        prevPoint = [0, 0]

# Bind events for drawing and mouse-release actions
can.bind("<B1-Motion>", paint)  # Binds the 'paint' function to mouse drag (Button 1 Motion)
can.bind("<ButtonRelease-1>", paint)  # Resets prevPoint when the mouse button is released

# Start the application event loop
win.mainloop()
