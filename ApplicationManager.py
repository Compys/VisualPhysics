'''
    Define AppManager class.
'''

import visual

class AppManager:
    '''
        Base class with general options of a visual interface.
    '''
    def __init__( self, title, **options ):
        default = { 'x' : 0, 'y' : 0,
                    'width' : 800, 'height' : 600,
                    'center' : (0,0,0),
                    'autoscale' : True,
                    'forward' : (0, 0, -1 ) }

        for opt in default:
            if not opt in options:
                options[opt] = default[opt]

        self.simu = visual.display( title = title, **options )
        self.objects = {}

    def Add( self, object, name, **options ):
        '''
            Add some object.
        '''
        exec( "self.objects[name] = visual.{0}(**options)".format(object) )

    def Get( self, name ):
        return self.objects.get(name)

if __name__ == '__main__':
    import random
    app = AppManager('trial')
    R   = random.Random()
    Npart = 20
    dt    = 3e-6
    app.Add( 'box', 'box',
             pos = (0.,0.,0.),
             length = 2, height = 2, width = 2,
             color = visual.color.orange, opacity = 0.2 )

    for n in range( Npart ):
        app.Add( 'sphere', 'sphere' + str(n),
                 pos = visual.vector( [R.uniform(-1,1) for i in range(3)] ),
                 p   = visual.vector( [R.uniform(-1,1) for i in range(3)] ),
                 radius = 0.05)

    def LJ( p1, p2 ):
        dir = ( p1.pos - p2.pos ).norm()
        r2 = 1. / ( p1.pos - p2.pos ).mag2
        return (r2**6 - r2**3) * dir

    def V( i ):
        pot  = visual.vector(0.,0.,0.)
        part = app.Get( 'sphere' + str(i) )
        for j in range(Npart):
            pot += LJ( part, app.Get( 'sphere' + str(j) ) ) if i != j else visual.vector(0.,0.,0.)

        return pot

    while True:
        visual.rate(200)
        for i in range(Npart):
            sph = app.Get( 'sphere' + str(i) )

            F = V(i)
            sph.p += F * dt
            sph.pos += sph.p * dt

            if abs(sph.x) > 0.95:
                sph.p.x *= -1
            if abs(sph.y) > 0.95:
                sph.p.y *= -1
            if abs(sph.z) > 0.95:
                sph.p.z *= -1


