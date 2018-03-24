def user_defined_lnprior(p):
    '''
    Takes a vector of stellar parameters and returns the ln prior.
    '''
    if not ((p[8] > 0) and
            (p[9] > 1) and (p[7] < 3.5) and
    		(p[10] > 10) and (p[6] < 200)):
    	return -np.inf

    ln_prior_out = 0

    return ln_prior_out
