from django.contrib import admin
from .models import Morbidity, Stage, Person, LabReport, JournalEntry

# Register your models here.
admin.site.register(Morbidity)
admin.site.register(Stage)
admin.site.register({Person})
admin.site.register(LabReport)
admin.site.register(JournalEntry)