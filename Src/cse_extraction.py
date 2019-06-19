from apiclient.discovery import build
import requests
from bs4 import BeautifulSoup
from config import *
from cookinglight import *
from collections import OrderedDict


def collect_cse_results(search_key):
    #Unique API key
    api_key = API_KEY

    #Creates a service resource object to send the request
    #We call the cse() to make a Custom Search Engine object from it
    
    resource = build("customsearch",'v1',developerKey = api_key).cse()

    #Place the query you want to search in q
    #Place the unique cse id in the cx
    #execute() is called to actually execute the request

    result = resource.list(q= search_key,cx = CX).execute()
 
    return result
    #The result gives us the JSON data

def extract_website_name(search_results):
    #List containing all the website names
    website_list = []
    for link in search_results['items']:
        website = ""
        scrapped_website = link['link'][12:]
        
        for letter in scrapped_website:
            if letter == ".":
                break
            else:
                website += letter

        website_list.append(website)
    
    return website_list
    

def create_ingredients_sources(website_list,search_results):
    
    #Creating a dict data structure to have the link and the
    #website name for it
    website_dict = {}
    index = 0
    for link in search_results['items']:
        website_dict.update({link['link'] : website_list[index]})
        index += 1
    return website_dict


def extract_info(website_dict):
    parent_dish_list = []
    parent_recipe_list = []
    parent_ingredient_list = []
    parent_nutrition_list = []
    parent_prep_yield_list = []
    super_parent_list = {}
    super_list = []


    for key in website_dict:
        url = key
        #Gets the HTML page of the url
        html_page = requests.get(url)
        #Parsing the page using Beautiful Soup
        soup = BeautifulSoup(html_page.content,'html.parser')

        if website_dict[key] == "cookinglight":
            obj = Cookinglight()
            dishes = obj.extract_dishes(soup)
            recipes = obj.extract_recipe(soup)
            nutrition = obj.extract_nutrition(soup)
            ingredients = obj.extract_ingredients(soup)
            stats = obj.extract_prep_info(soup)
            parent_dish_list.append(dishes)
            parent_recipe_list.append(recipes)
            parent_ingredient_list.append(ingredients)
            parent_nutrition_list.append(nutrition)
            parent_prep_yield_list.append(stats)
    
    for dish,stat,recipe,nutrition,ingredient in zip(parent_dish_list,parent_prep_yield_list,parent_recipe_list,parent_nutrition_list,parent_ingredient_list):
        super_parent_list = OrderedDict([("Dish" , dish),("Prep_Statistics" ,stat)        
        ,("Recipe",recipe),("Nutrition" ,nutrition),("Ingredients" ,ingredient)])  
        super_list.append(super_parent_list)    
        super_parent_list = {} 
    return super_list
    
