from cse_extraction import *
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.append(str(HERE / 'object_detection'))
from object_detection_tensorflow import *

def main():

    #Tensorflow API Call 
    objects= object_detect()

    #Our search key
    search_key = "Step by step recipes using"

    for object_entry in objects:
        search_key += str(object_entry + " and ")

    #Removing the last and
    search_key = "Tomatoes"

    print("Search key is " + search_key)

    #Gives us back the results dict object from the Customized Search Engine
    search_results = collect_cse_results(search_key)

    #Extract the website name for the scrapping
    website_list = extract_website_name(search_results)

    #Gives us back the dictionary required for the search query from
    #all the website links which will be used as sources for getting
    #the ingredients for us
    #Key is the link and value is the host name
    website_dict = create_ingredients_sources(website_list,search_results)

    print(website_dict)

    #Extracting data
    main_list = extract_info(website_dict)
   
    return main_list


if __name__ == '__main__':
    main()
