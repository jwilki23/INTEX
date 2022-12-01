import requests
import json

def searchItemName(searchItem):
  url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + searchItem + "&pageSize=10&api_key=sCGPWgSfRBPOVcf7w5KfIOuckccjw3R85ebjzBKs"

  response = requests.request("GET", url)

  json_data = json.loads(response.text)

  fooditems = (json_data['foods'][0:10])
  list_dict = []
  dictionary = {}

  # print(fooditems)
  for item in fooditems:
     dictionary = {
         "item_id":(item['fdcId']), 
         "item_name" : (item['lowercaseDescription'])
     }
     list_dict.append(dictionary)

  return list_dict

list_dict = searchItemName("apple")

