from django.contrib import admin
from .models import *
# Register your models here.

class GPUAdmin(admin.ModelAdmin):
    list_display = ['model']

admin.site.register(GPU)