from __future__ import division
import ROOT
import math
import Plots

R = ROOT.TRandom3(0)

def mean(x):
    return sum(x)/len(x)

def RMS( x, xm ):
    return math.sqrt( sum( map( lambda xi: (xi - xm)**2, x ) ) / len(x) )

def URandom( N = 1000 ):
    return [ R.Uniform(-1,1) for i in xrange(N) ]

def GRandom( N = 1000, sigma = 2.5 ):
    return [ R.Gaus(0,sigma) for i in xrange(N) ]

def Experiment( N = 1000, random = URandom ):
    points  = random( N )
    meanval = mean(points)
    rmsval  = RMS( points, meanval )
    return meanval, rmsval


Nexp = int(1e5)

hm = [ROOT.TH1F('uniform mean ' + str(i+1), 'uniform', 200, -1, 1 ) for i in range(10) ]
hr = [ROOT.TH1F('uniform rms  ' + str(i+1), 'uniform', 200,  0, 1 ) for i in range(10) ]

for i in xrange(Nexp):
    for Nrandom in range(10):
        m, rms = Experiment( 1 + Nrandom, URandom )
        hm[Nrandom].Fill( m )
        hr[Nrandom].Fill( rms )

cm = Plots.PutInCanvas(hm)
cr = Plots.PutInCanvas(hr)

