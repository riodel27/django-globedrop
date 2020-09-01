from django.contrib import admin
from .models import Organization

# Register your models here.


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization


admin.site.register(Organization, OrganizationAdmin)
