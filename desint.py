#---------------------------------
# Desintegration radiocative v1.1
#---------------------------------
from tkinter import *
from tkinter import messagebox
import random
import time
from math import *
import sys
import platform
 
def randomColor():
    COLORS =['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
            'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
            'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
            'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
            'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
            'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
            'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
            'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
            'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
            'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
            'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
            'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
            'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
            'indian red', 'saddle brown', 'sandy brown',
            'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
            'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
            'pale violet red', 'maroon', 'medium violet red', 'violet red',
            'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
            'thistle', 'snow2', 'snow3',
            'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
            'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
            'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
            'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
            'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
            'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
            'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
            'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
            'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
            'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
            'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
            'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
            'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
            'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
            'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
            'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
            'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
            'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
            'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
            'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
            'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
            'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
            'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
            'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
            'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
            'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
            'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
            'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
            'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
            'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
            'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
            'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
            'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
            'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
            'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
            'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
            'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
            'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
            'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
            'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
            'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
            'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
            'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
            'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
            'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
            'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4']
    
    return COLORS[random.randint(0, len(COLORS)-1)]

def ctw(co, view, zoom):
    dwidth = game.width/2
    dheight = game.height/2
    coords = []
    for i in range(0, len(co)):
        if i%2 == 0:
            coords.append((co[i] - view[0])*zoom  + dwidth)
        else:
            coords.append((co[i] - view[1])*zoom  + dheight)
            
    return coords

def collisionPoint(co1, co2):
    if co1[2] != co1[0]:
        a = (co1[3]-co1[1])/(co1[2]-co1[0])
        b = co1[1] - a*co1[0]
    else:
        a = None
    if co2[2] != co2[0]:
        c = (co2[3]-co2[1])/(co2[2]-co2[0])
        d = co2[1] - c*co2[0]
    else:
        c = None
    if c == None or a == None:
        #print("Vert")
        if c == None and a != None:
            x = co2[0]
            y = a*x +b
        elif a == None and c != None:
            x = co1[0]
            y = c*x +d
        else:
            return None
    elif a == c:
        return None
    else:
        x = (d-b)/(a-c)
        y = a*x +b 
    if (co1[0]<= x <=co1[2] or co1[2]<= x <=co1[0]) and (co2[0]<= x <=co2[2] or co2[2]<= x <=co2[0]):
        if (a == None or c == None) and (co2[1]<= y <=co2[3] or co2[2]<= y <=co2[0]):
            return [x, y]
        elif a != None and c != None:
            return [x, y]
    return None

def normalise(vec):
    x = vec[2] - vec[0]
    y = vec[3] - vec[1]
    length = hypot(x, y)
    return [x/length,  y/length]

def delete(entity):
        entity.canvas.delete(entity.id)
        entity.game.entities.remove(entity)
        entity.removed = True

def createEvent(entity, timeOffset, events):
    entity.events.append([time.time()+timeOffset, events])

def clamp(mini, number, maxi):
    if number>=maxi:
        return maxi
    elif number<=mini:
        return mini
    elif mini<=number<=maxi:
        return number


class Settings:
    def __init__(self, player = None):
        self.root = Tk()
        self.root.title("Settings")
        #self.root.wm_attributes("-fullscreen", 1)
        self.root.protocol('WM_DELETE_WINDOW', self.quit)
        
        self.collisions = IntVar()
        
        self.instruction3 = Label(self.root,text="Nombre d'atomes: ")
        self.instruction3.grid(row=0,column=0,columnspan=1,sticky=W)
        
        self.nb = Entry(self.root)
        self.nb.grid(row=0,column=1,sticky=E)
        
        self.ok_button = Button(self.root,text="OK", command=self.apply)
        self.ok_button.grid(row=0,column=2,sticky=W)
        
        self.load_button = Checkbutton(self.root,text="Collisions", variable=self.collisions, onvalue=0, offvalue=1)
        self.load_button.grid(row=1,column=0,sticky=W)
        
        self.root.mainloop()
        
    def apply(self):
        
        if str(self.nb.get()).isdigit():
            global atomNb
            global collisionNotActive
            collisionNotActive = self.collisions.get()
            atomNb = int(str(self.nb.get()))
            self.root.destroy()
        

    def quit(self):
        self.root.destroy()
        sys.exit(0)

class Menu:
    def __init__(self, game):
        self.root = Toplevel(takefocus = 1)
        #self.root.overrideredirect(1)
        self.game = game
        
        self.instruction = Label(self.root,text="Menu")
        self.instruction.grid(row=0,column=0,columnspan=1,sticky=W)
        
        self.quit_button = Button(self.root,text="Quit", command=self.game.quit)
        self.quit_button.grid(row=1,column=0,sticky=W)
        
        self.ok_button = Button(self.root,text="Close", command=self.apply)
        self.ok_button.grid(row=0,column=1,sticky=W)
        
    def apply(self):
        #self.root.config(takefocus = 0)
        self.root.destroy()
    
    
class Graph:
    def __init__(self, game):
        self.root = Toplevel()
        self.root.title('Graphique')
        #self.root.overrideredirect(1)
        global atomNb
        self.atomNb = atomNb
        self.game = game
        self.width = 700
        self.height = 300
        self.canvas= Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0, background='dark turquoise')
        self.canvas.pack()
        self.counter = 0
        self.oldCounter = self.counter
        self.number = self.height-(self.game.atoms*self.height/self.atomNb)
        
        self.timeSinceUpdate = self.game.timeSinceUpdate
        
    def update(self):
        self.timeSinceUpdate = self.game.timeSinceUpdate
        
        self.oldNumber = self.number
        self.number = self.height-(self.game.atoms*self.height/self.atomNb)
        self.canvas.create_line(self.oldCounter, self.oldNumber, self.counter, self.number, fill='black')
        self.oldCounter = self.counter
        self.counter += self.timeSinceUpdate*10
        self.root.update_idletasks()
        self.root.update()
        

class Game:
    def __init__(self, collisionsNotActive):
        self.tk = Tk()
        self.tk.title("Desintegration radiocative")
        #self.tk.resizable(0, 0)
        self.tk.wm_attributes("-fullscreen", 1)
        self.width = 1920
        self.height = 1080
        self.canvas= Canvas(self.tk, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.collisionsNotActive = collisionsNotActive
        self.view = [0.0, 0.0]
        self.zoom = 5
        self.freezeTime = False
        self.test = time.time()
        self.stime = time.time()
        self.bg = PhotoImage(file="images/background.gif")
        self.fps = self.canvas.create_text(15,15, text="test", fill ='white')
        print(time.time()-self.test)
        self.framerate = 60
        
        self.deathProbability = 0.1
        
        
        self.mapActive = False
        self.normalZoom = 10.0
        self.mapWaitTime = time.time()
        
        self.platform = platform.system()
        
        self.timeSinceUpdate = time.time()
        self.timeSinceUpdateCounter = time.time()
        
        self.entities = []
        global atomNb
        self.atoms = atomNb
        self.infunction = True
        
        self.bgimage = self.canvas.create_image(0, 0, image=self.bg, anchor='nw')
      
        self.menuButton = Label(self.canvas, text="Menu", fg='dark sea green', font=('Monospaced',25), bg= 'black')
        self.menuButton.bind("<Button-1>", self.showMenu)
        self.menuWindow = self.canvas.create_window(self.width/2, 13, window=self.menuButton)
        
        self.canvas.bind_all('<BackSpace>', self.freeze)
        
    
    def quit(self):
        self.tk.destroy()
        sys.exit(0)
    
    def showMenu(self, evt):
        menu = Menu(self)
    
    def freeze(self, evt):
        if self.freezeTime == True:
            self.freezeTime = False
        else:
            self.freezeTime = True
    
    def collisions(self):
         for entity1 in self.entities:
            if type(entity1) == Cursor:
                continue
            for entity2 in self.entities:
                if type(entity2) == Cursor or entity2 == entity1:
                    continue
                if hypot(entity1.center[0]-entity2.center[0], entity1.center[1]-entity2.center[1])>=6:
                    continue
                if hypot(entity1.center[0]-entity2.center[0], entity1.center[1]-entity2.center[1]) <= entity2.radius + entity1.radius:
                    entity1.touch(entity2)
                

    def gameLoop(self):
        global graph
        self.graph = graph
        global atomNb
        self.atoms = atomNb
        
        while self.infunction == True:
            self.timeSinceUpdate = time.time() - self.timeSinceUpdateCounter
            self.timeSinceUpdateCounter = time.time()
            #self.renderDistance = hypot(-self.width/self.zoom +self.view[0], -self.height/self.zoom +self.view[1])
            
            self.stime = time.time()
            
            for entity in self.entities:
                if random.random()/self.timeSinceUpdate<=self.deathProbability:
                    color = '#%02x%02x%02x' % (random.randint(50,255), random.randint(50,255), random.randint(50,255))
                    self.canvas.itemconfigure(entity.id, fill = color, outline = color)
                    self.atoms -= 1
                    self.entities.remove(entity)
                    
            """
            if self.freezeTime == False:
                for entity in self.entities:
                    entity.update()
                if self.collisionsNotActive == 0:
                    self.collisions()
            """
            if self.tk.winfo_width() != self.width:
                self.width = self.tk.winfo_width()
                self.canvas.coords(self.menuWindow, self.width/2, 13)
        
            self.height = self.tk.winfo_height()
            self.canvas.lift(self.fps)
            self.tk.update()
            self.graph.update()
            
            self.waitTime = time.time() - self.stime
            time.sleep(max(1/self.framerate - self.waitTime, 0))
            self.stime = time.time() - self.stime
            self.canvas.itemconfigure(self.fps, text=str(int(1/self.stime)))
            


class Entity:
    def __init__(self, game, x=0.0, y=0.0, events = []):
        self.x = x
        self.y = y
        self.speed = None
        self.game = game
        self.coords = None
        self.canvas = self.game.canvas
        self.id = None
        self.removed = False
        self.timeSinceUpdate = time.time()
        self.events = events
        self.redraw = True
    
    def update(self):
        pass
    
    def processEvents(self):
        for event in self.events:
            if event[0] <= time.time():
                if type(event[1]) is list:
                    for subevent in event[1]:
                        exec(subevent)
                    self.events.remove(event)
                else:
                    exec(event[1])
                    self.events.remove(event)
    
    

class Cursor(Entity):
    def __init__(self, game,
                x = 0.0,
                y = 0.0,
                center = [0.0, 0.0],
                events = []):
        
        Entity.__init__(self, game, x, y, events = events)
        self.canvas = self.game.canvas
        self.center = center
        self.forward = False
        self.left = False
        self.right = False
        self.spaceBreak = False
     
        game.canvas.bind_all('<KeyPress-Left>', self.pLeft)
        game.canvas.bind_all('<KeyPress-Right>', self.pRight)
        game.canvas.bind_all('<KeyPress-Up>', self.pForward)
        game.canvas.bind_all('<KeyPress-Down>', self.pBreak)
        
        game.canvas.bind_all('<KeyRelease-Left>', self.rLeft)
        game.canvas.bind_all('<KeyRelease-Right>', self.rRight)
        game.canvas.bind_all('<KeyRelease-Up>', self.rForward)
        game.canvas.bind_all('<KeyRelease-Down>', self.rBreak)
        
        game.canvas.bind_all('<Shift-Left>', self.zoomP)
        game.canvas.bind_all('<Shift-Right>', self.zoomM)
        
        
    def zoomP(self, evt):
        if self.game.zoom < 100:
            self.game.zoom  += 1.0
        
    def zoomM(self, evt):
        if self.game.zoom >1:
            self.game.zoom -= 1.0
        
    def pLeft(self, evt):
        self.left = True
        
    def pRight(self, evt):
        self.right = True
        
    def pForward(self, evt):
        self.forward = True
        
    def pBreak(self, evt):
        self.spaceBreak = True
        
    
    def rLeft(self, evt):
        self.left = False
        
    def rRight(self, evt):
        self.right = False
        
    def rForward(self, evt):
        self.forward = False
        
    def rBreak(self, evt):
        self.spaceBreak = False


    def update(self):
        
        self.timeSinceUpdate = time.time() - self.timeSinceUpdate
        self.timeSinceUpdate *= 30
        
        
        self.oldCenter = self.center
        
        if self.events != []:
            self.processEvents()
            
        if self.left:
            self.x = -1
            
        if self.right:
            self.x = 1
            
        if self.forward:
            self.y = -1
            
        if self.spaceBreak:
            self.y = 1
        
        self.center[0] += self.x * self.timeSinceUpdate
        self.center[1] += self.y * self.timeSinceUpdate
        self.game.view = self.center
        
        self.x = 0
        self.y = 0
        
        self.timeSinceUpdate = time.time()
    
    

class Atom(Entity):
    def __init__(self, game,
                time = time.time(),
                events = []):
        
        Entity.__init__(self, game, events = events)
        self.canvas = self.game.canvas
        #self.timeSinceUpdate = self.game.timeSinceUpdate
        if random.randint(0,9) == 0:
            self.center = [random.randint(-100,100), random.randint(-100,100)]
            #self.oldCenter = self.center
            self.radius = random.random()*3
            self.x = (random.random()-0.5)*2
            self.y = (random.random()-0.5)*2
            #self.deathProbability = 0.1
            self.color = "white"
            self.coords = [self.center[0]-self.radius, self.center[1]-self.radius, self.center[0]+self.radius, self.center[1]+self.radius]
            self.wCoords = ctw(self.coords, self.game.view, self.game.zoom)
            self.id = self.canvas.create_oval(self.wCoords[0], self.wCoords[1], self.wCoords[2], self.wCoords[3], fill = self.color, outline = self.color)
        
    def touch(self, entity):
        velocity = normalise([self.center[0], self.center[1], entity.center[0], entity.center[1]])
        entity.center = entity.oldCenter
        entity.center[0] += velocity[0] * 0.2
        entity.center[1] += velocity[1] * 0.2
        self.center[0] += -velocity[0] * 0.2
        self.center[1] += -velocity[1] * 0.2
        entity.x = velocity[0]
        entity.y = velocity[1]
        self.x = -velocity[0]
        self.x = -velocity[1]
        
    
    def update(self):
        
        self.timeSinceUpdate = self.game.timeSinceUpdate
        
        if random.random()/self.timeSinceUpdate<=self.deathProbability:
            delete(self)
        
        self.oldCenter = self.center
        
        self.center[0] += self.x * self.timeSinceUpdate
        self.center[1] += self.y * self.timeSinceUpdate
        
        self.coords = [self.center[0]-self.radius, self.center[1]-self.radius, self.center[0]+self.radius, self.center[1]+self.radius]
        
        self.wCoords = ctw(self.coords, self.game.view, self.game.zoom)
        
        self.distance = hypot(self.center[0]-self.game.view[0], self.center[1]-self.game.view[1])
        if self.distance <= self.game.renderDistance + self.radius:
            self.canvas.coords(self.id, self.wCoords[0], self.wCoords[1], self.wCoords[2], self.wCoords[3])
        
        self.timeSinceUpdate = time.time()
 
 
"""
Start Application
"""
atomNb = 100
collisionActive = 1

settings = Settings()
game = Game(collisionNotActive)
graph = Graph(game)

for i in range(1,atomNb):
    game.entities.append(Atom(game))
game.entities.append(Cursor(game))

game.gameLoop()
