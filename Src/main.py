from cse_extraction import *
from VideoDetection import *

def main():

    ##To clear the image slate 
    ClearImageFolder()
    
    ##Instantiate the class object
    facedetection = VideoCapture()
    
    ##Call CaptureFrames from the class to begin the class detection
    search_key = facedetection.CaptureFrames()

    #search = "Search key is:" + search_key
    #search_key = "step by step recipe using tomatoes"
    
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
