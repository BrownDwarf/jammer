#!/usr/bin/env python
import os

chs = list(range(5, 30))

os.chdir(os.path.expandvars('$jammer/sf/2M0314/'))

for ch in chs:
    print(m)
    os.system("cp K_ch004/user_prior.py K_ch{:03d}/".format(ch))
    os.chdir("K_ch{:03d}/output/marley_grid/run01/".format(ch))
    os.system('time $jammer/code/star_marley_beta.py --samples=5000 --incremental_save=100 > run.out')
    os.chdir(os.path.expandvars('$jammer/sf/2M0314/'))
