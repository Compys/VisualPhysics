# 
#  Classes and methods to operate with Physics Objs under Gravity and Electro-magnetism
#
#  J.A. Hernando 09/12/14
#


from visual import vector, mag, cross, mag, norm
import visual as vis
from functools import *
from math import *
import random

DEBUG = False

# constants
#-------------------------
qe = 1.602176e-19 #C
me = 9.109382e-31 #kg
mp = 1.672621e-27 #kg
kc = 8.987552e9 #N m^2/C^2
G  = 6.673000e-11 #N m^2/kg^2 

rh = 5.3e-11 # m (H radius)

class qmag:

    f,p,n,u,m = 1e-15,1e-12,1e-9,1e-6,1e-3
    k,M,G,T,P = 1e3,1e6,1e9,1e12,1e15

class qconst:
    qe = 1.602176e-19 #C
    me = 9.109382e-31 #kg
    mp = 1.672621e-27 #kg
    kc = 8.987552e9 #N m^2/C^2
    G  = 6.673000e-11 #N m^2/kg^2 

class SI:
    length = 1. # meter
    time = 1. # second
    mass = 1. # kg
    charge = 1. # C

VNull = vector(0.,0.,0.)

def sumvectors(fs):
    f = reduce(lambda x,y:x+y,fs)
    return f

class QDin:
    """ Class to operate the object's dynamic
    """

    def __init__(self,mass=0.,pos=[0.0,0.],velocity=[0.,0.,0.],fix=False):
        """ generate an obj with a mass, position and velocity
            if fix is True the object does not move
        """
        self.mass = mass
        self.pos = vector(pos)
        self.velocity = vector(velocity)
        self.fix = fix
        return

    def move(self,dt,F=None):
        """ move the object a dt (diferential time) under a Force (F)
        """
        if (self.fix): return VNull
        if (F): self.ace = F/self.mass
        else: self.ace = VNull
        ds = self.velocity*dt+0.5*dt*dt*self.ace
        self.pos = self.pos + ds
        self.velocity = self.velocity + self.ace*dt
        dl = mag(ds)
        #print "QDin.move dt ",dt,' F ',F,' ace ',self.ace
        #print "QDin.move ds ",ds,' pos ',self.pos,' velo ',self.velocity
        return ds

class QCharge:
    """ Class to operate with the charge (electric and mass)
    """

    def __init__(self,charge,pos):
        """ create and obj with charge and position
        """
        self.pos = vector(pos)
        self.charge = charge
        return

    def force(self,E):
        """ return the force on the object if there is a field E
        """
        F = self.charge*E
        return F

    def efield(self,pos):
        """ return the E field created by this object on a position (pos)
        """
        vdir = pos-self.pos
        dir = mag(vdir)
        E = (qconst.kc*self.charge/(dir*dir))*(vdir/dir)
        return E

    def vfield(self,pos):
        """ return the V potencial created by this object on a position (pos)
        """
        vdir = pos.self.pos
        dir = mag(vdir)
        V = qconst.kc*self.charge/dir
        return V

    def update(self,ds):
        """ update the object if it moves a distance (vector) ds
        """
        self.pos = self.pos+ds
        return

class QUniform:
    """ Create an object with uniform charge
    """

    def __init__(self,E0,pos):
        self.E0 = E0
        self.udir = E0/mag(E0)
        self.pos = pos
        return

    def force(self,E):
        return VNull

    def efield(self,x):
        return self.E0

    def vfield(self,x):
        dis = (x-self.position()).dot(self.udir)
        V = 0.+mag(self.E0)*dis
        return V

    def update(self,ds):
        self.pos = self.pos+ds
        return

class QObj:
    """ Create a complete Q-Object. It has a qforce, and qdin (dynamic) and a (qvis) 
    """

    def __init__(self,qdin=None,qforce=None,qvis=None):
        """ create a Qobj with a qdin, qdin, and qvis objects
        """
        self.qdin = qdin
        self.qforce = qforce
        self.qvis = qvis
        return

    def move(self,dt,F):
        """ move the object under a force F applied a differential time (dt)
        """
        if (not self.qdin): return VNull
        if (self.qdin.fix): return VNull
        #print 'QObj.move dt ',dt,' F ',F
        ds = self.qdin.move(dt,F)
        if (self.qforce):
            self.qforce.update(ds)
        if (self.qvis):
            self.qvis.pos = self.qvis.pos+ds
        #print 'QObj.move ',ds
        return ds

    def force(self,E):
        """ return the Force over the object done by a E field
        """
        if (not self.qforce): return VNull
        F = self.qforce.force(E)
        #print 'QObj.force F ',F
        return F

    def efield(self,x):
        """ return the E-field created by this object on a position (pos)
        """
        if (not self.qforce): return VNull
        E = self.qforce.efield(x)
        #print 'QObj.efield E ',E
        return E

    def vfield(self,x):
        """ return the V potencial created by this object on a positon (pos)
        """
        if (not self.qforce): return 0.
        V = self.qforce.vdield(x)
        print 'QObj.vfield ',V
        return V

class QFrame:
    """ class to hold a list of QObjs that acts between themselves
    """

    def __init__(self,L=SI.length,T=SI.time,size=100):
        """ create frame with a length and time dimension
        """
        self.size = size
        self.qobjs = []
        self.ds = L/self.size
        self.dt = T/self.size
        return

    def add(self,qobj):
        """ add a QObj on the frame
        """
        if (not isinstance(qobj,QObj)):
            print 'Not valid obj ',qobj
        self.qobjs.append(qobj)
        return

    def run(self,time,rate=100,userfun=None):
        """ run the frame during a time (time)
        after every step the userfun is called with the objects of the frame as argument 
        """
        ns = int(time/self.dt)
        for i in range(ns):
            vis.rate(rate)
            self.move(self.dt)
            if (userfun): userfun(self.qobjs)
        return

    def move(self,dt):
        """ do a move with a differential time (dt)
        """
        for iobj in self.qobjs:
            E = self.efield_atobj(iobj)
            F = iobj.force(E)
            ds = iobj.move(self.dt,F)
            if (mag(ds)>self.ds): 
                print "WARNIGN! large ds step ds ",ds,self.ds
                self.dt /=10.
        return 

    def efield(self,pos):
        """ return the E-field at position (pos) created by the objs of the frame
        """
        es = map(lambda obj: obj.efield(pos),self.qobjs)
        E = sum(es)
        return E

    def vfield(self,pos):
        """ return the V-potencial at position (pos) created by the objs of the frame
        """
        vs = map(lambda  obj: obj.vfield(pos),self.qobjs)
        V = sum(vs)
        return V

    def efield_at(self,obj):
        """ return the E-field at object (obj)
        """
        if (not obj.qdin): return VNull
        x = obj.qdin.pos
        cobjs = filter(lambda iobj: iobj != obj, self.qobjs)
        if (len(cobjs)==0): return VNull
        E = sumvectors(map(lambda obj: obj.efield(x),cobjs))
        return E

    def vfield_at(self,obj):
        """ return the V-potential al object (obj)
        """
        if (not obj.qdin): return VNull
        x = obj.qdin.pos
        cobjs = filter(lambda iobj: iobj != obj, self.qobjs)
        V = sum(map(lambda obj: obj.vfield(x),cobjs))
        return V

class QFactory:
    """ class to create QObjs
    """

    @staticmethod
    def ball(pos,mass,charge,radius,velocity=(0.,0.,0.)):
        """ create a ball (QObj object) with mass, charge, and radius, at position (pos) and velocity
        """
        qdin,qforce,qvis = None,None,None
        if (mass): qdin = QDin(mass,pos,velocity=velocity)
        if (charge): qforce = QCharge(charge,pos)
        if (radius): qvis = vis.sphere(pos=pos, radius= radius, frame = None)
        qobj = QObj(qdin,qforce,qvis)
        return qobj


def exam1():
    """ example to generate a ball 
    """
    q1 = QFactory.ball(pos=(-10.,0.,0.),mass=1.,charge=1.*QMag.u,radius=0.1)
    q1.qdin.velocity=vector(1.,0.,0.)
    #q2 = QFactory.ball(pos=(0.,0.,0.),mass=1.,charge=1*QMag.u,radius=0.1)
    f = QFrame()
    f.add(q1)
    #f.add(q2)
    f.run(1000*f.dt)
    return f

def exam2():
    """ example to generate 4 balls in a square
    """
    q1 = QFactory.ball(pos=(-10.,0.,0.),mass=10.*qmag.m,charge=+10.*qmag.u,radius=0.3)
    q2 = QFactory.ball(pos=(+10.,0.,0.),mass=10.*qmag.m,charge=+10.*qmag.u,radius=0.3)
    q3 = QFactory.ball(pos=(0.,-10.,0.),mass=10.*qmag.m,charge=-10.*qmag.u,radius=0.3)
    q4 = QFactory.ball(pos=(0.,+10.,0.),mass=10.*qmag.m,charge=-10.*qmag.u,radius=0.3)
    q3.qdin.fix = True; q4.qdin.fix = True;
    q3.qvis.color = vis.color.red; q4.qvis.color = vis.color.red
    f = QFrame()
    map(lambda q: f.add(q),[q1,q2,q3,q4])
    vis.rate(1)
    raw_input('enter key to continue ')
    f.run(10000*f.dt,rate=1000)
    return f
    
def exam3(n=10):
    """ example to generate n balls inside a balloon, some of them are fix  
    """
    qs = []
    box = vis.sphere(pos=(0,0,0),radius=10.,opacity=0.5,color=vis.color.white)
    for i in range(n):
        x,y,z = random.uniform(-1.,1.),random.uniform(-1.,1.),random.uniform(-1.,1.)
        q = QFactory.ball(pos=(x,y,z),mass=1.*qmag.m,charge=+100.*qmag.u,radius=0.3)
        q.qvis.color = vis.color.blue
        x = random.uniform(0.,1.)
        ok = (x<0.9)
        print ' ok ',ok
        q.qdin.fix = ok
        if (not ok): q.qvis.trail = vis.curve(color=vis.color.blue)
        qs.append(q)
    def velo(v=0.1):
        phi = random.uniform(0,2.*pi)
        theta = random.uniform(0,pi)
        v = vector(v*sin(theta)*cos(phi),v*sin(theta)*sin(phi),v*cos(theta))
        print ' v ',v
        return v
    for q in qs:
        q.qdin.velocity = velo()
    f = QFrame()
    f.dt/=20
    map(lambda q: f.add(q),qs)
    def bounce(qs):
        for q in qs:
            if (mag(q.qdin.pos)>10.): 
                print 'Bounce!! '
                q.qdin.velocity = -1.*q.qdin.velocity
            if (not q.qdin.fix): q.qvis.trail.append(q.qvis.pos)
        return
    #vis.rate(1)
    raw_input('press key to continue ')
    f.run(10000*f.dt,rate=1000,userfun=bounce)
    return f








