'''
Created on Dec 22, 2012

@author: go
'''

import os
import sys
import cPickle
from SimpleCV import Image

import retrieve
import RetrieveConstants

def main():
    # Command line check.
    if len(sys.argv) < 2:
        print "Usage: python index.py absolute_path_to_image_db."
        sys.exit()
    else:
        imageDbBase = sys.argv[1]
    
    # Open index file.
    indexFile = open(RetrieveConstants.INDEX_FILE, "wb")
    indexFile.write("#" + imageDbBase + "\n")
        
    print "Indexing.."
    
    # Traverse in directory and sub-directories to get images.
    rootDirLen = len(imageDbBase)
    fingerprint = {} 
    for root, dirs, files in os.walk(imageDbBase):
        print files
        for f in files:
            if f.endswith(RetrieveConstants.IMAGE_FORMATS):
                # detect and segment cloth region for each image
                # Evaluate and save color histogram into index file.
                imageFile = os.path.join(root, f)
                #cPickle.dump((imageFile[rootDirLen:], retrieve.getHistogram(imageFile)), 
                #             indexFile)
                fingerprint[imageFile[rootDirLen:]] = retrieve.getHistogram(imageFile)

    cPickle.dump(fingerprint, indexFile)
    
    indexFile.close()

if __name__ == "__main__":
    main()
