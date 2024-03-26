import h5py
import numpy as np
import matplotlib.pyplot as plt
#from collections import Counter
from scipy import interpolate
from scipy.interpolate import CubicSpline
import os


#class LinRegLearner(object):  
def __init__(self):
    """
    """
    pass


def retWidthSize(cr1, cr2):
    """
    """
    sizelist = [0.05, 0.07, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.23, 0.26, 0.3, 0.33, 0.36, 0.4, 0.43, 0.46, 0.5, 0.53, 0.56, 0.6, 0.7]
    sizelist = np.array(sizelist)
    # size applied in the LUT
    widthlist = np.arange(1.05,2.0,0.05)
    db449 = np.loadtxt('../dat/db_width_449.txt')
    db756 = np.loadtxt('../dat/db_width_756.txt')
    db1544 = np.loadtxt('../dat/db_width_1544.txt')

    ratio1 = db449[:,:]/db756[:,:]
    ratio2 = db1544[:,:]/db756[:,:]
    nwidth,nsize = np.shape(ratio1)

    arr_size = np.zeros(nwidth)
    # array contains size for each width after first interpolation
    arr_cr2 = np.zeros(nwidth)
    # array contains color ratio 2 for each width when size is arr_size

    for iw in range(nwidth):
    # loop for width
        fsize = interpolate.interp1d(ratio1[iw,:],sizelist)
        # function: size = fw(color ratio 1)
        arr_size[iw] = fsize(cr1)
#        arr_size[iw] = np.interp(cr1,ratio1[iw,:],sizelist)
        # color ratio 1 -> size of each width
#        print(ratio1[iw,:])
#        print(sizelist)
#        print(cr1, arr_size[iw])

        #fcr2 = CubicSpline(sizelist, ratio2[iw,:])
        # function: color ratio 2 = fw(size)
        arr_cr2[iw] = np.interp(arr_size[iw],sizelist, ratio2[iw,:])
        # size of each width -> color ratio 2 of each width

        result_width = np.interp(cr2, arr_cr2, widthlist)
        # function: width = fw(color ratio 2)
        # color ratio 2 -> width
        
        result_size = np.interp(result_width, widthlist, arr_size)


#    print(arr_size)
#    print(arr_cr2)
#    print(result_width)
#    print(result_size)

    return result_width, result_size

def loadDat(file00):
    """
    """

    filename = file00
        #ds_disk = xr.open_dataset(filename)

    with h5py.File(filename, 'r') as data:
    #    for group in data.keys() :
    #        print (group)

        ds_ext = data['Aerosol Products']['AerExt'][()]
        ds_lat = data['Ground Track Data']['GT_Latitude'][()]
        ds_wav = data['Aerosol Products']['Aer_Wavelength'][()]
        #    ds_data = data['payload_data']['RADIANCE']
        #    print (ds_data.shape, ds_data.dtype)

    ds_alt = np.arange(0,len(ds_ext)/2,0.5)
    print(ds_lat[5])

    nalt, nband = np.shape(ds_ext)
    print(np.shape(ds_ext))

    # 0:384.1;
    # 1:448.7;
    # 2:520.5;
    # 3:601.7;
    # 4:676.1;
    # 5:756.0;
    # 6:869.2;
    # 7:1021.5;
    # 8:1543.9; 
    band1 = 1 # 449 nm
    band2 = 5 # 756 nm
    band3 = 8 # 1544 nm

    cr1 = ds_ext[:,band1].squeeze()/ds_ext[:,band2].squeeze()

    cr2 = ds_ext[:,band3].squeeze()/ds_ext[:,band2].squeeze()

    cr1[cr1 >= 5] = np.nan
    cr1[cr1 <= 0] = np.nan
    cr1[cr1 == 1] = np.nan
    cr2[cr2 >= 1] = np.nan
    cr2[cr2 <= 0] = np.nan

#    print(cr1)
#    print(cr2)
    return cr1, cr2



if __name__ == "__main__":

#    retWidthSize(1.5, 0.3)
    ds_alt = np.arange(0,90/2,0.5)
    datCR1, datCR2 = loadDat('./../dat/g3b.ssp.2020010111SSv05.30')
    for i in range(len(datCR1)):
        if (datCR1[i] > 0 and datCR2[i] > 0):
            print('altitude: ',ds_alt[i], datCR1[i], datCR2[i])
            result_width, result_size = retWidthSize(datCR1[i], datCR2[i])
            print(result_width, result_size)





