from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import imageio as imo
import pandas as pd
import numpy as np
import fibo as f

class KMeansGif:
    def __init__(self):
        '''
        Init is self explanatory. Look at the in-line comments for the selfs.
        '''
        self.saveas = "kmeangif.gif" # default save fn for gifs
        self.saveasj = "kmeanjpg.jpg" #default save fn for jpgs
        self.n = 2 # number of kmeans to perform whether those k's are sequential or sudo-random is another matter
        self.delay = .1 # delay in between gifs - used to determine how many times to repeat an image, giving the illusion of a delay
        self.doRotation = False # do i want to rotate the predictions along it's array (to purposely shift the colors around)
        self.doRotationAmt = 2 # if we are rotating by how much are we shifting the predictions
        self.images = [] # final list of images to be gif'd together
        self.imgOut = [] # the output image after performing a kmeans reassignment
        self.imgIn = [] # the input image to be kmeans'd
        self.ydim = 0 # y dimension for the image to be processed
        self.xdim = 0 # x dimension
        self.dpth = 0 # depth, meaning RGB as a standard s/b 3
        self.pred = [] # array of kmeans predictions for each feature
      
    def SaveToDisk(self, meth="gif"):
        '''
        By default we operate in the world that we are creating gifs.
        But if you happen to do only 1 KMeans operation why not save it as a 'jpg'
        instead?

        '''
        if meth == "gif":
            imo.mimsave(self.saveas,self.images,duration=self.delay)
        else:
            imo.imsave(self.saveasj,self.imgOut)
        
    def AddImage(self):
        '''
        Set obj.image the the array you want added to the list of images
        to be gifed prior to running AddImage.
        '''
        print(len(self.imgOut))
        self.images.append(self.imgOut)
    
    def ResetImages(self):
        '''
        Wipes out the array of images to be gifed. Generally only used when starting over.
        '''
        self.images = []
        
    def getImageKM(self):
        '''
        Do a KMeans on an image array and save the result in self.imgOut.
        This func will optionally rotate the predictions if that is set
        beforehand to True.
        '''
        print(len(self.imgIn))
        km_model = MiniBatchKMeans(n_clusters=self.n)
        km_model.fit(self.imgIn)
        print("Fitting KMeans Model to "+str(self.n)+" clusters.")
        self.pred = km_model.predict(self.imgIn)
        if self.doRotation:
            self.pred = self.rotate_predictions()
        predictions = km_model.cluster_centers_[self.pred]
        self.imgOut = predictions.reshape(self.ydim, self.xdim, self.dpth)
        print(len(self.imgOut))