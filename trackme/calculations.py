from trackme.models import JournalEntry

def calcTotals(journals) :
    sodium = 0
    protein = 0
    water = 0
    k = 0
    phos = 0

    for entry in journals :
        sodium += entry.DV_sodium
        protein += entry.DV_protein
        water += entry.DV_water
        k += entry.DV_k
        phos += entry.DV_phos

    totals = {
       'sodium' : sodium, 
       'protein' :  protein, 
       'water' :  water, 
       'k' :  k, 
       'phos' :  phos
       }
    return(totals)

def calcStage(stage, person) :
    
    sodiumul = stage.healthy_dv_sodium_ul
    sodiumll = stage.healthy_dv_sodium_ll
    proteinul = stage.healthy_dv_protein_ul
    proteinll = stage.healthy_dv_protein_ll
    if person.gender == "male" :
        waterul = stage.healthy_dv_water_ul_men
        waterll = stage.healthy_dv_water_ll_men
    else: 
        waterul = stage.healthy_dv_water_ul_women
        waterll = stage.healthy_dv_water_ll_women
    kul = stage.healthy_dv_k_ul
    kll = stage.healthy_dv_k_ll
    phosul = stage.healthy_dv_phos_ul
    phosll = stage.healthy_dv_phos_ll

    stageValues = {
        'sodiumul' : sodiumul, 
        'sodiumll' : sodiumll,
        'proteinul' :  proteinul, 
        'proteinll' :  proteinll, 
        'waterul' :  waterul, 
        'waterll' : waterll,
        'kul' : kul,
        'kll' :  kll, 
        'phosul' :  phosul,
        'phosll' : phosll,
    }
    return(stageValues)

def checkRange(value, ll, ul) :
    if value < ll :
        return ("on the low side")
    elif value > ul :
        return ('on the high side')
    else :
        return ('within the appropriate range!')
def alert(micros, stages) :
    alerts = {
       'sodium' : checkRange(micros['sodium'], stages['sodiumll'], stages['sodiumul']),
       'protein' :  checkRange(micros['protein'], stages['proteinll'], stages['proteinul']),
       'water' :  checkRange(micros['water'], stages['waterll'], stages['waterul']),
       'k' :  checkRange(micros['k'], stages['kll'], stages['kul']),
       'phos' :  checkRange(micros['phos'], stages['phosll'], stages['phosul'])
       }
    return(alerts)