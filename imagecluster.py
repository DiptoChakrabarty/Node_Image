import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import os 
import sys
'''cap = cv2.VideoCapture(0)
ret,photo = cap.read()
cv2.imshow("photo",photo)
cv2.waitKey()
cv2.destroyAllWindows()
cap.release()'''

def photo_segment(sys.argv[1]):
    path=sys.argv[1]    
    os.system("touch worked.txt")
    #photo=cv2.imread("/home/chuck/Downloads/download.png")
    photo= cv2.imread(path)
# Reshape Image
#photo=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
    rgb=cv2.cvtColor(photo,cv2.COLOR_BGR2RGB)

    x,y,z=rgb.shape
    rgb=rgb.reshape(x*y,z)


    #Use Kmeans
    rgb=np.float32(rgb)
    criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    K=7
    attempts=10
    ret,label,center=cv2.kmeans(rgb,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)


    #Plotting images
    center=np.uint8(center)
    res=center[label.flatten()]
    result_image=res.reshape((photo.shape))

    '''figure_size = 15
    plt.figure(figsize=(figure_size,figure_size))
    plt.subplot(1,2,1),plt.imshow(photo)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(result_image)
    plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])
    plt.show()'''
    cv2.imwrite("public/uploads/test1.png",result_image)
    
    return result_image

