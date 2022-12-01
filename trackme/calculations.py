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

def calcStage(stage) :
    
    sodiumul = stage.healthy_dv_sodium_ul
    sodiumll = stage.healthy_dv_sodium_ll
    proteinul = stage.healthy_dv_protein_ul
    proteinll = stage.healthy_dv_protein_ll
    water = 0
    k = 0
    phos = 0

    stageValues = {
        'sodiumul' : sodiumul, 
        'sodiumll' : sodiumll,
       'proteinul' :  proteinul, 
       'proteinll' :  proteinll, 
       'water' :  water, 
       'k' :  k, 
       'phos' :  phos
    }
    return(stageValues)