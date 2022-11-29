from django.db import models
from datetime import datetime, timedelta
# Create your models here.


class Morbidity (models.Model):
    type_name = models.CharField(max_length=30)
    food_suggestions = models.CharField(max_length=200)
    
    def __str__ (self) :
        return (self.type_name)

    
class Stage (models.Model) :
    stage_name = models.CharField(max_length=30)

    #healthy serum levels: upper and lower limits
    healthy_serum_k_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_k_ll = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_phos_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_phos_ll = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_na_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_na_ll = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_creatinine_ul_men = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_creatinine_ll_men = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_creatinine_ul_women = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_creatinine_ll_women = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_albumin_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_albumin_ll = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_bloodsugar_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_serum_bloodsugar_ll = models.DecimalField(max_digits=8, decimal_places=2)

    #healthy DV/RDA levels: upper and lower limits
    healthy_dv_sodium_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_sodium_ll = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_protein_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_protein_ll = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_water_ul_men = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_water_ll_men = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_water_ul_women = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_water_ll_women = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_k_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_k_ll = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_phos_ul = models.DecimalField(max_digits=8, decimal_places=2)
    healthy_dv_phos_ll = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__ (self) :
        return (self.stage_name)
class Person(models.Model) :
    morbidity_type = models.ManyToManyField(Morbidity, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, blank=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    height_feet = models.IntegerField(default=0)
    height_inches = models.IntegerField(default=0)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__ (self) :
        return (self.full_name)

    @property
    def full_name(self) :
        return '%s %s' % (self.first_name, self.last_name)

class LabReport(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    k = models.DecimalField(max_digits=8, decimal_places=2)
    phos = models.DecimalField(max_digits=8, decimal_places=2)
    Na = models.DecimalField(max_digits=8, decimal_places=2)
    creatinine = models.DecimalField(max_digits=8, decimal_places=2)
    albumin = models.DecimalField(max_digits=8, decimal_places=2)
    bloodSugar = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__ (self) :
        return (self.person.full_name)
class JournalEntry(models.Model) :
    date = models.DateField(default=datetime.today, blank=True)
    meal = models.CharField(max_length=20)
    food_name = models.CharField(max_length=50)
    servings = models.DecimalField(max_digits=8, decimal_places=2)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)

    #Micro Sub-Values per Journal Entry (Daily totals calculated by date)

    DV_sodium = models.DecimalField(max_digits=8, decimal_places=2)
    DV_protein = models.DecimalField(max_digits=8, decimal_places=2)
    DV_water = models.DecimalField(max_digits=8, decimal_places=2)
    DV_k = models.DecimalField(max_digits=8, decimal_places=2)
    DV_phos = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__ (self) :
        return (self.entry_title)

    @property
    def entry_title(self) :
        return '%s %s' % (str(self.date), self.meal)