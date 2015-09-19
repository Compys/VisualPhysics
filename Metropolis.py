from random import Random
from math import pi, exp

_k   = 1.3806488e-23   # Boltzman constant in J/K
_amu = 1.660538921e-27 # atomic mass unit to kg conversion

class Metropolis:
    '''
        Generate random numbers according to a given pdf.
    '''
    def __init__(self, pdf, xlow = 0, xupp = 1, sigma = None, rng = Random() ):
        self.pdf = pdf
        self.low = xlow
        self.upp = xupp

        self.x0  = self._Mean()
        self.sig = 0.1 * self.x0 if sigma is None else sigma

        self.rng = rng
        self.x1 = self.x0
        self.f1 = self.pdf(self.x0)

    def _Mean(self):
        dx = ( self.upp - self.low ) * 1e-5
        xv = [ self.low + i * dx for i in xrange(int(1e5)) ]
        yv = map( self.pdf, xv )
        mean = sum( map( lambda x,y: x*y, xv, yv ) ) / sum(yv)
        return mean

    def __call__( self ):
        x2 = self.low - 1
        while not( self.low <= x2 < self.upp ):
            x2 = self.rng.gauss( self.x1, self.sig )

        f2 = self.pdf(x2)
        ratio = f2/self.f1

        if ratio >= 1 or self.rng.uniform(0,1) < ratio:
            self.x1 = x2
            self.f1 = f2

        return self.x1

class MaxwellGenerator:
    '''
        Generate random numbers according to a given pdf.
    '''
    def __init__( self, T = 300., m = 1.0 ):
        '''
            Initialize with temperature in K and mass in amu.
        '''
        m       *= _amu
        clin     = 4 * pi * ( 0.5 * m / ( pi * _k * T ) )**1.5
        cexp     = -0.5 * m / _k / T
        self.pdf = lambda v: clin * v**2 * exp(cexp * v**2)
        self.gen = Metropolis( self.pdf, 0.0, 100*(2*_k*T/(pi*m))**0.5 )

    def GetVelocityVector( self ):
        module  = self.GetVelocityModule()
        x, y, z = [ self.gauss(0,1) for i in range(3) ]
        norm    = ( x**2 + y**2 + z**2 )**0.5
        return module * x / norm, module * y / norm, module * z / norm

    def GetVelocityModule( self ):
        return self.gen()

    def __call__( self ):
        return self.gen()

# Example of the velocity distribution for pure helium, neon, argon and xenon at 300 K. Check it out in
# https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution#/media/File:MaxwellBoltzmann-en.svg
if __name__ == '__main__':
    from ROOT import *

    helium = MaxwellGenerator(300.,4.002602)
    neon   = MaxwellGenerator(300.,20.1797)
    argon  = MaxwellGenerator(300.,39.948)
    xenon  = MaxwellGenerator(300.,131.293)

    hHe = TH1F('He','He;v (m/s);Entries',500,0,2500)
    hNe = TH1F('Ne','Ne;v (m/s);Entries',500,0,2500)
    hAr = TH1F('Ar','Ar;v (m/s);Entries',500,0,2500)
    hXe = TH1F('Xe','Xe;v (m/s);Entries',500,0,2500)

    hHe.SetLineWidth(2); hHe.SetLineColor(kBlue)
    hNe.SetLineWidth(2); hNe.SetLineColor(kYellow)
    hAr.SetLineWidth(2); hAr.SetLineColor(kCyan)
    hXe.SetLineWidth(2); hXe.SetLineColor(kViolet)

    for i in xrange(100000):
        hHe.Fill(helium())
        hNe.Fill(neon())
        hAr.Fill(argon())
        hXe.Fill(xenon())

    gStyle.SetOptTitle(0)
    hXe.Draw()
    hAr.Draw('same')
    hNe.Draw('same')
    hHe.Draw('same')
    raw_input('done')
