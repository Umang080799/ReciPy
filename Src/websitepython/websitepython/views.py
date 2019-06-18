from django.shortcuts import render
import sys
from pathlib import Path

HERE = Path(__file__).parent

sys.path.append(str(HERE / '../../'))

from main import main

#For renderting the HTML page
def button(request):
    return render(request,'home.html')

#For displaying the output once the button is clicked
def output(request):
    search = main()
    return render(request,'home.html',{'search': search})