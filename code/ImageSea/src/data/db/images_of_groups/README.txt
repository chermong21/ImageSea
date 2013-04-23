The Images of Groups Dataset

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Citation
A. Gallagher, T. Chen, “Understanding Groups of Images of People,” IEEE Conference on Computer Vision and Pattern Recognition, 2009.

Bibtex

@inproceedings{gallagher_cvpr_09_groups,
author = {A. Gallagher and T. Chen},
title = {Understanding Images of Groups of People},
booktitle = {Proc. CVPR},
year = {2009},
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



The actual dataset includes 5080 images and 28231 faces.  In the paper, we describe features from the group structure that 
are used as context for estimating age and gender, and also to perform some camera calibration and 
event classification.

The images are split among 11 folders, based on the keyword search used to download the images from Flickr. The images are either 
Wedding images, Family images, or Group images. The folders of images are as follows: 

Wed2a
Wed3a
Wed5a
Fam2a
Fam4a
Fam5a
Fam8a
Group2a
Group4a
Group5a
Group8a

The number associated with the folder indicates the number of faces found in the image with our face detector. Note that 
non-detected faces are manually added. 
Each folder contains its images as well as a data file that describes the images in THAT folder. 

The ground truth file: PersonData.txt 

Each row is either an IMAGE row, or a FACE row. 
An image row is the name of an image (e.g. 1006149518_250f8036fc_1438_9284053@N07.jpg)


Each image name comprises the information required to recover the image source on Flickr. 
The format of the image is: ID_secret_server_userid.jpg
and the associated url is: 'http://static.flickr.com/' server '/' ID '_' secret '.jpg'];

In our example case:   		http://farm2.static.flickr.com/1438/1006149518_250f8036fc.jpg



An image row is followed with face rows (the faces belonging to that image). 
A face row has 6 tab-separated numbers: 
1. Left eye X coord
2. Left eye Y coord
3. Right eye X coord
4. Right eye Y coord
5. Human-Labeled Age
6. Human-Labeled Gender
Note that the left and right eyes are with respect to the viewer, so are opposite the person's point of view.


Human-Labeled Age: 
Faces were labeled as one of 7 categories, corresponding to 7 age ranges: 
Label		Age Range
1		0-2
5		3-7
10		8-12
16		13-19
28		20-36
51		37-65
75		66+

Human-Labeled Gender:
1		Female
2		Male 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

MATLAB DATA 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The same data is contained in Matlab form in the MatlabFiles folder. There, each file contains the associated information 
about one folder's worth of group images. Loading an .mat file leads the variable "coll" into the workspace. 

Here are the fields of coll. 
             faceData: [1x1090 struct]      size is 1xN, where N is the number of faces in the collection. faceData is a structure containing the field  "name" that is the name of the image that contains the face. (Note, this is the full path on my PC, so it will need to be massaged to match its new home). Also field poslxlyrxry is 1x4, the x and y coordinates of the left and right eyes. wh is 1x2, the width and height of the image. faceScore is the score of the face detector (0 if manually added). 
             ageClass: [1090x1 uint8]       size is 1xN. either 1,5,10,16,28,51 or 75 based on age class. 
             genClass: [1090x1 uint8]	    size is 1xN. either 1 (female) or 2 (male).
             genFeat: [1090x14 double]     These are the contextual features that are computed:
			% %   1. xcenter                  (normalized from 0 to 100). Left to right image coord
			%     2. ycenter                  (normalized from 0 to 100). top to bottom image coord
			%     3. minSpanningTreeDegree
			%     4. SizeRelativeToNeighbor   >1 means face bigger than neighbor
			%     5. PosX                     % negative means neighbor to the right of face (in eye dist units)
			%     6. PosY                     % % negative means Face below NN
			%     7. neiAngle                 % Angle of neighbor Face. Left eye at center, Cartesian coord system
			%     8. myAngle                  % angle of current Face
			%     9. SizeRelAverage           % face size relative to the average
			%     10-11. [x y] position relative average. 
			%     12. Size Relative to Planar FaceFit. 
			%     13. Nearest Neighbor Gender   (NOT USED IN CVPR 09)
			%     14. NEarest Neighbor Agebin   (NOT USED IN CVPR 09)
            facePlane: [509x3 double]
            faceImage: [509x25 double]
              faceDen: [509x4 double]
                 fimg: [1x1090 struct]      this is a structure that contains a small version of each face. e.g. imagesc(reshape(coll.fimg(1).im,61,49));colormap gray;axis image
               colorT: [1x1090 struct]
              ffcoefs: [1090x37 double]	    Nx37. Each row is a projection of that face into a fisherFace space, effective for facial similarity measurement. 
             faceGist: [1090x600 single]
            ageGuess1: [1090x1 double]
            ageGuess2: [1090x1 double]
        genderGuessNN: [1090x1 double]
        ageGuessGist1: [1090x1 double]
        ageGuessGist2: [1090x1 double]
    genderGuessGistNN: [1090x1 double]
     genderAccuracies: [2x1 double]
        ageAccuracies: [4x1 double]
               images: [1x1090 double]    size is 1xN, the index of the image that the face is from. The largest entry is I, the number of images in this portion of the collection. 
          facePosSize: [1090x7 single]    Nx7. Each row is [leftEyeX leftEyeY rightEyeX rightEyeY Xcenter YCenter EyeDistance]
            layerInfo: [1090x3 single]
	  tableImages: [299x1 single]    Ix1 where I is the number of images in the collection. The value is 1 if the image is "dining" otherwise it is 0. This field only exists for Group5a and Group8a, containing a total of 44 dining images out of 826 images. 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

MATLAB DATA for even age and gender sets. 

Even samplings of age and gender sets are in AgeGenderClassification 
eventrain     contains a collection (as above) containing 3500 faces 
eventest      contains a collection (as above) of 1050 faces. The age and gender classification results in the paper are with respect to this test set. 

Each of the test vectors can be traced back to an image in the collection. More information is available in another readme file in that directory about how the age and gender subspaces are used. 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

MATLAB DATA for row Labeling. 

This same dataset is used in the following paper: 

A. Gallagher, T. Chen, ”Finding Rows of People in Group Images,” IEEE International Conference on Multimedia and Expo 2009

to find rows of people in images. 

The ground truth row labelings for 234 images is: contained in Matlab format in the files: 
rowLabels5Groupa
and 
rowLabels8Groupa

Each of these files correspond to the collections in the Matlab format. For example, rowLabels5Groupa contains the row labels for selected images from Group5a. 
for example: 

load('C:\research\flickrGroupShot\Group5a.mat')
load('C:\research\flickrGroupShot\rowLabels5Groupa.mat')
% Then, here is an image that was not labeled:  (all zeros)
%>> rowLabels5Groupa(coll.images==2)
%
%ans =
%
%     0
%     0
%     0
%     0
%     0
%     0
%     0
%     0
%     0
%
% here is an image that was labeled: 
%>> rowLabels5Groupa(coll.images==13)
%
%ans =
%
%     2
%     2
%     1
%     1
%     2
%
Note if you use these variables in your work, please also cite the ICME paper as above. 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Also, a matlab viewer is included. If all files are placed in a single directory, 
then running the command: viewGroupImages(coll) after loading one of the matlab files will open file 
and  view the images and faces one by one (press any key to advance to a new image). 
Again,  you will need to replicate the full path of where the images are located, though.


