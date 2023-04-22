from django.contrib import admin
from .models import Goods, DeliveryNotes, DeliveryNoteDetails, AdditionalServices, ServiceDetails, Cost

# Register your models here.

admin.site.register(Goods)
admin.site.register(DeliveryNotes)
admin.site.register(DeliveryNoteDetails)
admin.site.register(AdditionalServices)
admin.site.register(ServiceDetails)
admin.site.register(Cost)
