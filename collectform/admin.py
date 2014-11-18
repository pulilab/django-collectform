from django.contrib import admin
from .models import DistributionRequests, Vidzios

class VidziosInline(admin.StackedInline):
    model = Vidzios

class DistributionRequestAdmin(admin.ModelAdmin):
    inlines = [
        VidziosInline
    ]
    list_display = ['name', 'email', 'created']

admin.site.register(DistributionRequests, DistributionRequestAdmin)