import visual
import Geometry

class Colors:
    black   = ( 0.0, 0.0, 0.0 )
    red     = ( 1.0, 0.0, 0.0 )
    green   = ( 0.0, 1.0, 0.0 )
    blue    = ( 0.0, 0.0, 1.0 )
    yellow  = ( 1.0, 1.0, 0.0 )
    cyan    = ( 0.0, 1.0, 1.0 )
    magenta = ( 1.0, 0.0, 1.0 )
    white   = ( 1.0, 1.0, 1.0 )
    gray    = ( 0.5, 0.5, 0.5 )
    orange  = ( 1.0, 0.5, 0.0 )
    
    @staticmethod
    def Complementary( color ):
        return tuple( visual.vector( Colors.white ) - visual.vector( color ) )
    
    @staticmethod
    def Select( color0 = white, opacity0 = 1, x_window = 0, y_window = 0 ):
        L = 1.  # box size = bar length
        R = L/8 # ball radius
        
        scene = visual.display( title = 'Select color',
                                x = x_window, y = y_window,
                                width = 600, height = 400,
                                center = 2.5 * Geometry.xaxis + Geometry.yaxis,
                                autoscale = True,
                                autocenter = False,
#                                userspin  = False,
                                userzoom  = False,
                                forward   = -Geometry.zaxis)
        
        sample = visual.box( pos = 3 * L * Geometry.xaxis + L * Geometry.yaxis,
                             length = L, height = L, width = L,
                             color = color0, opacity = opacity0 )
                             
        hidden = visual.sphere( pos = sample.pos - (0,0,sample.width),
                                radius = R,
                                color = Colors.Complementary( color0 ), opacity = 1 )

        red_bar = visual.cylinder( pos = (0,0,0),
                                   axis = Geometry.yaxis * L * 2,
                                   radius = R,
                                   color = Colors.red )

        green_bar = visual.cylinder( pos = (L/2,0,0),
                                     axis = Geometry.yaxis * L * 2,
                                     radius = R,
                                     color = Colors.green )

        blue_bar = visual.cylinder( pos = (L,0,0),
                                    axis = Geometry.yaxis * L * 2,
                                    radius = R,
                                    color = Colors.blue )
                                    
        white_bar = visual.cylinder( pos = 2.5 * L * Geometry.xaxis ,
                                    axis = Geometry.xaxis * L * 2,
                                    radius = R,
                                    color = Colors.white )

        red_ball = visual.sphere( pos = visual.vector(red_bar.pos) + (0,2*color0[0],0),
                                  radius = L/4,
                                  color = Colors.red )

        green_ball = visual.sphere( pos = visual.vector(green_bar.pos) + (0,2*color0[1],0),
                                    radius = L/4,
                                    color = Colors.green )

        blue_ball = visual.sphere( pos = visual.vector(blue_bar.pos) + (0,2*color0[2],0),
                                   radius = L/4,
                                   color = Colors.blue )

        white_ball = visual.sphere( pos = visual.vector(white_bar.pos) + (2*opacity0,0,0),
                                    radius = L/4,
                                    color = Colors.white )

        ok_button = visual.cylinder( pos    = 5 * L * Geometry.xaxis + Geometry.yaxis,
                                     axis   = -Geometry.zaxis * 1e-2,
                                     radius = 3 * R,
                                     color  = Colors.red )
                                     
        ok_text   = visual.text    ( text   = 'OK', pos = ok_button.pos + Geometry.zaxis * 1e-3,
                                     height = R, depth = 1e-3,
                                     align = 'center', font = 'Times',
                                     color  = Colors.white )


        def ChangeColor( click, ball ):
            if ball is white_ball:
                x0 = white_bar.pos[0]
                x1 = x0 + white_bar.axis[0]
                x = (click.pos[0] - x0)/2
                ball.pos[0] = x0 if x < 0 else x0 + 2*x if 2*x < x1 - x0 else x1
                sample.opacity = x
                return
            
            y = click.pos[1]/2
            ball.pos[1] = 0 if y < 0 else 2*y if y < 1 else 2.
            sample.color = ( red_ball.y / 2, green_ball.y / 2, blue_ball.y / 2 )
            hidden.color = Colors.Complementary( sample.color )
        
        
        while True:
            ball = None
            click = scene.waitfor('mousedown')
            if   (click.pos -   red_ball.pos).mag < 2*R:
                ball = red_ball
            elif (click.pos - green_ball.pos).mag < 2*R:
                ball = green_ball
            elif (click.pos -  blue_ball.pos).mag < 2*R:
                ball = blue_ball
            elif (click.pos -  white_ball.pos).mag < 2*R:
                ball = white_ball
            elif ( click.pos - ok_button.pos).mag < ok_button.radius:
                break
            
            if ball:
                scene.bind( 'mousemove', ChangeColor, ball )
                unclick = scene.waitfor( 'mouseup' )
                scene.unbind( 'mousemove', ChangeColor )

        return sample.color

__all__ = ['Colors']

print Colors.Select()