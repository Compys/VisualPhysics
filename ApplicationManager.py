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
    from math import log
    app = AppManager('trial',autoscale = False, range = 3)
    R   = random.Random()
    Npart = 20
    dt    = 1e-6
    app.Add( 'box', 'box',
             pos = (0.,0.,0.),
             length = 2, height = 2, width = 2,
             color = visual.color.orange, opacity = 0.2 )
    v = 100
    for n in range( Npart ):
        app.Add( 'sphere', 'sphere' + str(n),
                 pos = visual.vector( [R.uniform(-1,1) for i in range(3)] ),
                 p   = visual.vector( [ R.gauss(v,v**.5) * R.choice([-1,1]) for i in range(3)] ),
                 radius = 0.05)
    
    def Force( i ):
        Fi  = visual.vector(0.,0.,0.)
        parti = app.Get( 'sphere' + str(i) )
        for j in range(Npart):
            if i == j: continue
            partj = app.Get( 'sphere' + str(j) )
            dr2 = 1.0 / ( parti.pos - partj.pos ).mag2**4
            Fi += ( 2.*dr2**2 - dr2 ) * ( parti.pos - partj.pos )
        Fi *= 24
        return Fi

    while True:
        visual.rate(200)
        F = range(Npart)
        for i in range(Npart):
            sph = app.Get( 'sphere' + str(i) )

            F[i] = Force(i)
        
        for i in range(Npart):
            sph = app.Get( 'sphere' + str(i) )
            sph.p += F[i] * dt
            sph.pos += sph.p * dt

            if abs(sph.x) > 0.95:
                sph.p.x *= -1
            if abs(sph.y) > 0.95:
                sph.p.y *= -1
            if abs(sph.z) > 0.95:
                sph.p.z *= -1
            if sph.p.mag > 1e13:
                sph.p *= sph.p.mag**.5



