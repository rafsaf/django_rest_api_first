from django.contrib import admin
import books.models as models
# Register your models here.

admin.site.register(models.Book)
admin.site.register(models.Author)