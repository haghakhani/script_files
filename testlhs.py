# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:49:58 2015

@author: haghakha
"""
import numpy as np
import os
import shutil as st

#lhs_sample=np.load('new_colima_samples.txt')
lhs_sample = np.genfromtxt ('colima_samples.csv', delimiter=",")

num_sample=64

fp = open(os.path.join(os.getcwd(),'mother/simulation.data'),'r')
simdata = fp.read()
fp.close

fp = open(os.path.join(os.getcwd(),'mother/frict.data'),'r')
fricdata = fp.read()
fp.close

#for paraboliod .5, for cylinder 1
shape_coef=1
h=320
r=300
phi_bed=37.0

for i in range(0,num_sample): 
    st.copytree('mother',os.path.join(os.getcwd(),'sample'+str(i))) 
    
for i in range(0,num_sample):
    
    h_rad=(shape_coef*(10.0**lhs_sample[i,0])/np.pi)**(1.0/3.0)
    print h_rad
    rp_simdata = simdata.replace(str(h), str(h_rad))
    rp_simdata = rp_simdata.replace(str(r), str(h_rad))
    
    rp_fricdata = fricdata.replace(str(phi_bed), str("{0:.2f}".format(lhs_sample[i,1])))
    
    fp = open(os.path.join(os.getcwd(),'sample'+str(i)+'/simulation.data'),'w')
    fp.write(rp_simdata)
    fp.close
    
    fp = open(os.path.join(os.getcwd(),'sample'+str(i)+'/frict.data'),'w')
    fp.write(rp_fricdata)
    fp.close