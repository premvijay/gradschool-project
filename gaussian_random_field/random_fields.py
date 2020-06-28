# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:32:33 2020

@author: premv
"""

import numpy as np
from matplotlib import widgets, pyplot as plt
import pandas as pd




class GaussianRandomField:
    def __init__(self):
        pass
    
    def _power_law(self,b,n):
        """Returns a function which is a power law in one variable."""
        return lambda k : b*k**n

    def set_Pk(self,P):
        self.P = P
        
    def set_Pk_power_law(self,b,n):
        self.P = self._power_law(b,n)
        
    
    def generate_from_Pk(self,shape):
        self.shape = shape
        self.K = np.array(np.meshgrid(*[np.fft.fftfreq(x) * x for x in self.shape[:-1]],
                                         np.fft.rfftfreq(self.shape[-1]) * self.shape[-1]))
#        self.K = self.K1.transpose(0,*np.arange(len(self.shape),0,-1))
    #    K = np.indices(shape,dtype='float')  # K vector
        self.k = np.sqrt((self.K**2).sum(axis=0))    # magnitude of K vector
        self.Pk = self.P(self.k)    
#        np.random.seed(840900)
        self.FK = (np.random.randn(*self.k.shape) + np.random.randn(*self.k.shape) *1j) * np.sqrt(self.Pk/2)
        self.FX = np.fft.irfftn(self.FK,shape)
        
    def visualise(self):
        plt.figure(dpi=120)
    #    plt.imshow(FX[1])
        self.image_interact = plt.imshow(self.FX[:,:,0]) #shows 0th frame
        plt.title("The gaussian random field in physical 3D space")
        plt.subplots_adjust(left=0.25, bottom=0.25)
        axframe = plt.axes([0.25, 0.1, 0.65, 0.03])
        self.image_slider = widgets.Slider(axframe, 'third direction', 0, self.shape[-1]-1, valinit=0)
        plt.show()
        
        def update(val):
#            print(val)
            self.image_interact.set_data(self.FX[:,:,int(val)])
            plt.show()
        
        self.image_slider.on_changed(update)
    
    def compute_Pk_from_field(self):
        self.FK_computed = np.fft.rfftn(self.FX)
        self.Pk_computed = pd.DataFrame(data=np.vstack((self.k.ravel(),
                    np.abs(self.FK_computed.ravel())**2)).T,columns=['k','Pk']).sort_values('k')
        
    def plot_original_and_computed_Pk(self):
        plt.figure(dpi=120)
        self.grouped3 = self.Pk_computed.groupby(pd.cut(self.Pk_computed['k'], bins=np.logspace(0.3,2, 600))).mean()
        plt.plot(self.grouped3['k'],self.P(self.grouped3['k']),'-',label='Used to generate the random field')
        plt.plot(self.grouped3['k'],self.grouped3['Pk'],'-',label='Computed from the generated random field')
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(bottom=10)
        plt.title("Power spectrum P(k)")
        plt.legend(loc="lower right")
        plt.show()
        
        
        
        
        
        
        
        
        
        
        