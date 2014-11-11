from __future__ import division
from visual import *
from random import Random

r = Random()


def Collision( A, B ):
    Ap = A.p
    Bp = B.p
    Amass = A.mass
    Bmass = B.mass
    Tmass = Amass + Bmass
    pcm = Ap + Bp
    cosAB = Ap.dot( Bp ) / ( Ap.mag * Bp.mag )
    cosB  = r.uniform(-1,1)
    print 'cosB', cosB

    Bout  = pcm.mag2 * cosB**2 / Amass**2
    Bout += 4 * Bp.mag2 * ( Bmass**-2 - Amass**-2 )
    Bout -= 4 * Ap.mag * Bp.mag / Amass * ( Amass**-1 + Bmass**-1) * cosAB
    Bout  = 0.5 * Amass * Bmass / Tmass * Bout**.5
    Bout -= 0.5 * Bmass * pcm.mag * cosB / Tmass

    print 'Bout',Bout


Ap = vector(1, 1,0)
Bp = vector(1,-1,0)

A = sphere( pos = (0,0,0), p = Ap, mass=  1. )
B = sphere( pos = (0,0,0), p = Bp, mass=  1. )

for i in range(1000):
    Collision(A,B)