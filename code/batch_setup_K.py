#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

chs = range(15, 32)

os.chdir(os.path.expandvars('$jammer/sf/2M0136'))

#for ch in chs:
#    os.chdir("K_ch{:03d}".format(ch))
#    os.system('mkdir libraries &')
#    os.system('grid.py --create > grid.out &')
#    os.chdir("..")

for ch in chs:
    os.chdir("K_ch{:03d}".format(ch))
    os.system('pca.py --create > pca_create.out')
    os.system('time pca.py --optimize=emcee --samples=100  > pca_optimize.out')
    os.system('time pca.py --store --params=emcee > pca_store.out')
    os.system('mkdir output')
    os.system('mkdir output/marley_grid')
    os.system('mkdir output/marley_grid/run01')
    os.system('cp /Users/gully/GitHub/jammer/sf/2M0136/m110/output/marley_grid/run01/s0_o0phi.json output/marley_grid/run01/')
    os.system('cp /Users/gully/GitHub/jammer/sf/2M0136/m110/output/marley_grid/run01/user_prior.py output/marley_grid/run01/')
    os.chdir("..")