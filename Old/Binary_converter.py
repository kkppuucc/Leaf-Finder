import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

move_directory = 'Processed'

image_path = ('UnProcessed/processedImage_150.jpg')

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


resized_image_biCUBIC = cv2.resize(image, (300, 300), interpolation=cv2.INTER_CUBIC)
threshold = 200
kernelY = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]],dtype=np.uint8)

kernel_eclipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

ret,text_static = cv2.threshold(resized_image_biCUBIC, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow('img',text_static)
plt.hist(resized_image_biCUBIC)
plt.show()
# os.chdir(move_directory)
# cv2.imwrite('processedImage_300.jpg', text_static)

cv2.waitKey(0)
cv2.destroyAllWindows()