import cv2
import numpy as np
rgb_to_lms=np.array([[17.8824, 43.5161, 4.11935],
                        [3.45565, 27.1554, 3.86714],
                        [0.0299566, 0.184309, 1.46709]]).T

lms_to_rgb= np.array(np.matrix(rgb_to_lms).I)
'''np.array([[0.0809, -0.1305, 0.1167],
                        [-0.0102, 0.0540, -0.1136],
                        [-0.0004, -0.0041, 0.6935]]).T'''



def get(imgpath="1.jpg",protanopia_degree=0.0,deutranopia_degree=0.0,tritanopia_degree=0.0,outpath="after.jpg"):
    lj=np.array([[1 - protanopia_degree, 2.02344 * protanopia_degree, -2.52581 * protanopia_degree],
                            [0.494207 * deutranopia_degree, 1 - deutranopia_degree, 1.24827 * deutranopia_degree],
                            [-0.395913 * tritanopia_degree, 0.801109 * tritanopia_degree, 1 - tritanopia_degree]]).T
    
    img=cv2.imread(imgpath)
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    img_corrected=np.uint8(np.dot(img/255.0,np.dot(np.dot(rgb_to_lms,lj),lms_to_rgb))*255)
    cv2.imwrite(outpath, img_corrected)
    return img_corrected
get()