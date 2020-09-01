from django.contrib import admin
from .models import Organization

# Register your models here.


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ('name', 'description', 'country', 'city',
                    'picture', 'created_at', 'updated_at')
    ordering = ['created_at']


admin.site.register(Organization, OrganizationAdmin)
