from django.contrib import admin
from web.models import Books, Rental, Members


class RentalAdmin(admin.ModelAdmin):
    list_display = ['id','book','user_name']
    
admin.site.register(Books)
admin.site.register(Rental, RentalAdmin)
admin.site.register(Members)
