from django.contrib import admin
from .models import Portfolio, PortfolioPhoto


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "video_url", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)

@admin.register(PortfolioPhoto)
class PortfolioPhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)