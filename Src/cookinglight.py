from bs4 import BeautifulSoup

class Cookinglight:

    def __init__(self):
      pass 

    def extract_dishes(self,soup):
        dish_list = []
        dishes = soup.find('h1',attrs={'class': 'headline heading-content margin-8-top margin-16-bottom'})
        for dish in dishes:
            dish_list.append(dish)

        return dish_list

    def extract_recipe(self,soup):
        recipe_list = []
        recipes = soup.findAll('div',attrs={'class' : 'step'})
        for recipe in recipes:
            step = recipe.find("p")
            if step != None:
               recipe_list.append(step.text.strip())

        return recipe_list

    def extract_ingredients(self,soup):
        ingredient_list = []
        ingredients = soup.find('div',attrs={'class': 'ingredients'}).find("ul").findChildren()
        for ingredient in ingredients:
            ingredient_list.append(ingredient.text.strip())
            
        return ingredient_list

    def extract_nutrition(self,soup):
        nutrition_list = []
        nutrients = soup.find('div',attrs={'class': 'partial recipe-nutrition'}).find("ul").findChildren()
        for nutrient in nutrients:
            nutrition_list.append(nutrient.text.strip())
            
        return nutrition_list
  
    def extract_prep_info(self,soup):
        stat_dict = {}
        stat_value = soup.findAll('div',attrs={'class': 'recipe-meta-item-body'})
        stat_key = soup.findAll('div',attrs={'class': 'recipe-meta-item-header'})
        for key,val in zip(stat_key,stat_value):
             stat_dict.update({key.text.strip() : val.text.strip()})        
        return stat_dict