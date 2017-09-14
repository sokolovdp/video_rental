from django.contrib import admin

from . import models


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']  # in this order fields will appear
    search_fields = ['title', 'length']  # create search box

admin.site.register(models.Movie, MovieAdmin)


admin.site.register(models.Customer)
