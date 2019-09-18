from tkinter import *

class vec2:
    
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def getX (self):
        return self.x
    def getY (self):
        return self.y
    def setX (self, x):
        self.x = x
    def setY (self, y):
        self.y = y
    
    def DEBUG_PRINT(self):
        return ("x=" + str (self.getX()) + ", y=" + str(self.getY()) )
    
    def print_equation_of_line (self, end):
        x_con = self.x - end.getX ()
        y_con = self.y - end.getY ()
        m = y_con/x_con
        
        #print ( self.y, 'y = ',y_con,'/',x_con, ' * (', self.x,'x)')
        
        self.eq = str(self.y) + 'y = '+str(y_con)+'/'+str(x_con)+ ' * ('+ str(self.x)+'x)'
        
        return self.eq



class Rectangle:
    def __init__ (self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
    def InitDraw (self, cvas):
        self.w = cvas
        self.itemID_rect = cvas.create_rectangle(
                                                 self.getPos2().getX(), self.getPos2().getY()
                                                 , self.getPos1().getX(), self.getPos1().getY())
    
    
    def reDraw (self):
        self.w.coords(self.itemID_rect, self.pos2.getX(), self.pos2.getY(),
                         self.pos1.getX(), self.pos1.getY())
    def MoveToPoint(self, x1, y1, x2, y2):
        
        self.pos1.setX(x1)
        
        self.pos1.setY(y1)
        
        self.pos2.setX(x2)
        
        self.pos2.setY(y2)
        self.cvas.coords(self.itemID_rect, self.pos2.getX(), self.pos2.getY(),
                         self.pos1.getX(), self.pos1.getY()
                         )
    
    
    def getPos1 (self):
        return self.pos1
    def getPos2 (self):
        return self.pos2
    def DrawVectorEdges(self):
        itemID_r1_text = self.w.create_text(self.getPos1().getX(),self.getPos1().getY(),fill='green', text="A")
        itemID_r3_text = self.w.create_text(self.getPos1().getX(),self.getPos2().getY(),fill='red', text="B")
        itemID_r4_text = self.w.create_text(self.getPos2().getX(),self.getPos1().getY(),fill='orange', text="C")
        itemID_r2_text = self.w.create_text(self.getPos2().getX(),self.getPos2().getY(),fill='purple', text="D")
    def getVertA (self):
        return self.getPos1()
    def getVertB (self):
        return vec2 (self.getPos1().getX(),self.getPos2().getY())
    def getVertC (self):
        return vec2 (self.getPos2().getX(),self.getPos1().getY())
    def getVertD (self):
        return self.getPos2()



class Line :
    #start end canvas object
    def __init__ (self, vert1, vert2, cvas):
        self.cvas = cvas
        self.startPos = vert1
        self.endPos = vert2
    
    
    
    def UpdateEndPoint (self, pos):
        self.endPos = pos
    def UpdateStartPoint(self, pos):
        self.startPos = pos

    def getStartPos (self):
        return self.startPos

    def getEndPos (self):
        return self.endPos

    def Initdraw (self):
        #print ("initial draw")
        self.itemID = self.cvas.create_line(self.getStartPos().getX(),self.getStartPos().getY(),self.getEndPos().getX(),self.getEndPos().getY(), fill="red")
        self.itemID_s = self.cvas.create_text(self.getStartPos().getX(),self.getStartPos().getY(),fill='red', text="start")
        self.itemID_e = self.cvas.create_text(self.getEndPos().getX(),self.getEndPos().getY(),fill='blue', text="end")
        self.CalculateSlope ()
    
    def setStartPos (self, x, y):
        self.startPos.setX(x)
        self.startPos.setY(y)
    
    def setEndPos (self, x, y):
        self.endPos.setX(x)
        self.endPos.setY(y)
    
    def ReDraw (self):
        print ("re draw")
        
        self.cvas.coords (self.itemID,self.getStartPos().getX(),self.getStartPos().getY(),self.getEndPos().getX(),self.getEndPos().getY())
        
        self.cvas.coords(self.itemID_e, self.getEndPos().getX(),self.getEndPos().getY())
        
        self.cvas.coords(self.itemID_s, self.getStartPos().getX(),self.getStartPos().getY())
        
        print ("end points coor is ", self.cvas.coords(self.itemID_e))
        
        
        self.cvas.itemconfigure (self.itemID_e, text ="end x= " + str(self.getEndPos().getX()) +
                                 ", y= " + str(self.getEndPos().getY())
                                )
        print ("start points coor is ", self.cvas.coords(self.itemID_s))
                                
        self.cvas.itemconfigure (self.itemID_s, text ="start x= " + str(self.getStartPos().getX()) +
                                 ", y= " + str(self.getStartPos().getY())
                                 )
    def CalculateSlope (self):
        #print ("Calculating slope")
        #print ("DEBUG y = " + str(self.getEndPos().getY()-self.getStartPos().getY())+" x =" + str (self.getEndPos().getX()-self.getStartPos().getX()))
      
        if self.getEndPos().getX()-self.getStartPos().getX() == 0:
            self.slope_m = 0
            return
          
        self.slope_m = (self.getEndPos().getY()-self.getStartPos().getY())/(self.getEndPos().getX()-self.getStartPos().getX())
    
        return
    
    def GetSlope (self):
        self.CalculateSlope ()
        return self.slope_m
    def GetBConstant (self):
        self.CalculateEquationOfLine()
        return self.b
    def CalculateEquationOfLine(self):
        
        
        
        self.b = self.getEndPos().getY()-self.getEndPos().getX() * self.GetSlope()


    
    def GetEQLLineText (self):
        self.CalculateEquationOfLine()
        
        if self.b > 0:
            return ("y=" + str(self.GetSlope()) + "x +"+str(self.b))
        if self.b < 0:
            return ("y=" + str(self.GetSlope()) + "x "+str(self.b))

        return ("y=" + str(self.GetSlope()) + "x")

class Ray_CollisionDetector:
    def __init__ (self, cvas):
        self.cvas = cvas
        print ("starting...")
    def InitCollision(self,obj_line, obj_rect):
        self.ourline = obj_line
        self.ourrect = obj_rect
    def CheckForCollisions (self):
        
        size = 5
        
        #print ("loop and check if things have collided with ray")
        AB = Line (self.ourrect.getVertA(), self.ourrect.getVertB(), self.cvas)
    
        CD = Line (self.ourrect.getVertC(), self.ourrect.getVertD(), self.cvas)
        
        AC = Line (self.ourrect.getVertA(), self.ourrect.getVertC(), self.cvas)
        
        BD = Line (self.ourrect.getVertB(), self.ourrect.getVertD(), self.cvas)
        
        
        vecAB = self.CheckForIntersectingLines (self.ourline, AB,1)
        vecCD = self.CheckForIntersectingLines (self.ourline, CD,1)
        vecAC = self.CheckForIntersectingLines (self.ourline, AC,4)
        vecBD = self.CheckForIntersectingLines (self.ourline, BD,4)
        
        self.cvas.create_rectangle(vecAB.getX() - size, vecAB.getY() - size,vecAB.getX(),vecAB.getY(), fill='red')
        
        self.cvas.create_rectangle(vecCD.getX() - size, vecCD.getY() - size,vecCD.getX(),vecCD.getY(), fill='red')
    
        self.cvas.create_rectangle(vecAC.getX() - size, vecAC.getY() - size,vecAC.getX(),vecAC.getY(), fill='red')
        
        self.cvas.create_rectangle(vecBD.getX() - size, vecBD.getY() - size,vecBD.getX(),vecBD.getY(), fill='red')
    
    
    def CheckForIntersectingLines (self, ray, line, offset):
        #print ("checking line against ray")
        
        ray.CalculateEquationOfLine()
        line.CalculateEquationOfLine()
     
     
     
        a = line.GetSlope() - ray.GetSlope()
        b = ray.GetBConstant () - line.GetBConstant()
        
        
     
     #a = -1 * (line.GetSlope()) + ray.GetSlope()
     #  b = -1 * (ray.GetBConstant()) + line.GetBConstant()

        if (a == 0):
           print ("Divide by zerp a is zero")
           return False

        x = b/a
        #verts
        
        if line.GetSlope () == 0 and offset != 4:
            #print ("x = " + str(x))
        #x = line.GetBConstant()
            x = line.getStartPos().getX()
        #x = b / a
        
        y = ray.GetSlope () * x + ray.GetBConstant()

        
        
        #print ("found an intersecting point x="+ str(x)+ " , y="+str(y))

        return vec2 (x, y)
