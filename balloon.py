import visual as vs
import wx

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

balloon = vs.sphere( radius = 1., color = vs.color.red )

def SetBalloonRadius(evt):
    balloon.radius = slider.GetValue()

def PumpBalloon(evt):
    balloon.radius *= 1.1

def PunctureBalloon(evt):
    balloon.radius = 1.

# Place buttons, radio buttons, a scrolling text object, and a slider
# in the right half of the window. Positions and sizes are given in
# terms of pixels, and pos(0,0) is the upper left corner of the window.
panel = w.panel # Refers to the full region of the window in which to place widgets

pump = wx.Button( panel, label = 'Pump', pos = ( L + 10, 15 ) )
pump.Bind( wx.EVT_BUTTON, PumpBalloon )

puncture = wx.Button( panel, label = 'Puncture', pos = ( L + 210, 15 ) )
puncture.Bind( wx.EVT_BUTTON, PunctureBalloon )


slider = wx.Slider( panel,
                    pos = ( L, 0.8 * L ), size = ( 0.9 * L, 20 ),
                    minValue = 0, maxValue = 100 )
slider.Bind( wx.EVT_SCROLL, SetBalloonRadius )
slider.SetValue(10.)
wx.StaticText( panel, pos = ( L, 0.75*L ), label = 'Set balloon radius' )

while True:
    vs.rate(100)
