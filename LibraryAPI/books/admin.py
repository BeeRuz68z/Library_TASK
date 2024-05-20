from django.contrib import admin

from .models import *

# Register your models here

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publicationDate','ISBN')
    list_display_links = ('id','title')
    search_fields = ('title', 'author')
    list_per_page =10

admin.site.register(Book)
