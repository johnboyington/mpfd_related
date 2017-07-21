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
    s += '{} PX  {}\n'.format(560 + num, 180)
    s += 'c \n'
    return s

def addAbs(cell, num):
    for i, value in enumerate(cell):
        if value > 0:
            cell[i] += num
        if value < 0:
            cell[i] -= num
    return cell

def makeNodeCells(num):
    #write spacer cells
    s  = 'c   spacer {}\n'.format(num)
    cell = np.array([-10, 11, -30, 40, 41, 42, 43, 44, 45, 46, 47, 48])
    cell = addAbs(cell, num)
    s   += '{} {} {} {} {} {}  {} {} {} {} {} {} {} {}\n'.format(10 + num, *mat[0], *cell)
    cell = np.array([-12, 13, -30, 40, 41, 42, 43, 44, 45, 46, 47, 48])
    cell = addAbs(cell, num)
    s   += '{} {} {} {} {} {}  {} {} {} {} {} {} {} {}\n'.format(11 + num, *mat[0], *cell)
    cell = np.array([-11, 12, -30, 31, 50, 40, 41, 42, 43, 44, 45, 46, 47, 48])
    cell = addAbs(cell, num)
    s   += '{} {} {} {} {} {} {} {}  {} {} {} {} {} {} {} {}\n'.format(12 + num, *mat[0], *cell)
    
    #write electrodeposition cells
    cell = np.array([-31, -11, 22])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(20 + num, *mat[0], *cell)
    cell = np.array([-31, -22, 21])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(21 + num, *mat[0], *cell)
    cell = np.array([-31, -21, 20])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(22 + num, *mat[0], *cell)
    cell = np.array([ -31, -11, 25])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(23 + num, *mat[0], *cell)
    cell = np.array([-31, -25, 24])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(24 + num, *mat[0], *cell)
    cell = np.array([-31, -24, 23])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(25 + num, *mat[0], *cell)
    
    #write argon within nodes
    cell = np.array([-50, 41, 45, -31, 23, -20])
    cell = addAbs(cell, num)
    s   += '{} {} {}    ({} {} {}):({} {} {}):\n'.format(26 + num, *mat[0], *cell)
    #argon in outer wand around node
    cell = np.array([-33, 30, -10, 13])
    cell = addAbs(cell, num)
    s   += '                ({} {} {} {})\n'.format(*cell)
    
    return s


def makeWandCells():
    #write wire cells
    s = ''
    for i in range(8):
        s   += '{} {} {}  {} {} {}\n'.format(5500 + i, *mat[0], -39, 3060, -2540 - i)
    
    #write steel casing cell
    s   += '{} {} {}  {} {} {}  $steel casing\n'.format(5550, *mat[0], -39, 3060, 2532, -2533)

    #write silica spacer cells
    s   += '{} {} {}   {}  {}  {}  {}\n'.format(5560, *mat[0], 3060, -2513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {}\n'.format(5561, *mat[0], 2510, -3513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {}\n'.format(5562, *mat[0], 3510, -4513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {}\n'.format(5563, *mat[0], 4510, -5513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {}\n'.format(5564, *mat[0], 5510, -39, 2531, -2533)
    
    #write argon in spacer cells
    s   += '{} {} {}   {}  {}  {} \n'.format(5570, *mat[0], 3060, -2513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5571, *mat[0], 2510, -3513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5572, *mat[0], 3510, -4513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5573, *mat[0], 4510, -5513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5574, *mat[0], 5510, -39, -2531)
    return s



mat = [[7, -3.88], #alumina
       [7, -3.88], #alumina
       [20, -3.88], #alumina
       [20, -3.88], #alumina
       [20, -3.88], #alumina
       [20, -3.88], #alumina
       ]

origins = [(200.0, 0.0, -8.3), (210.0, 0.0, -8.3), (220.0, 0.0, -8.3), (230.0, 0.0, -8.3)]

triga = open('triga1.txt', 'r').read()

cells = ''
for i, origin in enumerate(origins):
    i *= 1000 
    i += 2500
    cells += makeNodeCells(i)

cells += makeWandCells()

triga += cells

surfaces = ''

for i, origin in enumerate(origins):
    i *= 1000 
    i += 2500
    surfaces += makeSurfaces(origin, i)

triga += open('triga2.txt', 'r').read()
triga += surfaces
triga += open('triga3.txt', 'r').read()


with open('mpfd_cards.txt', 'w+') as cards:
    cards.write(cells)
with open('mpfd_cards.txt', 'a') as cards:
    cards.write(surfaces)
with open('triga_mpfd.i', 'w+') as inputfile:
    inputfile.write(triga)