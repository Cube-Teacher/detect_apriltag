import pupil_apriltags as apriltag 
import cv2
import numpy as np
import time
from pupil_apriltags import Detector

cap = cv2.VideoCapture(0)
cv2.namedWindow('camera', cv2.WINDOW_AUTOSIZE)
detector1 = apriltag.Detector(families='tag36h11')
#detector2 = apriltag.Detector(families='tag16h5')
#detector3 = apriltag.Detector(families='tag25h9')

while (1):
    ret, image = cap.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #options = apriltag.DetectorOptions(families='tag36h11')
    
    tag36h11_tag0=0
    tag36h11_tag1=0
    tag36h11_tag24=0
    tag36h11_tag25=0
    
    results1 = detector1.detect(gray)
    #print(results1)
    for tag in results1:
        cv2.circle(image, tuple(tag.corners[0].astype(int)), 4,(0,0,255), 2) # right-bottom
        cv2.circle(image,tuple(tag.corners[1].astype(int)), 4,(0,0,255), 2) # left-top
        cv2.circle(image, tuple(tag.corners[2].astype(int)), 4,(0,0,255), 2) # right-top
        cv2.circle(image, tuple(tag.corners[3].astype(int)), 4,(0,0,255), 2) # left-bottom
        if tag.tag_id==0:
            tag36h11_tag0=tag36h11_tag0+1
        if tag.tag_id==1:
            tag36h11_tag1=tag36h11_tag1+1
        if tag.tag_id==24:
            tag36h11_tag24=tag36h11_tag24+1
        if tag.tag_id==25:
            tag36h11_tag25=tag36h11_tag25+1
        #print(tag.tag_id)
    
    #results2 = detector2.detect(gray)
    #print(results2)
    #for tag in results2:
        #cv2.circle(image, tuple(tag.corners[0].astype(int)), 4,(0,255,255), 2) # right-bottom
        #cv2.circle(image,tuple(tag.corners[1].astype(int)), 4,(0,255,255), 2) # left-top
        #cv2.circle(image, tuple(tag.corners[2].astype(int)), 4,(0,255,255), 2) # right-top
        #cv2.circle(image, tuple(tag.corners[3].astype(int)), 4,(0,255,255), 2) # left-bottom
    
    #results3 = detector3.detect(gray)
    #print(results3)
    #for tag in results3:
        #cv2.circle(image, tuple(tag.corners[0].astype(int)), 4,(255,0,255), 2) # right-bottom
        #cv2.circle(image,tuple(tag.corners[1].astype(int)), 4,(255,0,255), 2) # left-top
        #cv2.circle(image, tuple(tag.corners[2].astype(int)), 4,(255,0,255), 2) # right-top
        #cv2.circle(image, tuple(tag.corners[3].astype(int)), 4,(255,0,255), 2) # left-bottom
        

    cv2.imshow('camera', image)
    cv2.waitKey(1)
    print('tag0:',tag36h11_tag0,'\n')
    print('tag1:',tag36h11_tag1,'\n')
    print('tag24:',tag36h11_tag24,'\n')
    print('tag25:',tag36h11_tag25,'\n')
    print('\n')
    #time.sleep(1.0)
    
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
