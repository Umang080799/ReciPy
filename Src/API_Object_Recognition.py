import cv2, numpy,os,argparse
from clarifai.rest import ClarifaiApp
import operator



def object_detect():
    search_key = "step by step recipes using "
    #Having the ingredient name and the value of its accuracy
    ingredients_dict = {}
    ingredient_list = []
    app = ClarifaiApp(api_key="feb7a705a2e74e25a9dfeac8c5ce0fe5")
    #Food model
    model = app.models.get('food-items-v1.0')
    response = model.predict_by_url(url='https://i.ibb.co/gPYyqmF/img-20180304-121907.jpg')
    
    for items in response['outputs']:
       for tags in items['data']['concepts']:
             ingredients_dict[tags['name']] = tags['value']


    #Sorts the dictionary based on the descending order of accuracy
    sorted_dict = sorted(ingredients_dict.items(), key=operator.itemgetter(1),reverse=True) 
    
    #Extracted all the ingredient names based on the highest level of accuracy
    for list_of_tuple in sorted_dict:
        ingredient_list.append(list_of_tuple[0])

    #Returning back the top 5 items from the list

    for ingredient in ingredient_list[:5]:
         search_key += ingredient + ' and '

    return search_key[:-5] 

