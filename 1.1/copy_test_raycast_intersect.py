from tkinter import *
import random
import time
from ray_math import *


endPoints = vec2(0,0)
startPoints = vec2(100,100)
RectPos1 = vec2 (250,250)
RectPos2 = vec2 (500,500)


myRect = Rectangle (RectPos1, RectPos2)


def cb (event):
    print ("left clicked ", event.x, event.y)
   
    endPoints.setX(event.x)
    endPoints.setY(event.y)
    w.coords (itemID,startPoints.getX(),startPoints.getY(),endPoints.getX(),endPoints.getY())
    w.coords(itemID_e, endPoints.getX(),endPoints.getY())
    print ("end points coor is ", w.coords(itemID_e))
    w.itemconfigure (itemID_e, text ="end x= " + str(endPoints.getX()) +
                     ", y= " + str(endPoints.getY())
                     )


#endPoints.print_equation_of_line(startPoints)

def cb2 (event):
    print ("right clicked ", event.x, event.y)
    startPoints.setX(event.x)
    startPoints.setY(event.y)
    
    w.coords (itemID,startPoints.getX(),startPoints.getY(),endPoints.getX(),endPoints.getY())
    
    
    w.coords(itemID_s, startPoints.getX(),startPoints.getY())
    w.itemconfigure (itemID_s, text ="start x= " + str(startPoints.getX()) +
                     ", y= " + str(startPoints.getY())
                     )
                     
                     
    
    print ("start points coor is ", w.coords(itemID_s))
#startPoints.print_equation_of_line(endPoints)
window = Tk()


window.geometry('1000x860')
canvas_width = 800
canvas_height = 600
w = Canvas(window,
           width=canvas_width,
           height=canvas_height)
w.bind ("<Button-1>", cb)
w.bind ("<Button-2>", cb2)
w.pack()


itemID = w.create_line(startPoints.getX(),startPoints.getY(),endPoints.getX(),endPoints.getY(), fill="red")
itemID_s = w.create_text(startPoints.getX(),startPoints.getY(),fill='red', text="start")
itemID_e = w.create_text(endPoints.getX(),endPoints.getY(),fill='blue', text="end")
itemID_UI = w.create_text(200,10,fill='blue', text="slope")

myRect.InitDraw(w)
myRect.DrawVectorEdges()
print ("Rect verticies {")
print ("A = " + myRect.getVertA().DEBUG_PRINT())
print ("B = " + myRect.getVertB().DEBUG_PRINT())
print ("C = " + myRect.getVertC().DEBUG_PRINT())
print ("D = " + myRect.getVertD().DEBUG_PRINT())
print ("}")


#w.delete(itemID)

#find_withtag(itemID)

#if w.find_withtag (itemID):
#   item = w.focus (itemID)
#   print ("found")
#item.fill ("blue")

#we can modify an item using canvas.itemconfigure (id, fill='blue', width=2)

#w.itemconfigure (itemID, fill='blue')
    #moving
    #w.coord(itemID, 0,0,0,0)
mainloop()


i = 0
val = 1
while 1:
    window.update_idletasks()
    window.update()
    

    try:
        myRect.reDraw()
        #myRect.MoveToPoint(myRect.getPos1().getX() + val,myRect.getPos1().getY(),
        #                myRect.getPos2().getX() + val,myRect.getPos2().getY()
        #                  )
        
        w.itemconfigure (itemID_UI, text=
        endPoints.print_equation_of_line(startPoints))
    except:
        print ("program execution complete!")
        exit()

    time.sleep(.1)




