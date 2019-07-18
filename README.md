# RecipePy
Python-based application to help you decide what to do with the left over groceries in your fridge!

Tried out Object Detectin via:

1. OpenCV real time object detection
2. Clarifai API
3. Tensorflow


The following is the frontend UI which displays the all the results gathered. 




Currently, I trained the model for detecting Onions using TF

The following were the results by the pre trained TF API




The following were the results by custom training for detecting Onions 




Tools used for training were:

1. LabelImg : For labelling the images. 
2. ssd_mobilenet_v1_coco_11_06_2017 : Pre trained model for training and building the model 
3. Tensorboard : To keep track of the progress of the training

