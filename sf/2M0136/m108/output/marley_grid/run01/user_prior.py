def user_defined_lnprior(p):
    '''
    Takes a vector of stellar parameters and returns the ln prior.
    '''
    if not ((p[8] > 0) and 
            (p[9] > 1) and (p[7] < 3.5) and
    		(p[10] > 10) and (p[6] < 200)):
    	return -np.inf

    lnp_sigamp = -(p[8] - 1.0)**2/(2.0*0.05**2)

    ln_prior_out = lnp_sigamp

    return ln_prior_out
