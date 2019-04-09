from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Faculties)
class FacultyAdmin(admin.ModelAdmin):
    pass