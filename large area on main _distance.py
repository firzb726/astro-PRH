# _*_utf-8: coding _*_
############ computation for large area on main
import numpy as np
import matplotlib.pyplot as plt
import math
import copy
import os
import sys
import itertools


b1=-1.005916  ### cone angle_main
b2=-1.536136  ### cone angle_sub
R1=-11000.    ### curvature radius_mian  in[mm]
R2=-1885.256  ### curvature radius_sub   in[mm]

#r1=np.arange(0.,5000.,50.) ###[mm]
r2=750.  ###[mm]
L=4650.  ###[mm] distance between two aperture plane
L2=4000. ### distance from system focus to aperture plane of main ref

##### the solution of saq: (1+b)z^2-2Rz+r^2=0
def z(b,R,r_m):
    z1=np.sqrt((R/(1.+b))**2-r_m**2/(1.+b))+R/(1.+b)
    return z1
#A_m=z(b1,R1,5000.)-z(b1,R1,0.) #### aperture distance to x-axis on main
b=z(b1,R1,0.)
A_m=z(b1,R1,5000.)-z(b1,R1,0.)
#z_Es=A_m+L ###### z value of edge point on sub-mirror in coordinate
z_Es=z(b2,R2,750.)-z(b2,R2,0.)+L
#print A_m,',',z_Es
a=input('offset value of source:') ####### offset of source to vertical axis

##### 
def ang(r):
    z=np.sqrt((R1/(1.+b1))**2-r**2/(1.+b1))+R1/(1.+b1)-b
    z_der=(-1.)*(-1.)*r/((1.+b1)*np.sqrt((R1/(1.+b1))**2-r**2/(1.+b1)))
    vector1=np.array([a-r,l-z])
    vector2=np.array([750.-r,z_Es-z])
    vector3=np.array([z_der,1])
    cos1=np.dot(vector1,vector3)/(np.linalg.norm(vector1)*(np.linalg.norm(vector3)))
    cos2=np.dot(vector2,vector3)/(np.linalg.norm(vector2)*(np.linalg.norm(vector3)))
    ang=np.arccos(cos1)-np.arccos(cos2)
    #res=cos1-cos2
    return ang*360./(2.*np.pi)
    #return res


#print z, z_der
    #print np.arccos(cos1)*360./(2.*np.pi),np.arccos(cos2)*360./(2.*np.pi)

#plt.subplot(2,1,1)
for l in np.arange(90000,200000,5000):
    for r in np.arange(0,5001,100):
        if ang(r)<0.:
            continue
        else:
            plt.plot(l/1000.,r,'ko')
            


plt.xlabel('distance L in [m]')
plt.ylabel('radius measured in [mm]')
plt.xlim(85,200)
plt.ylim(0,5500)
plt.legend()

            #print 'distance is',l,',','radius is',r,',','difference of angle is',ang(r)
            #print l,r
#np.savetxt('test1_l.txt',l,delimiter=',')
############## plot
####
##plt.subplot(2,1,2)
##r=np.arange(0.,5001.,1.)
##z_der=r/((1.+b1)*np.sqrt((R1/(1.+b1))**2-r**2/(1.+b1)))
##ang=plt.plot(r,z_der,'r-')        
##plt.xlabel('distance in [mm]')                 
##plt.ylabel('inclueded angle in degree')    
##plt.xlim()
##plt.legend()
plt.show()
          


                
                
            
