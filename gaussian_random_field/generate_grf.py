import numpy as np
import matplotlib.pyplot as plt

def _power_law(b,n):
    """Returns a function which is a power law in one variable."""
    return lambda k : b*k**n

def from_power_spectrum(P,shape):
#    K = np.array(np.meshgrid(*[np.arange(0, x-1) for x in shape]))
    K1 = np.array(np.meshgrid(*[np.fft.fftfreq(x) * x for x in shape[:-1]],np.fft.rfftfreq(shape[-1]) * shape[-1]))
#    print(*np.arange(len(shape),0,-1))
    K = K1.transpose(0,*np.arange(len(shape),0,-1))
#    K = np.indices(shape,dtype='float')  # K vector
    k = np.sqrt((K**2).sum(axis=0))    # magnitude of K vector
    # k.shape
    Pk = P(k)
#    Pk[0,0] = 0

    np.random.seed(840900)

    FK = (np.random.randn(*k.shape) + np.random.randn(*k.shape)*1j) * np.sqrt(Pk/2)
#    FX = 
    return np.fft.irfftn(FK,shape)


if __name__=="__main__":
    
    from matplotlib.widgets import Slider
    
    P = _power_law(1,2)   # powerspectrum defined as a power law
    shape = (128,128,128)
    FX = from_power_spectrum(P,shape)
    plt.figure(dpi=120)
#    plt.imshow(FX[1])
    
    
    frame = 0
    l = plt.imshow(FX[frame,:,:]) #shows 0th frame
    plt.subplots_adjust(left=0.25, bottom=0.25)

    axframe = plt.axes([0.25, 0.1, 0.65, 0.03])
    sframe = Slider(axframe, 'third direction', 0, 127, valinit=0)
    
    def update(val):
#        print(val)
        l.set_data(FX[int(val),:,:])
    
    sframe.on_changed(update)

    
    
    
    
    
    
    
    
    