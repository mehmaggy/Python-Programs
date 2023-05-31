import os
import re
import cv2
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from os.path import isfile,join
from os.path import isfile, join
col_frames = os.listdir('frames/')
col_frames.sort(key=lambda f:int(re.sub('\D','',f)))
# load frames
col_images=[]
for i in tqdm(col_frames):
    img = cv2.imread('frames/'+i)
    col_images.append(img)
#specific frame
idx = 457
stencil = np.zeros_like(col_images[idx][:,:,0])
#Specify coordinates of the polygon
polygon = np.array([[50,270],[220,160],[360,160],[480,270]])
# fill polygon with ones
cv2.fillConvexPoly(stencil,polygon,1)
img = cv2.bitwise_and(col_images[idx][:,:,0], col_images[idx][:,:,0],mask=stencil)
ret, thresh = cv2.threshold(img, 130, 145, cv2.THRESH_BINARY)
lines = cv2.HoughLinesP(thresh, 1, np.pi/180,30,maxLineGaps=200)
# create a copy of the original frame
dmy = col_images[idx][:,:,0].copy()
# draw Hough lines
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(dmy, (x1,y1),(x2,y2),(255,0,0),3)
cnt=0
for img in tqdm(col_images):
    # apply frame mask
    masked = cv2.bitwise_and(img[:,:,0], img[:,:,0], mask=stencil)
    # apply image thresholding
    ret, thresh = cv2.threshold(masked, 130,145, cv2.THRESH_BINARY)
    # apply Hough Line Transformation
    lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)
    dmy = img.copy()

    # Plot detected lines
    try:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(dmy,(x1,y1),(x2,y2),(255,0,0),3)

        cv2.imwrite('detected/'+str(cnt)+'.png',dmy)
    except TypeError:
        cv2.imwrite('detected/'+str(cnt)+'.png',img)
    cnt+=1
    #input framepath
    pathIn = 'detected/'
    #output path to save the video
    pathOut = 'roads_v2.mp4'
    #specify frames per second
    fps = 30.0
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files.sort(key=lambda f: int(re.sub('\D','',f)))
    frame_list = []

    for i in tqdm(range(len(files))):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height,width,layers=img.shape
        size = (width,height)

        #inserting the frames into an image array
        frame_list.append(img)
        out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(frame_list)):
            # writing to a image array
            out.write(frame_list[i])

        out.release()

# plot frame
plt.figure(figsize=(10,10))
plt.imshow(dmy, cmap = "gray")
plt.show()