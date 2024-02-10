from django.contrib import admin
from .models import Order, Person
from import_export.admin import ImportExportModelAdmin
from .resource import OrderResource


class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = OrderResource


class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(Person, PersonAdmin)
