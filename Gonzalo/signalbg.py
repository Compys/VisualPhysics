from __future__ import division
import ROOT
import math

R  = ROOT.TRandom3(0)
B  = lambda: R.Uniform(-10,10)
B  = lambda: -10 + R.Exp(7)
S1 = lambda: R.Gaus(0.,.30)
S2 = lambda: R.Gaus(1.,.15)

significance = 2
nbg     = 10000
nsignal = 0.5 * significance**2 * ( 1 + math.sqrt( 1 + 4*nbg ) )
nsignal = int(nsignal)

def Generate():
    return [ B() for i in range(nbg) ] + [ S1() for i in range(nsignal) ] + [ S2() for i in range(nsignal//10) ]

h = ROOT.TH1D('sig+bg','sig+bg',200,-10,10)
f = ROOT.TF1('fit','[0] * exp(-(x-[1])^2/(2*[2]^2))+[3] * exp(-(x-[4])^2/(2*[5]^2))+[6]*exp(-(x-[8])/[7])')
f.SetParameters( nsignal/math.sqrt(2*math.pi), 0., .30,
             0.1*nsignal/math.sqrt(2*math.pi), 1., .15,
                 nbg/20, 7.,10)
f.SetNpx(5000)

f.SetParLimits( 0, 0, nsignal )
f.SetParLimits( 1, -3, 3 )
f.SetParLimits( 2, 0, 2 )
f.SetParLimits( 3, 0, nsignal/8 )
f.SetParLimits( 4, 0, 5 )
f.SetParLimits( 5, 0, 2 )
f.SetParLimits( 6, 0, nbg )
f.SetParLimits( 7, 0, 10 )
f.SetParLimits( 8, 0, 20 )

for i in Generate():
    h.Fill(i)
h.Fit(f)

