from trackme.models import JournalEntry, Person, LabReport, Stage, Morbidity
from decimal import Decimal

def calcTotals(journals, current_person) :
    sodium = 0
    protein = 0
    k = 0
    phos = 0
    weight = current_person.weight * Decimal(0.45359237)

    for entry in journals :
        sodium += entry.DV_sodium
        protein += entry.DV_protein
        k += entry.DV_k
        phos += entry.DV_phos
    #take total protein and make per kg
    perkg = round((protein/weight), 2)

    totals = {
       'sodium' : sodium, 
       'protein' :  perkg, 
       'k' :  k, 
       'phos' :  phos
       }
    return(totals)

def calcStage(stage, person) :
    
    sodiumul = stage.healthy_dv_sodium_ul
    sodiumll = stage.healthy_dv_sodium_ll
    proteinul = stage.healthy_dv_protein_ul
    proteinll = stage.healthy_dv_protein_ll
    # if person.gender == "male" :
    #     waterul = stage.healthy_dv_water_ul_men
    #     waterll = stage.healthy_dv_water_ll_men
        
    # else: 
    #     waterul = stage.healthy_dv_water_ul_women
    #     waterll = stage.healthy_dv_water_ll_women
       
    kul = stage.healthy_dv_k_ul
    kll = stage.healthy_dv_k_ll
    phosul = stage.healthy_dv_phos_ul
    phosll = stage.healthy_dv_phos_ll

    stageValues = {
        'sodiumul' : sodiumul,
        'sodiumll' : sodiumll,
        'proteinul' :  proteinul, 
        'proteinll' :  proteinll, 
        'kul' : kul,
        'kll' :  kll, 
        'phosul' :  phosul,
        'phosll' : phosll,
        
    }
    return(stageValues)

def checkRange(value, ll, ul) :
    if value < ll :
        return ("Daily intake is lower than recommended")
    elif value > ul :
        return ('Daily intake is higher than recommended')
    else :
        return ('Daily intake is in the recommended range!')
def alert(micros, stages) :
    alerts = {
       'sodium' : checkRange(micros['sodium'], stages['sodiumll'], stages['sodiumul']),
       'protein' :  checkRange(micros['protein'], stages['proteinll'], stages['proteinul']),
       'k' :  checkRange(micros['k'], stages['kll'], stages['kul']),
       'phos' :  checkRange(micros['phos'], stages['phosll'], stages['phosul'])
       }
    return(alerts)
