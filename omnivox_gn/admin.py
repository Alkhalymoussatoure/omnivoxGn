from django.contrib import admin
from .models import Etablissement,Etudiant
# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Etablissement)