from django.contrib import admin

from api.models import Company,Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)

# Register your models here.

