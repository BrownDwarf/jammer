#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

chs = range(0, 32)

os.chdir(os.path.expandvars('$jammer/sf/2M0136'))

for ch in chs:
    os.chdir("K_ch{:03d}".format(ch))
    os.system('mkdir libraries &')
    os.system('grid.py --create > grid.out &')
    os.chdir("..")

