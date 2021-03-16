from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} #связка слага с именем для url *подроб. в Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','slug', 'price', 'available') #отображение разделов
    list_filter = ('category', 'available') #фильтры для поиска товара
    list_editable = ('category', 'price', 'available') #возможность редактировать цену и категорию прямо в main window
    prepopulated_fields = {'slug': ('name',)} #автоматически подставляет нужные символы и переводит в латиницу для отображение слага в url