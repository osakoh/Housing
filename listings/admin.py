from django.contrib import admin
from .models import Listing


# admin.site.register(Listing)
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'state')
    list_display_links = ('id', 'title')  # fields to be linked
    list_filter = ('realtor',)  # filter section on the right side of admin page
    list_editable = ('is_published', )  # makes fields editable
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')  # creates a search field

    list_per_page = 10  # specify max amount of items to be displayed per page


