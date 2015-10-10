import visual as vs
import wx
import random

_kB  = 1.3806488e-23   # Boltzman constant in J/K
_amu = 1.660538921e-27 # atomic mass unit to kg conversion

_r = random.Random()
def random_position():
    lim = l/2 - radius
    rand = lambda: _r.uniform(-lim,lim)
    return vs.vector( rand(), rand(), rand() )

def random_direction():
    x = _r.gauss(0,1)
    y = _r.gauss(0,1)
    z = _r.gauss(0,1)
    n = ( x**2 + y**2 + z**2 )**0.5
    return vs.vector( x/n, y/n, z/n )

def V2T(ball):
    return ball.p.mag2/(3*_kB*m)

def T2V(t):
    return (3*_kB*t/m)**0.5

def SetVelocity(evt):
    T = slider.GetValue()
    print T
    for b in balls:
        b.p *= T/V2T(b)


L = 320
w = vs.window( width  = 2 * ( L + vs.window.dwidth ),
               height = L + vs.window.dheight + vs.window.menuheight,
               menus  = True, title = 'Widgets' )
w.autoscale = False

# Place a 3D display widget in the left half of the window.
d = 20
vs.display( window  = w, x = d, y = d,
            width   = L - 2 * d, height = L - 2 * d,
            range  = 200.,
            forward = - vs.vector( 0, 0, 1 ) )

# Place buttons, radio buttons, a scrolling text object, and a slider
# in the right half of the window. Positions and sizes are given in
# terms of pixels, and pos(0,0) is the upper left corner of the window.
panel = w.panel # Refers to the full region of the window in which to place widgets

slider = wx.Slider( panel,
                    pos = ( L, 0.8 * L ), size = ( 0.9 * L, 20 ),
                    minValue = 1, maxValue = 10000 )
slider.Bind( wx.EVT_SCROLL, SetVelocity )
slider.SetValue(300.)
wx.StaticText( panel, pos = ( L, 0.75*L ), label = 'Set temperature' )


N = 10
l = 200.0
m = 131.293 * _amu
radius = l*0.05
box  = vs.box( pos = (0,0,0), length=l, height=l, width=l, opacity=0.1, color=vs.color.white)
balls = [ vs.sphere(
pos = random_position(),
p = m * T2V(slider.GetValue()) * random_direction(),
radius = radius,
color = vs.color.red,
mass = m )
for i in range(N) ]


dt = 1e-3
while True:
    vs.rate(100)
    for b in balls:
        b.pos += b.p/b.mass * dt
        if abs(b.x) > l/2 - radius:
            b.p.x *= -1
        if abs(b.y) > l/2 - radius:
            b.p.y *= -1
        if abs(b.z) > l/2 - radius:
            b.p.z *= -1
