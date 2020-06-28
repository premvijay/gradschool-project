# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:43:35 2020

@author: premv
"""

from random_fields import GaussianRandomField

grf1 = GaussianRandomField()

grf1.set_Pk_power_law(1.0,2)


grf1.generate_from_Pk(shape=(128,128,128))

grf1.visualise()

grf1.compute_Pk_from_field()

grf1.plot_original_and_computed_Pk()























