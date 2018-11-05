def user_defined_lnprior(p):
    '''
    Takes a vector of stellar parameters and returns the ln prior.
    '''
    if not ((p[0] > 1900) and (p[0] < 2400) and
            (p[1] > 3.25) and (p[1] < 5.5) and
            (p[2] > -100) and (p[2] < 100) and
            (p[3] > 3) and (p[3] < 60) and
            (p[4] > -6) and (p[4] < 10) and
            (p[8] > 0.02) and (p[8] < 2.0) and
            (p[9] > 2.0) and (p[9] < 4.2) and
            (p[10] > 3) and (p[10] < 200) ):
      return -np.inf

    ln_prior_out = 0

    return ln_prior_out
