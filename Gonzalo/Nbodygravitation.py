from __future__ import division
import visual
import math
import random

def force(p1,p2):
    return L(p1,p2)**2 / p2.mass * (p1.pos - p2.pos) / (p1.pos - p2.pos).mag2 - G * 