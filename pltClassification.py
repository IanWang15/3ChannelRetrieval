import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

#sizelist = [0.0001, 0.001, 0.005, 0.01, 0.03, 0.05, 0.07, 0.08, 0.1, 0.12, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6]
sizelist = [0.01, 0.05, 0.07, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.23, 0.26, 0.3, 0.33, 0.36, 0.4, 0.43, 0.46, 0.5, 0.53, 0.56, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9]
    # size applied in the LUT
widthlist = np.arange(1.05,2.0,0.05)
#wavelengthlist = [510, 600, 675, 745, 868, 997]
db521 = np.loadtxt('../dat/db_width_521.txt')
db1022 = np.loadtxt('../dat/db_width_1022.txt')
# loading LUT

sizelist = np.array(sizelist)

#ratio1 = db510[:,:]/db745[:,:]
#ratio2 = db997[:,:]/db745[:,:]
ratio1 = db521[:,:]/db1022[:,:]
nwidth,nsize = np.shape(ratio1)
    # 19 16
#    print(nwidth,ndize)
#    print(len(sizelist))
fig, ax = plt.subplots(figsize=(10, 7))
for iw in range(0,nwidth,3):
    ax.plot(db1022[iw,1:]*100000., ratio1[iw,1:],'o-',label='width='+str(round(widthlist[iw],2)))

#for isize in range(0,nsize):
#    ax.plot(ratio2[:,isize], ratio1[:,isize],c='k',label='size='+str(sizelist[isize]))

import pdb
#pdb.set_trace() 
#print('stop here')

#ax.set_xlabel('Color Ratio (997/745)', fontsize=16)
#ax.set_ylabel('Color Ratio (510/745)', fontsize=16)
ax.set_ylabel('Color Ratio (521/1022)', fontsize=16)
ax.set_xlabel('1022 nm extinction', fontsize=16)
plt.legend(loc='upper right',frameon=False, fontsize=11.5)
plt.xscale("log")
plt.xlim([0.00001, 0.1])
plt.ylim([-0.1, 6.01])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

#pngname = "../fig/"+"fig_510_745_997.png"
pngname = "../fig/"+"fig_521_1022_zoom.png"
print("save ", pngname)
plt.savefig(pngname, bbox_inches='tight')

