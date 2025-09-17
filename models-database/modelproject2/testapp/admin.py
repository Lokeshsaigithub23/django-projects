from django.contrib import admin

# Register your models here.
from testapp.models import employee
class employeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
admin.site.register(employee,employeeAdmin)    