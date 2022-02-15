from django.contrib import admin
from news_app.models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)


class NewsAdmin(admin.ModelAdmin):
    list_display=['category', 'sub_category', 'news_title', 'description']
    class Media:
        js=("category_drop/category_ajax.js",)

admin.site.register(News,NewsAdmin)