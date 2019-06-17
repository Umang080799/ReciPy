#To make requests
import urllib.request
#For OpenCV
import cv2
import numpy as np
#To interface with the unerlying OS that python is operationg on
import os


def store_raw_images(): 
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    #Opening the URL link, opening , reading and then decoding it
    neg_image_url = urllib.request.urlopen(neg_images_link).read().decode()
    #Counter for keeping track of the URL number
    pic_num = 48
    
    #We create the neg directory of it doesn't exist
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    #We split the URLs according to the new line
    for i in neg_image_url.split('\n'):
        try:
            #Prints the URL
            print(i)
            #We save the raw image in the neg folder
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            #Reading the image as Greyscale
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            #Resizing the image
            resized_image = cv2.resize(img, (100, 100))
            #Writing the resized image
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))

def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

           if file_type == 'pos':
                #The dimensions of all the negartive images is 
                #50 by 50 to keep everything uniform
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
           elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)


create_pos_n_neg()
#The info.lst has the positive images which has
#the object we want to detect superimposed on the negatives.
#Added to that the file format is the file name, # of objects 
# in the file image, and the coordinates of the ROI(Region 
# of Interest). 
#store_raw_images()
