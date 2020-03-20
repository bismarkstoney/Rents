from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'listing', 'email', 'contact_date','message', 'phone', 'user_id', 'listing_id')
    list_display_links=('id', 'name')
    search_fields=('email', 'name')

admin.site.register(Contact, ContactAdmin)