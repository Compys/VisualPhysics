'''
    Module with some useful physical data. Math constants not included because the math module is usually needed and those numbers are already defined there.
'''

from __future__ import division

class Units:
    '''
        Conversions factors among units. The international system of units is set to 1.
    '''
    
    ### Base units
    m  =   kg =  s =  A =  K =  mol =  cd = 1e+00

    ### Sub-multiples
    mm =    g = ms = mA = mK = mmol = mcd = 1e-03
    um =   mg = us = uA = uK = umol = ucd = 1e-06
    nm =   ug = ns = nA = nK = nmol = ncd = 1e-09
    pm =   ng = ps = pA = pK = pmol = pcd = 1e-12
    fm =   pg = fs = fA = fK = fmol = fcd = 1e-15
    
    ### Multiples
    km =  ton = ks = kA = kK = kmol = kcd = 1e+03
    Mm = kton = Ms = MA = MK = Mmol = Mcd = 1e+06
    Gm = Mton = Gs = GA = GK = Gmol = Gcd = 1e+09
    Tm = Gton = Ts = TA = TK = Tmol = Tcd = 1e+12

    ### Derived units
    rad = 1 # Dimensionless
    sr  = 1 # Dimensionless
    Hz  = 1 / s
    N   = kg * m / s**2
    Pa  = N / m**2
    J   = N * m
    W   = J / s
    C   = A * s
    V   = W / A
    F   = C / V
    Ohm = V / A
    S   = 1 / Ohm
    Wb  = V * s
    T   = Wb / m**2
    H   = Wb / A
    Bq  = Hz
    
    ### Sub-multiples
    mrad = msr = mHz = mN = mPa = mJ = mW = mC = mV = mF = mOhm = mS = mWb = mT = mH = mBq = 1e-03
    urad = usr = uHz = uN = uPa = uJ = uW = uC = uV = uF = uOhm = uS = uWb = uT = uH = uBq = 1e-06
    nrad = nsr = nHz = nN = nPa = nJ = nW = nC = nV = nF = nOhm = nS = nWb = nT = nH = nBq = 1e-09
    prad = psr = pHz = pN = pPa = pJ = pW = pC = pV = pF = pOhm = pS = pWb = pT = pH = pBq = 1e-12
    frad = fsr = fHz = fN = fPa = fJ = fW = fC = fV = fF = fOhm = fS = fWb = fT = fH = fBq = 1e-15
    
    ### Multiples
    krad = ksr = kHz = kN = kPa = kJ = kW = kC = kV = kF = kOhm = kS = kWb = kT = kH = kBq = 1e+03
    Mrad = Msr = MHz = MN = MPa = MJ = MW = MC = MV = MF = MOhm = MS = MWb = MT = MH = MBq = 1e+06
    Grad = Gsr = GHz = GN = GPa = GJ = GW = GC = GV = GF = GOhm = GS = GWb = GT = GH = GBq = 1e+09
    Trad = Tsr = THz = TN = TPa = TJ = TW = TC = TV = TF = TOhm = TS = TWb = TT = TH = TBq = 1e+12

    ### Non-IS units
    gauss = 1e-4           * T
    amu   = 1.66053886e-27   * kg
    AU    = 1.49597870700e11 * m
    pc    = 3.08567758e16    * m
    ly    = 9.4605284e15     * m
    eV    = 1.602176565e-19  * J
    keV   = 1e3              * eV
    MeV   = 1e6              * eV
    GeV   = 1e9              * eV
    TeV   = 1e12             * eV
    PeV   = 1e15             * eV

    Celsius = lambda kelvin:  return ( kelvin  - 273.15 ) * K
    Kelvin  = lambda celsius: return ( celsius + 273.15 ) * K


class Constants:
    '''
        Physical constants.
    '''
    c       = 2.99792458e8          * Units.m / Units.s                   # Speed of light
    e       = 1.602176565e-19       * Units.C                             # Fundamental charge
    h       = 6.62606896e-34        * Units.J * Units.s                   # Planck constant
    hbar    = 1.054571628e-34       * Units.J                             # Reduced Planck constant
    eps0    = 8.854187817620391e-12 * Units.F / Units.m                   # Electromagnetic permittivity
    mu0     = 1.256637061435917e-6  * Units.N / Units.A**2                # Electromagnetic permeability
    Z0      = mu0 * c                                                     # Electromagnetic impedance of vacuum
    G       = 6.6742e-11            * Units.N * Units.m**2 / Units.kg**2  # Gravitational constant
    EM      = 8.987551787368176e9   * Units.N * Units.m**2 / Units.C **2  # Electromagnetic constant
    muB     = 9.27400949e-24        * Units.J / Units.T                   # Bohr magneton
    muN     = 5.05078343e-27        * Units.J / Units.T                   # Nuclear magneton
    a0      = 5.291772108e-11       * Units.m                             # Bohr radius
    alpha   = 7.297352568e-3                                              # Fine structure constant
    Rydberg = 1.0973731568525e7     *       1 / Units.m                   # Rydberg constant
    Nav     = 6.02214199e23         *       1 / Units.mol                 # Avogadro constant
    kBJ     = 1.3806505e-23         * Units.J / Units.K                   # Boltzmann constant
    R       = 8.314472              * Units.J / Units.mol  / Units.K      # Gas constant

class ParticlesMasses:
    '''
        Masses of some fundamental particles.
    '''
    e    =  0.510998928 * Units.MeV
    pi0  =  0.1349766   * Units.GeV
    pipm =  0.13957018  * Units.GeV
    p    =  0.938272013 * Units.GeV
    n    =  0.939565560 * Units.GeV
    mu   =  0.105658369 * Units.GeV
    W    = 80.401       * Units.GeV
    Z    = 91.1876      * Units.GeV

def Force( particle1, particle2, interaction_type = 'em' ):
    '''
        Force applied to particle1 due to the interaction of type interaction_type with particle2.
    '''
    if   interaction.upper() == 'G':
        constant = Constants.G * particle1.mass * particle2.mass
    elif interaction.upper() == 'EM':
        constant = Constants.EM * particle1.charge * particle2.charge

    relative_vector = particle1.pos - particle2.pos
    return constant * relative_vector.norm() / relative_vector.mag2

