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

def searchItem(food_id) : 
  url = "https://api.nal.usda.gov/fdc/v1/food/" + str(food_id) + "?api_key=sCGPWgSfRBPOVcf7w5KfIOuckccjw3R85ebjzBKs"

  response = requests.request("GET", url)

  json_data = json.loads(response.text)

  nutrients = json_data['labelNutrients']

  return(nutrients)

import requests
import json


def searchItemName2(searchItem):
  url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + str(searchItem) + "&pageSize=10&api_key=sCGPWgSfRBPOVcf7w5KfIOuckccjw3R85ebjzBKs"

  response = requests.request("GET", url)

  json_data = json.loads(response.text)

  fooditems = (json_data['foods'][0:10])
  nutrient_ids = [1092,1091,1093,1003]
  nutrient_list = []
  dictionary2_list = []
  x = 0
  for item in fooditems:
    nutrient_list.clear()
    food_nutrients = item['foodNutrients']
    for nutrients in food_nutrients: 
      nutrient = nutrients['nutrientId'] 
      if nutrient in nutrient_ids:
        dictionary = {
              "nutrient_id" : nutrient,
              "nutrient_name" : nutrients['nutrientName'],
              "value" : nutrients['value'],
              "unit" : nutrients['unitName']
              }
        nutrient_list.append(dictionary)
      else:
        pass
    
    dictionary2 = {
        "food_id" : item['fdcId'],
        "food_name" : item['lowercaseDescription'],
        "nutrients" : nutrient_list
    }
    dictionary2_list.append(dictionary2)
        
  return dictionary2_list

import requests
import json

def idSearch(searchID):
  url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + str(searchID) + "&pageSize=10&api_key=sCGPWgSfRBPOVcf7w5KfIOuckccjw3R85ebjzBKs"

  response = requests.request("GET", url)
  json_data = json.loads(response.text)
  food_nutrients = json_data['foods'][0]['foodNutrients']

  nutrient_ids = [1092,1091,1093,1003]
  nutrient_list = []
  

  for nutrients in food_nutrients: 
      nutrient = nutrients['nutrientId'] 
      if nutrient in nutrient_ids:
        dictionary = {
              "nutrient_id" : nutrient,
              "nutrient_name" : nutrients['nutrientName'],
              "value" : nutrients['value'],
              "unit" : nutrients['unitName']
              }
        nutrient_list.append(dictionary)
      else:
        pass
        
  return nutrient_list


def assignMicros(food_item) :
  protein_value = 0
  sodium_value = 0
  phos_value = 0
  k_value = 0
  for i in food_item :
    if i['nutrient_name'] == 'Protein' :
      protein_value = i['value']
    elif i['nutrient_name'] == 'Sodium, Na' :
      sodium_value = i['value']
    elif i['nutrient_name'] == 'Potassium, K' :
      k_value = i['value']
    elif i['nutrient_name'] == 'Phosphorus, P' :
      phos_value = i['value']

  ordered_nutrients = [protein_value, sodium_value, k_value, phos_value]
  return (ordered_nutrients)

    