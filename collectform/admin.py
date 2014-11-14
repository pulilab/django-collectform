from django.contrib import admin
from .models import DistributionRequests, Vidzios

class VidziosInline(admin.StackedInline):
    model = Vidzios

class DistributionRequestAdmin(admin.ModelAdmin):
    inlines = [
        VidziosInline
    ]

admin.site.register(DistributionRequests, DistributionRequestAdmin)