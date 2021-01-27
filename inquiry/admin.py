from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'inquiry_date')
    list_display_links = ('id', 'name')  # fields to be linked
    list_filter = ('name', 'email', 'listing')  # filter section on the right side of admin page
    search_fields = ('name', 'email', 'listing')

    list_per_page = 20

