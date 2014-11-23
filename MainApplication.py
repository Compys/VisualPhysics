'''
    Main application of the package. It displays a set of physics fields,
    each one containing a bunch of examples.
    
    @Author: Gonzalo M.
    @Date: 23/11/2014
'''

import Tkinter

class Application( Tkinter.Tk ):
    '''
        Redefine Tkinter's Tk class in order to use contain every object associated to it.
    '''
    def __init__( self, name, **kargs ):
        Tkinter.Tk.__init__( self, screenName = name )
        self.elements = {}
        for k in kargs:
            exec( 'self.configure( {0} = {1} ) )'.format( k, kargs[k] ) )
        
        self.update()

    def Add( self, kind, name, *args, **kargs ):
        '''
            Add a widget of specified kind.
        '''
        if args:
            exec( "self.elements['{1}'] = Tkinter.{0}( self, *args, **kargs )".format(kind,name))
        else:
            exec( "self.elements['{1}'] = Tkinter.{0}( self, **kargs )".format(kind,name))

    def Get( self, name ):
        '''
            Return element identified named name.
        '''
        return self.elements.get( name )
    
    def GetValue( self, name ):
        '''
            Return current value of some element named name. It must be a variable (and have a get method).
        '''
        return self.Get( name ).get()

    def Pack( self, name, **packing_opt ):
        '''
            Pack widget named @name.
        '''
        self.elements[name].pack( **packing_opt )
    
    def Size( self ):
        '''
            Get size of the application.
        '''
        return tuple(int(npx) for npx in self.geometry().split('+')[0].split('x'))

    def Resize( self, width, height ):
        '''
            Change dimensions.
        '''
        self.geometry( '{0}x{1}'.format( width, height ) )
        self.update()

    def Repos( self, xpos, ypos ):
        '''
            Change position on screen.
        '''
        self.geometry( '+{0}+{1}'.format( xpos, ypos ) )
        self.update()

    def Center( self ):
        '''
            Center application on screen.
        '''
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        xsize, ysize = self.Size()
        x = w/2 - xsize/2
        y = h/2 - ysize/2
        self.Repos( x, y )

def Calling(arg):
    '''
        Dummy printing
    '''
    print 'Calling ' + arg

def CheckSelection():
    '''
        Check the selected option and behave accordingly to it.
    '''
    
    if MainWindow.GetValue('gravity_var') != Gravity_labels[0]:
        Calling( MainWindow.GetValue('gravity_var') )

    elif MainWindow.GetValue('electro_var') != Electromagnetism_labels[0]:
        Calling( MainWindow.GetValue('electro_var') )

    elif MainWindow.GetValue('thermo_var') != Thermodynamics_labels[0]:
        Calling( MainWindow.GetValue('thermo_var') )

    elif MainWindow.GetValue('optics_var') != Optics_labels[0]:
        Calling( MainWindow.GetValue('optics_var') )

    elif MainWindow.GetValue('quantum_var') != QuantumMechanics_labels[0]:
        Calling( MainWindow.GetValue('quantum_var') )


# Create a new window
MainWindow = Application( 'VisualPhysics' )
MainWindow.Resize( 600, 300 )
MainWindow.Center()

# Load and insert logo
photofile = Tkinter.PhotoImage( file = 'pylogo.gif'  )
MainWindow.Add( 'Label', 'logo', image = photofile, height = 300, width = 300 )
MainWindow.Pack( 'logo', side = Tkinter.RIGHT )

# Now we want to create a number of sections for our physics examples.

# Label for each field
Gravity_labels          = ['Gravity']
Electromagnetism_labels = ['Electromagnetism']
Thermodynamics_labels   = ['Thermodynamics']
Optics_labels           = ['Optics']
QuantumMechanics_labels = ['Quantum mechanics']

# We can add a few examples for each field
Gravity_labels          += ['Solar system','Moon']
Electromagnetism_labels += ['Dipole']

# Create variables
MainWindow.Add( 'StringVar', 'gravity_var', Gravity_labels[0]          )
MainWindow.Add( 'StringVar', 'electro_var', Electromagnetism_labels[0] )
MainWindow.Add( 'StringVar', 'thermo_var' , Thermodynamics_labels[0]   )
MainWindow.Add( 'StringVar', 'optics_var' , Optics_labels[0]           )
MainWindow.Add( 'StringVar', 'quantum_var', QuantumMechanics_labels[0] )

# Add option menus to Main window
MainWindow.Add( 'OptionMenu', 'Gravity', MainWindow.Get('gravity_var'), *Gravity_labels          )
MainWindow.Add( 'OptionMenu', 'Electro', MainWindow.Get('electro_var'), *Electromagnetism_labels )
MainWindow.Add( 'OptionMenu', 'Thermo' , MainWindow.Get('thermo_var' ), *Thermodynamics_labels   )
MainWindow.Add( 'OptionMenu', 'Optics' , MainWindow.Get('optics_var' ), *Optics_labels           )
MainWindow.Add( 'OptionMenu', 'Quantum', MainWindow.Get('quantum_var'), *QuantumMechanics_labels )

# Add a button to run the selected option
MainWindow.Add( 'Button', 'GO', text = 'GO!', command = CheckSelection )

# Packing
[ MainWindow.Pack( name, fill = Tkinter.X ) for name in [ 'GO', 'Gravity', 'Electro', 'Thermo', 'Optics', 'Quantum' ] ]

# Mainloop
MainWindow.mainloop()



