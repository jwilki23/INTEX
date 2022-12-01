import requests
import json

def searchItemName(searchItem):
  url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + str(searchItem) + "&pageSize=10&api_key=sCGPWgSfRBPOVcf7w5KfIOuckccjw3R85ebjzBKs"

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


def getNutrients(searchItem, food_id):
  url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + str(searchItem) + "&pageSize=10&api_key=sCGPWgSfRBPOVcf7w5KfIOuckccjw3R85ebjzBKs"

  response = requests.request("GET", url)

  json_data = json.loads(response.text)

  fooditems = (json_data['foods'][0:10])
  nutrient_ids = [1092,1091,1093,1003]
  nutrient_list = []
  
  for item in fooditems:
    if item['fdcId'] == food_id:
      food_nutrients = item['foodNutrients']
      for nutrient in food_nutrients: 
        nutrient_id = nutrient['nutrientId']
        if nutrient_id in nutrient_ids:
          dictionary = {
            "nutrient_id" : nutrient_id,
            "nutrient_name" : nutrient['nutrientName'],
            "value" : nutrient['value'],
            "unit" : nutrient['unitName']
            }
          nutrient_list.append(dictionary)

    else: 
      pass

  return nutrient_list

