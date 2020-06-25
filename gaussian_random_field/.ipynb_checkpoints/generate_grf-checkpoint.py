import numpy as np
import matplotlib.pyplot as plt

def _power_law(b,n):
    """Returns a function which is a power law in one variable."""
    return lambda k : b*k**n

def from_power_spectrum(P,shape,)
    K = np.meshgrid(*[np.arange(0, x-1) for x in shape])
    # len(K)
    K = np.indices(shape,dtype='float')  # K vector
    k = (K**2).sum(axis=0)**(1/2)    # magnitude of K vector
    # k.shape
    Pk = P(k)
    Pk[0,0] = 0

    np.random.seed(840900)
    return (np.random.randn(*shape) + np.random.randn(*shape)*1j) * np.sqrt(Pk/2)