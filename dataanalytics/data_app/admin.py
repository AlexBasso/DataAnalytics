from django.contrib import admin
from .models import Car, Sale, Order, Person
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .resource import OrderResource


class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = OrderResource


class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Car)
admin.site.register(Sale)
admin.site.register(Order, OrderAdmin)
admin.site.register(Person, PersonAdmin)
