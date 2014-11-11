'''
    Main application of the package. It displays a set of physics fields,
    each one containing a bunch of examples of that field.
'''

import Tkinter

class Application( Tkinter.Tk ):
    '''
        To be implemented???: a class for using the window also as a container.
    '''
    def __init__( self, name, **kargs ):
        Tkinter.Tk.__init__( self, screenName = name )
        self.elements = {}
        for k in kargs:
            exec( 'self.configure( {0} = {1} ) )'.format( k, kargs[k] ) )

    def AddButton( name, **kargs ):
        button = Tkinter.Button( self, **kargs )
        self.elements[name] = button

def Calling(arg):
    '''
        Dummy printing
    '''
    print 'Calling ' + arg

def CheckSelection():
    '''
        Check the selected option and behave accordingly to it.
    '''
    
    if ProgramSelectorG.get() != GravityExamples[0]:
        Calling( ProgramSelectorG.get() )

    elif ProgramSelectorEM.get() != ElectromagnetismExamples[0]:
        Calling( ProgramSelectorEM.get() )

    elif ProgramSelectorTD.get() != ThermodynamicsExamples[0]:
        Calling( ProgramSelectorTD.get() )

    elif ProgramSelectorOP.get() != OpticsExamples[0]:
        Calling( ProgramSelectorOP.get() )

    elif ProgramSelectorQM.get() != QuantumMechanicsExamples[0]:
        Calling( ProgramSelectorQM.get() )


# Create a new window
MainWindow = Tkinter.Tk( screenName = 'VisualPhysics' )
MainWindow.configure( bg = 'black' )

# Load and insert logo
photofile = Tkinter.PhotoImage( file = "pylogo.gif"  )
photo = Tkinter.Label( MainWindow, image = photofile )
photo.config( height = 175, width = 175 )
photo.pack( side = Tkinter.RIGHT )

# Label for each field
GravityExamples          = ['Gravity']
ElectromagnetismExamples = ['Electromagnetism']
ThermodynamicsExamples   = ['Thermodynamics']
OpticsExamples           = ['Optics']
QuantumMechanicsExamples = ['Quantum mechanics']

# Examples for each field
GravityExamples += ['Solar system','Moon']
ElectromagnetismExamples += ['Dipole']

# Variables
ProgramSelectorG  = Tkinter.StringVar( MainWindow ); ProgramSelectorG .set(GravityExamples[0])
ProgramSelectorEM = Tkinter.StringVar( MainWindow ); ProgramSelectorEM.set(ElectromagnetismExamples[0])
ProgramSelectorTD = Tkinter.StringVar( MainWindow ); ProgramSelectorTD.set(ThermodynamicsExamples[0])
ProgramSelectorOP = Tkinter.StringVar( MainWindow ); ProgramSelectorOP.set(OpticsExamples[0])
ProgramSelectorQM = Tkinter.StringVar( MainWindow ); ProgramSelectorQM.set(QuantumMechanicsExamples[0])

# Option menus
Gravity          = Tkinter.OptionMenu( MainWindow, ProgramSelectorG , *GravityExamples          )
Electromagnetism = Tkinter.OptionMenu( MainWindow, ProgramSelectorEM, *ElectromagnetismExamples )
Thermodynamics   = Tkinter.OptionMenu( MainWindow, ProgramSelectorTD, *ThermodynamicsExamples   )
Optics           = Tkinter.OptionMenu( MainWindow, ProgramSelectorOP, *OpticsExamples           )
QuantumMechanics = Tkinter.OptionMenu( MainWindow, ProgramSelectorQM, *QuantumMechanicsExamples )

# A button to run the selected option
GoButton = Tkinter.Button( MainWindow, bg = 'red', text = 'GO!', command = CheckSelection )


# Sizes configuration
wdt = 20
GoButton.config( width = wdt - 2 )
Gravity.config( width = wdt )
Electromagnetism.config( width = wdt )
Thermodynamics.config( width = wdt )
Optics.config( width = wdt )
QuantumMechanics.config( width = wdt )

# Packing
GoButton.pack()
Gravity.pack()
Electromagnetism.pack()
Thermodynamics.pack()
Optics.pack()
QuantumMechanics.pack()

# Mainloop
MainWindow.mainloop()



