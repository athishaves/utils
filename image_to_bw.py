import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

from PIL import Image  


def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def dodge(front,back): 
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')


def conver_to_gray(start_img, i):
    plt.figure(figsize=(8, 6))
           
    gray_img = grayscale(start_img)    
    plt.subplot(2,2,1)
    plt.title('Original')
    plt.imshow(start_img, cmap='gray')
    plt.axis('off')
    
    inverted_img = 255 - gray_img    
    plt.subplot(2,2,2)
    plt.title('Inverted')
    plt.imshow(inverted_img, cmap='gray')
    plt.axis('off')
    
    blur_img = ndimage.filters.gaussian_filter(inverted_img,sigma=i)    
    plt.subplot(2,2,3)
    plt.title('Blur')
    plt.imshow(blur_img, cmap='gray')
    plt.axis('off')
    
    final_img = dodge(blur_img,gray_img)    
    plt.subplot(2,2,4)
    plt.title('Final')
    plt.imshow(final_img, cmap='gray')
    plt.axis('off')
    
    return final_img


# TODO : Specify picture location
start_img = Image.open(img_location)  # image location


# print("Image size", start_img.size)

s = np.array(start_img)

rotated = ndimage.rotate(s, 0)            # specify rotation of the pic

final_img = conver_to_gray(rotated, 50)     # Vary the second parameter


# TODO : Specify final location
plt.savefig(final_img_location)      # final image location