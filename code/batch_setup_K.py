#!/usr/bin/env python
import os
chs = range(5, 32)

os.chdir(os.path.expandvars('$jammer/sf/2M0314'))

if False:
    for ch in chs:
        os.chdir("K_ch{:03d}".format(ch))
        os.system('mkdir libraries &')
        os.system('$Starfish/scripts/grid.py --create > grid.out &')
        os.chdir("..")
print('Done with part I')

if True:
    for ch in chs:
        os.chdir("K_ch{:03d}".format(ch))
        os.system('$Starfish/scripts/pca.py --create > pca_create.out')
        os.system('$Starfish/scripts/pca.py --optimize=emcee --samples=3  > pca_optimize.out')
        os.system('$Starfish/scripts/pca.py --store --params=emcee > pca_store.out')
        os.system('mkdir output')
        os.system('mkdir output/marley_grid')
        os.system('mkdir output/marley_grid/run01')
        os.system('cp $jammer/sf/2M0314/K_ch003/output/marley_grid/run01/s0_o0phi.json output/marley_grid/run01/')
        os.chdir("..")

print('Done with part II')