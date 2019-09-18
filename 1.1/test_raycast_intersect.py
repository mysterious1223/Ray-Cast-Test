import tkinter
import random
import time
from ray_math import *
import threading

exit_sig = False
x1 = 0
y1 = 0
x2 = 0
y2 = 0


window = Tk()


window.geometry('1000x860')
canvas_width = 800
canvas_height = 600
w = Canvas(window,
           width=canvas_width,
           height=canvas_height)


endPoints = vec2(0,0)
startPoints = vec2(100,100)
RectPos1 = vec2 (250,250)
RectPos2 = vec2 (400,400)

def pos ():
    print ("pos ++")

def neg ():
    print ("neg --")
myRect = Rectangle (RectPos1, RectPos2)
line_seg = Line (startPoints, endPoints, w)

butt = tkinter.Button (window, text="+", command=pos)
butt.place(x=10, y=10)
butt.pack()

butt2 = tkinter.Button (window, text="-", command=neg)
butt2.pack()


def cb (event):
    print ("left clicked ", event.x, event.y)
    
    line_seg.setEndPos (event.x,event.y)
    
    line_seg.ReDraw()

    line_seg.CalculateSlope()

def cb2 (event):
    print ("right clicked ", event.x, event.y)
    
    line_seg.setStartPos (event.x,event.y)
    line_seg.ReDraw()
    line_seg.CalculateSlope()


w.bind ("<Button-1>", cb)
w.bind ("<Button-2>", cb2)
w.pack()


line_seg.Initdraw()


itemID_UI = w.create_text(200,10,fill='blue', text="slope")

myRect.InitDraw(w)
myRect.DrawVectorEdges()

ray_detector = Ray_CollisionDetector(w)

ray_detector.InitCollision (line_seg, myRect)

print ("Rect verticies {")
print ("A = " + myRect.getVertA().DEBUG_PRINT())
print ("B = " + myRect.getVertB().DEBUG_PRINT())
print ("C = " + myRect.getVertC().DEBUG_PRINT())
print ("D = " + myRect.getVertD().DEBUG_PRINT())
print ("}")

def run_loop ():


    i = 0
    val = 1
    while 1:
        
        
       
        try:
            window.update_idletasks()
            window.update()
            vec = ray_detector.CheckForCollisions()
            
            
            myRect.reDraw()
            #myRect.MoveToPoint(myRect.getPos1().getX() + val,myRect.getPos1().getY(),
            #                myRect.getPos2().getX() + val,myRect.getPos2().getY()
            #                  )
            
            w.itemconfigure (itemID_UI, text="Our line " +str (line_seg.GetEQLLineText()))
        except:
            print ("Program ended")
            exit()
        
        
        time.sleep(.1)


x_1 = threading.Thread (target=run_loop)

x_1.start()



mainloop()



#run_loop()
