#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

#chs = range(0, 14)
#chs= [9,8,7,6,5,4,3,2,1,0, 15, 16, 17, 18, 19, 20, 21]
#chs= [7,6,5,4,3,2,1,0, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
chs= [5,4,3,2,1,0, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

os.chdir(os.path.expandvars('$jammer/sf/2M0136'))

#for ch in chs:
#    os.chdir("K_ch{:03d}".format(ch))
#    os.system('mkdir libraries &')
#    os.system('grid.py --create > grid.out &')
#    os.chdir("..")

for ch in chs:
    os.chdir("K_ch{:03d}/output/marley_grid/run01/".format(ch))
    os.system('cp ../../../config.yaml .')
    os.system('/Users/gully/GitHub/jammer/code/star_marley.py --samples=5000 --incremental_save=50')
    os.chdir(os.path.expandvars('$jammer/sf/2M0136'))