from django.contrib import admin
from .import models
# Register your models here.


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','published','staus')
    prepopulated_fields = {'slug':('title',)}


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)    
    
