'''
This script will write the mcnp input that will position the mpfd's within
the NEBP.
'''

import numpy as np
import os

def calcUHeight(mass):
    '''
    Calculates the volume of the tally region and then the height of the plane to create a cell for the uranium deposit.
    
    Input - mass of uranium (ug)
    Output - a height value (cm)
    '''
    
    radius = 0.075  #cm
    density = 19.1  #g/cm3
    mass_g = mass * 10 ** -6  #convert mass from ug to g
    volume = mass_g / density  #calculate volume of uranium
    print('Node volume is {} cm^3.'.format(volume))
    return volume / (np.pi * (radius ** 2))

def makeSurfaces(origin, num, u_mass):
    
    #write x planes for spacer
    s  = '{} PX  {} $+ disk\n'.format(10 + num,  0.25 + origin[0])
    s += '{} PX  {} $+ spacer\n'.format(11 + num,  0.10 + origin[0])
    s += '{} PX  {} $- spacer\n'.format(12 + num, -0.10 + origin[0])
    s += '{} PX  {} $- disk\n'.format(13 + num, -0.25 + origin[0])
    s += '{} PX  {} $midplane\n'.format(14 + num,  0.00 + origin[0])
    
    dh = calcUHeight(u_mass)
    #write x planes for depositions
    s += '{} PX  {}\n'.format(20 + num,   0.099993289718781 + origin[0])
    s += '{} PX  {}\n'.format(21 + num,   0.0999945 + origin[0])
    s += '{} PX  {}\n'.format(22 + num,   0.0999995 + origin[0])
    s += '{} PX  {}\n'.format(23 + num,  -0.0999945 + dh + origin[0])
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
    s += '{} RPP {} {}   {} {}   {} {}\n'.format(50 + num, -0.05 + origin[0], 0.05 + origin[0], -0.05 + origin[1], 0.05 + origin[1], -0.2351 + origin[2], 0.2351 + origin[2])
    s += 'c \n'
    #write endplanes
    s += '{} PX  {}\n'.format(561 + num, 175.25)
    s += '{} PX  {}\n'.format(560 + num, 177.79)
    s += 'c \n'
    print('{} {}'.format(-0.0999945 + origin[0], -0.0999945 + dh + origin[0]))
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
    cell = np.array([-10, 11, -30, 40, 41, 42, 43, 44, 45, 46, 47])
    cell = addAbs(cell, num)
    s   += '{} {} {} {} {} {}  {} {} {} {} {} {} {} {}\n'.format(10 + num, *mat[8], *cell)
    cell = np.array([-12, 13, -30, 40, 41, 42, 43, 44, 45, 46, 47])
    cell = addAbs(cell, num)
    s   += '{} {} {} {} {} {}  {} {} {} {} {} {} {} {}\n'.format(11 + num, *mat[8], *cell)
    cell = np.array([-11, 12, -30, 31, 50, 40, 41, 42, 43, 44, 45, 46, 47])
    cell = addAbs(cell, num)
    s   += '{} {} {} {} {} {} {} {} \n              {} {} {} {} {} {} {} {}\n'.format(12 + num, *mat[8], *cell)
    
    cell = np.array([ -31, 12, -25])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(23 + num, *mat[4], *cell)
    cell = np.array([-31, -24,  25])
    cell = addAbs(cell, num)
    s   += '{} {} {}   {}  {}  {}\n'.format(24 + num, *mat[5], *cell)
    cell = np.array([-31, -23, 24])
    cell = addAbs(cell, num)
    uranium = 3
    if num == 2500 or num == 5500:
        uranium = 10
    s   += '{} {} {}   {}  {}  {} $Uranium\n'.format(25 + num, *mat[uranium], *cell)
    
    #write argon within nodes
    cell = np.array([-50, 40, 41, 42, 43, 44, 45, 46, 47, -31, 23, -11])
    cell = addAbs(cell, num)
    s   += '{} {} {}    ({} {} {} {} {} {} {} {} {}):\n          ({} {} {}):'.format(26 + num, *mat[6], *cell)
    #argon in outer wand around node
    cell = np.array([-33, 30, -10, 13])
    cell = addAbs(cell, num)
    s   += '({} {} {} {})\n'.format(*cell)
    
    return s


def makeWandCells():
    #write wire cells
    s = ''
    for i in range(8):
        s   += '{} {} {}  {} {} {}\n'.format(5500 + i, *mat[7], -39, 3060, -2540 - i)
    
    #write steel casing cell
    s   += '{} {} {}  {} {} {} {} $steel casing\n'.format(5550, *mat[2], -39, 3060, -2532, 2533)
    s   += '{} {} {}  {} {} {}    $steel casing\n'.format(5551, *mat[2], 3061, -3060, -2532)

    #write silica spacer cells
    s   += '{} {} {}   {}  {}  {}  {} \n           5540 5541 5542 5543 5544 5545 5546 5547\n'.format(5560, *mat[9], 3060, -2513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {} \n           5540 5541 5542 5543 5544 5545 5546 5547\n'.format(5561, *mat[9], 2510, -3513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {} \n           5540 5541 5542 5543 5544 5545 5546 5547\n'.format(5562, *mat[9], 3510, -4513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {} \n           5540 5541 5542 5543 5544 5545 5546 5547\n'.format(5563, *mat[9], 4510, -5513, 2531, -2533)
    s   += '{} {} {}   {}  {}  {}  {} \n           5540 5541 5542 5543 5544 5545 5546 5547\n'.format(5564, *mat[9], 5510, -39, 2531, -2533)
    
    #write argon in spacer cells
    s   += '{} {} {}   {}  {}  {} \n'.format(5570, *mat[6], 3060, -2513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5571, *mat[6], 2510, -3513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5572, *mat[6], 3510, -4513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5573, *mat[6], 4510, -5513, -2531)
    s   += '{} {} {}   {}  {}  {} \n'.format(5574, *mat[6], 5510, -39, -2531)
    return s



mat = [[0, 0],
       [41, -0.00129300], #air
       [42, -8.000], #316 stainless stell
       [43, -19.100], #natural uranium
       [44, -4.500], #titanium
       [45, -21.450], #platinum
       [46, -0.01731596], #argon gas
       [47, -8.61000], #30 AWG alumel
       [48, -3.8800], #alumina
       [49, -2.200], #silica
       [50, -19.100], #HEU (highly enriched uranium)
       ]

masses = [0.877, 0.801, 0.803, 0.889]


x1 = 175.25 + 33.86
x2 = 175.25 + 34.86
x3 = 175.25 + 35.86
x4 = 175.25 + 36.86



origins = [(x1, 0.0, -8.3 - 0.87), (x2, 0.0, -8.3 - 0.87), (x3, 0.0, -8.3 - 0.87), (x4, 0.0, -8.3 - 0.87)]

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
    j = i
    i *= 1000 
    i += 2500
    surfaces += makeSurfaces(origin, i, masses[j])

triga += open('triga2.txt', 'r').read()
triga += surfaces
triga += open('triga3.txt', 'r').read()


with open('mpfd_cards.txt', 'w+') as cards:
    cards.write(cells)
with open('mpfd_cards.txt', 'a') as cards:
    cards.write(surfaces)
with open('triga_mpfd.i', 'w+') as inputfile:
    inputfile.write(triga)

#os.system('mcnp6 rp inp=triga_mpfd.i')
