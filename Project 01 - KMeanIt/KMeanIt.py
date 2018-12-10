import os, sys
from KMeansGifer import KMeansGif
from matplotlib import pyplot as plt
import numpy as np
import fibo as f


# Setup:
# 1. Import Image
# 2. Save it's dimensions and depth
# 3. Scale and flatten.
# 4. Make array of rand numbers based on the pixels themselves
image = plt.imread("kmeans.jpg")
k_offset = 2 # minimum k value never drop below 2
kmg = KMeansGif()
kmg.ydim, kmg.xdim, kmg.dpth = image.shape
scaler = 1 # Use .0 to scale to floats
image = image / scaler
image_flat = image.reshape(kmg.ydim * kmg.xdim, kmg.dpth)
kari = [int(0.01*f[0]*f[1]*f[2])%10+k_offset for f in image_flat]
kari = [v for i,v in enumerate(kari) if v != kari[i-1]]
print("KARI",len(kari))
# Do KMeansGif
# 1. Determine how many images you want in the final gif.
# 2. Do them
# 3. Save them.
howmany = 9
kmg.ResetImages()
kmg.imgIn = image_flat
for i,k in enumerate(kari[:howmany]):
    print(i,k)
    kmg.n = k
    print("INOUT",len(kmg.imgIn),len(kmg.imgOut))
    kmg.getImageKM() # <- perform KMeans (found in KMeansGifer.py)
    print("INOUT",len(kmg.imgIn),len(kmg.imgOut))
    kmg.AddImage()
    print("INOUT",len(kmg.imgIn),len(kmg.imgOut))
kmg.SaveToDisk()