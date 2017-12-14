from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Sentence)
admin.site.register(Chapter)