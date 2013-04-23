'''
Created on Dec 22, 2012

@author: go
'''

import math
import numpy
import itertools
import cPickle
from SimpleCV import Image

import RetrieveConstants

RED, GREEN, BLUE = 0, 1, 2
X, Y = 0, 1

''' Generates histogram '''
def getHistogram(imageFile):
    im = Image(imageFile)
    #im = im.toRGB()
    im = im.toHSV()
    
    return im.histogram(64)

''' Normalizes histogram '''
def normHist(histograms):
    hist = []
    for histogram in histograms:
        hist.append(list(numpy.array(histogram) / float(sum(histogram))))
        
    return hist 

''' Evaluates histogram intersection for given two images' histograms '''
def evalHistIntersection(histReference, histQuery):
    nominator = 0.0
    sumHistReference = sum(histReference)
    sumHistQuery = sum(histQuery)
    for bin1, bin2 in zip(histReference, histQuery):
        nominator += min(float(bin1)/sumHistReference, float(bin2)/sumHistQuery)
    
    #denominator = min(sum(histReference), sum(histQuery))
    #denominator = sum(histReference)
        
    #return nominator / denominator
    return nominator

def getResult(queryImage):
    # Evaluate histogram of query image.
    histQueryImage = getHistogram(queryImage)
    
    indexFile = open(RetrieveConstants.INDEX_FILE, "rb")
    # Line starts with #, eliminating.
    imageDbBase = indexFile.readline()[1:].rstrip("\n")  
    
    # Get fingerprints for each image in database.
    fingerprint = cPickle.load(indexFile)
    
    queryResult = []
    for image in fingerprint.keys():
        # Apply histogram intersection to get similarity between two images by their histograms.
        similarity = evalHistIntersection(fingerprint[image], histQueryImage)
        if similarity > RetrieveConstants.SIMILARITY:
            queryResult.append((imageDbBase + image, similarity))
    
    return queryResult

def gridImage(image):
    numOfInterval = int(math.sqrt(RetrieveConstants.GRID))
    # Evaluate step size.
    step = int(min(round(image.width / numOfInterval), \
               round(image.height / numOfInterval)))
    
    # Determine row/column start indices for grids,
    # X=Y then X is enough for calculations.
    endX = 1 + (step * (numOfInterval - 1)) + step
    startPointsX = range(1, endX, step)
    # Cartesian product of points to determine start points of grids.
    startPoints = itertools.product(startPointsX, repeat=2)
    
    images = []
    for startPoint in startPoints:
        images.append(image.crop(startPoint[X], startPoint[Y], step, step))
    
    return images