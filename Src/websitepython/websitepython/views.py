from django.shortcuts import render
import sys
from pathlib import Path

#It's the current file location
HERE = Path(__file__).parent

sys.path.append(str(HERE / '../../'))

#Importing the main() function
from main import main

#For renderting the HTML page
def button(request):
    return render(request,'home.html')

#For displaying the output once the button is clicked
def output(request):
    search = main()
    key_name = ['Dish','Prep Statistics','Recipe','Nutrition','Ingredient']
    return render(request,'home.html',{'search': search,'key_name':key_name})