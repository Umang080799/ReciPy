# RecipePy
Python-based application to help you decide what to do with the left over groceries in your fridge!

Tried out Object Detectin via:

1. OpenCV real time object detection
2. Clarifai API
3. Tensorflow


## The following is the frontend UI which displays the all the results gathered. 

## We have the details for the following information:

1. Dish name
2. Preparation Statistics
3. Recipe
4. Nutrition
5. Ingredients

<img width="1428" alt="Screen Shot 2019-07-18 at 4 29 17 PM" src="https://user-images.githubusercontent.com/35209670/61490364-c2c05680-a97a-11e9-8093-9f661f074951.png">



Currently, I trained the model for detecting Onions using TF

## The following were the results by the pre trained TF API

<img width="1252" alt="Tensorflow API Detection_Onion_1" src="https://user-images.githubusercontent.com/35209670/61490184-5ba2a200-a97a-11e9-94ac-061316d876fc.png">
<img width="480" alt="Tensorflow API Detection_Onion_2" src="https://user-images.githubusercontent.com/35209670/61490186-5ba2a200-a97a-11e9-8557-9259ae50efe0.png">




## The following were the results by custom training for detecting Onions 

<img width="669" alt="After training result_2" src="https://user-images.githubusercontent.com/35209670/61490170-53e2fd80-a97a-11e9-861e-efa17d4b7073.png">
<img width="463" alt="After_training_result_onion_1" src="https://user-images.githubusercontent.com/35209670/61490171-53e2fd80-a97a-11e9-880e-de5dd2c52190.png">



## Tools used for training were:

1. LabelImg : For labelling the images. 
2. ssd_mobilenet_v1_coco_11_06_2017 : Pre trained model for training and building the model 
3. Tensorboard : To keep track of the progress of the training

