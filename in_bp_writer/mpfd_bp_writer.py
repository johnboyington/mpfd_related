'''
This script will write the mcnp input that will position the mpfd's within
the NEBP.
'''

import numpy as np

def makeSurfaces(origin, num):
    #write x planes for spacer
    s  = '{} PX  {} $+ disk\n'.format(10 + num,  0.25 + origin[0])
    s += '{} PX  {} $+ spacer\n'.format(11 + num,  0.10 + origin[0])
    s += '{} PX  {} $- spacer\n'.format(12 + num, -0.10 + origin[0])
    s += '{} PX  {} $- disk\n'.format(13 + num, -0.25 + origin[0])
    s += '{} PX  {} $midplane\n'.format(14 + num,  0.00 + origin[0])
    #write x planes for depositions
    s += '{} PX  {}\n'.format(20 + num,   0.099993289718781 + origin[0])
    s += '{} PX  {}\n'.format(21 + num,   0.0999945 + origin[0])
    s += '{} PX  {}\n'.format(22 + num,   0.0999995 + origin[0])
    s += '{} PX  {}\n'.format(23 + num,  -0.099993289718781 + origin[0])
    s += '{} PX  {}\n'.format(24 + num,  -0.0999945 + origin[0])
    s += '{} PX  {}\n'.format(25 + num,  -0.0999995 + origin[0])
    s += 'c \n'
    #write cylinders for spacer
    s += '{} C/X  {} {} {} $ceramic out\n'.format(30 + num, origin[1], origin[2],  0.235   )
    s += '{} C/X  {} {} {} $ceramin in \n'.format(31 + num, origin[1], origin[2],  0.075   )
    s += '{} C/X  {} {} {} $steel out  \n'.format(32 + num, origin[1], origin[2],  0.396075)
    s += '{} C/X  {} {} {} $steel in   \n'.format(33 + num, origin[1], origin[2],  0.346075)
    #write cylinders for wires
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(40 + num, origin[1] + 0.15    , origin[2] + 0.00,     0.02032)
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(41 + num, origin[1] + 0.106066, origin[2] + 0.106066, 0.02032)
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(42 + num, origin[1] + 0.00,     origin[2] + 0.15,     0.02032)
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(43 + num, origin[1] - 0.106066, origin[2] + 0.106066, 0.02032)
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(44 + num, origin[1] - 0.15,     origin[2] + 0.00,     0.02032)
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(45 + num, origin[1] - 0.106066, origin[2] - 0.106066, 0.02032)
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(46 + num, origin[1] + 0.00,     origin[2] - 0.15,     0.02032)
    s += '{} C/X  {:8.6f} {:8.6f} {:8.6f}\n'.format(47 + num, origin[1] + 0.106066, origin[2] - 0.106066, 0.02032)
    s += 'c \n'
    #write RPP for window in spacer
    s += '{} RPP {} {}   {} {}   {} {}\n'.format(50 + num, -0.2351 + origin[0], 0.2351 + origin[0], -0.05 + origin[1], 0.05 + origin[1], -0.05 + origin[2], 0.05 + origin[2])
    s += 'c \n'
    #write endplanes
    s += '{} PX  {}\n'.format(60 + num, 180)
    return s


def makeNodeCells(num):
    #write spacer cells
    s  = 'c   spacer {}\n'.format(num)
    cell = np.array([-10, 11, -30, 40, 41, 42, 43, 44, 45, 46, 47, 48]) + num
    s   += '{} {} {}   {} {} {}     {} {} {} {} {} {} {} {}\n'.format(10 + num, *mat[0], *cell)
    cell = np.array([-12, 13, -30, 40, 41, 42, 43, 44, 45, 46, 47, 48]) + num
    s   += '{} {} {}   {} {} {}     {} {} {} {} {} {} {} {}\n'.format(11 + num, *mat[0], *cell)
    cell = np.array([-11, 12, -30, 31, 50, 40, 41, 42, 43, 44, 45, 46, 47, 48]) + num
    s   += '{} {} {}   {} {} {} {} {}     {} {} {} {} {} {} {} {}\n'.format(12 + num, *mat[0], *cell)
    
    #write electrodeposition cells
    cell = np.array([-31, -11, ])
    s   += '{} {} {}   {}  {}  {}\n'.format(21 + num, *mat[0], *cell)
    return s

def makeWandCells():
    return



mat = [[20, -3.88], #alumina
       [20, -3.88], #alumina
       [20, -3.88], #alumina
       [20, -3.88], #alumina
       [20, -3.88], #alumina
       [20, -3.88], #alumina
       ]

origins = [(200.0, 0.0, -8.3), (210.0, 0.0, -8.3), (220.0, 0.0, -8.3), (230.0, 0.0, -8.3)]

surfaces = '\n \n CELLS \n \n'
for i, origin in enumerate(origins):
    i *= 100 
    i += 500
    surfaces += makeNodeCells(i)

surfaces += '\n \n SURFACES \n \n'

for i, origin in enumerate(origins):
    i *= 100 
    i += 500
    surfaces += makeSurfaces(origin, i)

with open('mpfd_cards.txt', 'w+') as cards:
    cards.write(surfaces)