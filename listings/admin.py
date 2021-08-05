from django.contrib import admin

from .models import Listing, Category


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)