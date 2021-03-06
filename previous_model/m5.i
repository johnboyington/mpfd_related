MPFD Model
c *****Block 1*****
c
11 8 -3.88000000  -11 12 -21       41 42 43 44 45 46 47 48     $top disk
12 8 -3.88000000  -13 14 -21       41 42 43 44 45 46 47 48     $bot disk
13 8 -3.88000000  -12 15 -21 22 31 41 42 43 44 45 46 47 48     $top spacer
14 8 -3.88000000  -15 13 -21 22 31 41 42 43 44 45 46 47 48     $bot spacer
c
21 4 -4.50000000  -23  13 -51   $Ti electrodeposition bot
22 5 -21.4500000  -23  51 -52   $Pt electrodeposition bot
23 3 -19.1000000  -23  52 -53   $U  electrodeposition bot
24 4 -4.50000000  -23 -12  54   $Ti electrodeposition top
25 5 -21.4500000  -23 -54  55   $Pt electrodeposition top
26 3 -19.1000000  -23 -55  56   $U  electrodeposition top
c
31 2 -8.00000000  -24 25 -32        $wand steel casing
c
41 9 -2.20000000  -25 22 -32  11 41 42 43 44 45 46 47 48    $silica spacer top
42 9 -2.20000000  -25 22 -32 -14 41 42 43 44 45 46 47 48    $silica spacer bot
c
51 6 -0.01731596  -31             41 45      $argon in window
52 6 -0.01731596   31 -56 -12 -22  15        $argon in spacer, but not window
53 6 -0.01731596   31  53 -12 -22 -15        $argon in spacer, but not window
54 6 -0.01731596   31  21 -25 -11  14        $argon in outer wand
55 6 -0.01731596   11    -22 -32             $argon in silica spacer top
56 6 -0.01731596  -14    -22 -32             $argon in silica spacer bot
c
61 7 -8.61000000  -41 -32     $wire E
62 7 -8.61000000  -42 -32     $wire NE
63 7 -8.61000000  -43 -32     $wire N
64 7 -8.61000000  -44 -32     $wire NW
65 7 -8.61000000  -45 -32     $wire W
66 7 -8.61000000  -46 -32     $wire SW
67 7 -8.61000000  -47 -32     $wire S
68 7 -8.61000000  -48 -32     $wire SE
c
91 1 -0.00129300  -32 24                 $air  problem space
92 0               32                    $void problem space

c *****Block 2*****
c
11 PZ   0.25      $plane +hi
12 PZ   0.1       $plane +lo
13 PZ  -0.1       $plane -lo
14 PZ  -0.25      $plane -hi
15 PZ   0.0       $plane mid
c
21 CZ   0.235      $cylinder ceramic out 
22 CZ   0.075      $cylinder ceramic in
23 CZ   0.075      $cylinder electrodeposition
24 CZ   0.396075   $cylinder steel out
25 CZ   0.346075   $cylinder steel in
c
31 RPP -0.2351 0.2351  -0.05 0.05  -0.05 0.05   $window
32 RPP -10 10  -10 10  -10 10                   $problem space
c
41 C/Z   0.15      0          0.02032  $hole E
42 C/Z   0.106066  0.106066   0.02032  $hole NE
43 C/Z   0         0.15       0.02032  $hole N
44 C/Z  -0.106066  0.106066   0.02032  $hole NW
45 C/Z  -0.15      0          0.02032  $hole W
46 C/Z  -0.106066 -0.106066   0.02032  $hole SW
47 C/Z   0.       -0.15       0.02032  $hole S
48 C/Z   0.106066 -0.106066   0.02032  $hole SE
c
51 PZ  -0.0999995          $top plane for Ti electrodeposition
52 PZ  -0.0999945          $top plane for Pt electrodeposition
53 PZ  -0.099993289718781  $top plane for U deposition
54 PZ   0.0999995          $bot plane for Ti electrodeposition
55 PZ   0.0999945          $bot plane for Pt electrodeposition
56 PZ   0.099993289718781  $bot plane for U deposition

c *****Block 3*****
NPS   1E7
IMP:N 1 27R 0
MODE  N
F4:N  (23 26)
FM4   0.048328 3 -6
F14:N (23 26)
c  ---------------------------------------------------------
c                    SOURCE SPECIFICATIONS
c  --------------------------------------------------------- 
SDEF POS=-5 0 0 AXS=1 0 0 EXT=0 VEC=1 0 0 ERG=D3 DIR=FERG=D5 RAD=D6 PAR=1
SI6   0  1.27
SP6 -21  1
SI1 L 1 2
SP1 D 1 27.898
SI3 H  0.000E0   0.025E-6   4E-6   6E-6   1.000E-5  4.000E-5   1.00E-4
       4.00E-4  1.00E-3 4.0E-3 1.00E-02   1.60E-02   2.75E-02   4.75E-02
       7.5E-02 0.25 0.5 0.75 1.0 1.25 1.5 1.75 2.0 2.25 
       2.5 2.75 3.0 3.25 3.5 3.75 4.0 4.25 4.5 4.75 5.0
       5.25 5.5 5.75 6.0 6.25 6.5 6.75 7.0 7.25 
       7.5 7.75 8.0 9 10 12 20
SP3 D  0.00000000e+00   5.20743000e-12   8.67527000e-09   3.94049000e-09
       7.11822000e-09   3.72312000e-08   4.05493000e-08   8.75266000e-08
       6.86617000e-08   1.26816000e-07   9.31909000e-08   4.60387000e-08
       6.63830000e-08   6.54540000e-08   6.43465000e-08   2.38362000e-07
       2.61228000e-07   2.47072000e-07   2.20258000e-07   5.90739000e-07
       1.79933000e-07   2.70591000e-07   2.68789000e-07   1.95041000e-07
       3.48246000e-07   1.55054000e-07   1.40195000e-07   1.37839000e-07
       1.10643000e-07   9.28268000e-08   5.39062000e-08   4.98983000e-08
       9.78402000e-08   1.01642000e-07   1.22470000e-07   5.17798000e-08
       7.27559000e-08   3.53545000e-08   3.22774000e-08   5.83851000e-08
       1.31847000e-08   1.63656000e-08   1.53910000e-08   1.48804000e-08
       5.70646000e-09   4.63540000e-09   4.49608000e-09   1.53292000e-08
       1.12757000e-08   2.12464000e-08   1.34279000e-09
c ***Angular Distribution
DS5 S 8 15R 9 33R
c ***Neutrons
SI9 H -1 0  0.087156 0.173648 0.258819 0.342020 0.422618 0.5      0.573576 
       0.64278  0.707167 0.766044 0.819152 0.866025 0.906308 0.939692 
       0.9659258263 0.984807753 0.9876883406 0.9902680687 0.9925461516
       0.9945218954 0.9961946981 0.9975640503 0.9986295348 0.999390827
       0.9998476952 1
SP9 D  0 1.21322000e-08   1.97043000e-09   7.03301000e-09
       1.38584000e-08   2.28437000e-08   3.48414000e-08   5.13302000e-08
       7.12085000e-08   9.05588000e-08   1.07712000e-07   1.21943000e-07
       1.34182000e-07   1.42789000e-07   1.49421000e-07   1.52257000e-07
       1.48970000e-07   1.52386000e-07   3.53456000e-08   3.88644000e-08
       4.30788000e-08   5.48886000e-08   7.25409000e-08   1.45550000e-07
       3.71627000e-07   4.91383000e-07   5.37701000e-07   4.93681000e-07
SI8 H -1 0  0.087156 0.173648 0.258819 0.342020 0.422618 0.5      0.573576 
       0.64278  0.707167 0.766044 0.819152 0.866025 0.906308 0.939692 
       0.9659258263 0.984807753 0.9876883406 0.9902680687 0.9925461516
       0.9945218954 0.9961946981 0.9975640503 0.9986295348 0.999390827
       0.9998476952 1
SP8 D  0 3.78632000e-08   3.28731000e-09   1.08763000e-08
       1.98999000e-08   2.99492000e-08   4.08706000e-08   5.12739000e-08
       6.15954000e-08   7.02954000e-08   7.88992000e-08   8.50336000e-08
       9.03255000e-08   9.33998000e-08   9.36321000e-08   9.29627000e-08
       9.18170000e-08   9.62473000e-08   1.92430000e-08   2.16130000e-08
       2.17911000e-08   2.21717000e-08   2.10241000e-08   3.27896000e-08
       7.46238000e-08   4.04199000e-08   2.36255000e-08   1.86541000e-09
c
c  ---------------------------------------------------------
c  composition of the AIR (nominal density 0.00129300 g/cm^3)
c  ---------------------------------------------------------
M1    7014 -0.7558
      8016 -0.2314
     18000 -0.0128
c
c  ---------------------------------------------------------
c  composition of the 316 STAINLESS STEEL (nominal density 8.00000000 g/cm^3)
c  ---------------------------------------------------------
M2   26000 -0.72
     24000 -0.16
     28000 -0.10
     42000 -0.02
c
c  ---------------------------------------------------------
c  composition of the NATURAL URANIUM (nominal density 19.1000000 g/cm^3)
c  ---------------------------------------------------------
M3   92238 -0.99289
     92235 -0.00711
c
c  ---------------------------------------------------------
c  composition of the TITANIUM (nominal density 4.50000000 g/cm^3)
c  ---------------------------------------------------------
M4   22000 -1
c
c  ---------------------------------------------------------
c  composition of the PLATINUM (nominal density 21.4500000 g/cm^3)
c  ---------------------------------------------------------
M5   78000 -1
c
c  ---------------------------------------------------------
c  composition of the ARGON GAS (nominal density 0.01731596 g/cm^3)
c  ---------------------------------------------------------
M6   18000 -1
c
c  ---------------------------------------------------------
c  composition of the 30 AWG ALUMEL (nominal density 8.61000000 g/cm^3)
c  ---------------------------------------------------------
M7   28000 -0.95
     25055 -0.02
     13027 -0.02
     14000 -0.01
c
c  ---------------------------------------------------------
c  composition of the ALUMINA (nominal density 3.88000000 g/cm^3)
c  ---------------------------------------------------------
M8   13027 0.4
      8016 0.6
c
c  ---------------------------------------------------------
c  composition of the SILICA (nominal density 2.20000000 g/cm^3)
c  ---------------------------------------------------------
M9   14000 0.33
      8016 0.67
