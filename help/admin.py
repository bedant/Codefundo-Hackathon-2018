from django.contrib import admin
from .models import Ticket
# Register your models here.
class Admin(admin.ModelAdmin):
    class Meta:
	
        model = Ticket
        verbose_name = 'Help Request'
        verbose_name_plural = 'Help Requests'

admin.site.register(Ticket, Admin)

    