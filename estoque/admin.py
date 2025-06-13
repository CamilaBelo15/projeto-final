from django.contrib import admin

# Register your models here.
from .models import Produto,Entrada,Saida

admin.site.register(Produto)
admin.site.register(Entrada)
admin.site.register(Saida)