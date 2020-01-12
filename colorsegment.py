import cv2
import numpy as np 
cap = cv2.VideoCapture(0)
#intensity of green
blue_lower=np.array([100,150,0])
blue_upper=np.array([140,255,255])
kernel_open=np.ones((5,5))
kernel_close=np.ones((15,15))

while True:
    ret,photo= cap.read()
    img=cv2.resize(photo,(340,220))
    # convert image to HSv
    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(imgHsv,blue_lower,blue_upper)
    #morphology 
    #kernel opening removes small white patches (noise)
    maskO=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel_open)
    #kernel close removes small black patches (noise) 
    maskC=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel_close)
    conts,h=cv2.findContours(maskC,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,conts,-1,(0,0,255),4)
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])   #Retreives boundary
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img,str(i+1),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), lineType=cv2.LINE_AA)
    cv2.imshow("close",maskC)
    cv2.imshow("open",maskO)
    cv2.imshow("HSV",mask)
    cv2.imshow("Normal",img)
    if (cv2.waitKey(1)==13):
        break
cap.release()
cv2.destroyAllWindows()
