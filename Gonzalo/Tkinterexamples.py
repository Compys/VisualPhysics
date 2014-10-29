
import Tkinter


mainwindow = Tkinter.Tk( screenName = 'MainWindow' )
leftclick  = '<1>'

def HelloWorld():
    text       = Tkinter.Label( mainwindow, text = 'Hello world!' )
    text.pack()
    mainwindow.mainloop()

def HelloWorldWithClasses():
    class App:
        def __init__(self, master):
            frame = Tkinter.Frame(master)
            frame.pack()
            
            self.button = Tkinter.Button( frame, text = "QUIT", fg = "red",
                                          command = frame.quit )
            self.button.pack(side = Tkinter.LEFT)

            self.hi_there = Tkinter.Button(frame, text="Hello",
                                           command=self.say_hi)
            self.hi_there.pack(side=Tkinter.LEFT)
        
        def say_hi(self):
            print "hi there, everyone!"

    app = App(mainwindow)
    mainwindow.mainloop()

def clicking():
    def printclicked(mouse):
        print "clicked at", mouse.x, mouse.y
    
    frame = Tkinter.Frame( mainwindow, width=1000, height=1000)
    frame.bind( leftclick, printclicked )
    frame.pack()
    mainwindow.mainloop()

#HelloWorld()
HelloWorldWithClasses()
#clicking()


