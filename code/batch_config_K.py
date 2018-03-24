#!/usr/bin/env python
import os
import yaml
import numpy as np
import h5py

chs = range(5, 32)

os.chdir(os.path.expandvars('$jammer/sf/2M0314'))

for ch in chs:

    dat_name = os.path.expandvars('$jammer/data/IGRINS/reduced/2M0314+1603_K_ch{:03}.hdf5'.format(ch))
    path_out = 'K_ch{:03d}/'.format(ch)
    sf_out = 'K_ch{:03d}/config.yaml'.format(ch)

    f = open("K_ch003/config.yaml")
    config = yaml.load(f)
    f.close()

    f=h5py.File(dat_name, "r")
    wls = f['wls'][:]
    f.close()

    config['data']['files'] = ['$jammer/data/IGRINS/reduced/2M0314+1603_K_ch{:03d}.hdf5'.format(ch)]
    config['grid']['hdf5_path'] = '$jammer/sf/2M0314/K_ch{:03d}/libraries/Bobcat_IGRINS_Teff1900-2400.hdf5'.format(ch)
    lb, ub = int(np.floor(wls[0])), int(np.ceil(wls[-1]))

    config['grid']['wl_range'] = [lb, ub]
    config['PCA']['path'] = '$jammer/sf/2M0314/K_ch{:03d}/libraries/Bobcat_PCA_Teff1900-2400.hdf5'.format(ch)
    config['Theta_priors'] = '$jammer/sf/2M0314/K_ch{:03d}/user_prior.py'.format(ch)

    os.makedirs(path_out, exist_ok=True)
    with open(sf_out, mode='w') as outfile:
        outfile.write(yaml.dump(config))
        print('wrote to {}'.format(path_out))

