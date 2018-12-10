from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import imageio as imo
import pandas as pd
import numpy as np
import fibo as f

class KMeansGif:
    def __init__(self):
        self.saveas = "kmeangif.gif"
        self.saveasj = "kmeanjpg.jpg"
        self.n = 2
        self.delay = .1
        self.doRotation = False
        self.doRotationAmt = 2
        self.images = []
        self.imgOut = []
        self.imgIn = []
        self.ydim = 0
        self.xdim = 0
        self.dpth = 0
        self.pred = []
      
    def SaveToDisk(self, meth="gif"):
        if meth == "gif":
            imo.mimsave(self.saveas,self.images,duration=self.delay)
        else:
            imo.imsave(self.saveasj,self.imgOut)
        
    def AddImage(self):
        self.images.append(self.imgOut)
    
    def ResetImages(self):
        self.images = []
        
    def rotate_predictions(self):
        rotv = self.doRotationAmt
        orig = self.pred
        uniq = np.unique(orig)
        rota = [uniq[idx-rotv] for idx,val in enumerate(uniq)]
        new = [rota[np.where(uniq==val)[0][0]] for val in orig]
        return new
        
    def getImageKM(self):
        km_model = MiniBatchKMeans(n_clusters=self.n)
        km_model.fit(self.imgIn)
        print("Fitting KMeans Model to "+str(self.n)+" clusters.")
        self.pred = km_model.predict(self.imgIn)
        if self.doRotation:
            self.pred = self.rotate_predictions()
        predictions = km_model.cluster_centers_[self.pred]
        self.imgOut = predictions.reshape(self.ydim, self.xdim, self.dpth)

    def getKsAndDelays(self, n, mink=2):
        k = n
        ans, fd = f.fibosum(k,rdict=1)
        rpt = [v for k,v in {key:value+1 for (key,value) in fd.items()}.items()][-1::-1]
        kd = [[i+mink,rpt[i]] for i in range(k)]
        return kd
    
    def getKsAndBreathe(self, n, mink=2):
        k = n
        breathe_sequence = [(np.round(.05*i**2)+10).astype('uint8') for i in range(k)][-1::-1]
        breathe_sequence = breathe_sequence+breathe_sequence[-1::-1]
        breathe_sequence = breathe_sequence-min(breathe_sequence)+1
        print(type(breathe_sequence))
        kd = [[i+mink,breathe_sequence[i]] for i in range(k)]
        return kd
