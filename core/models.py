from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to="portfolio/")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

class PortfolioPhoto(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="portfolio_photos/")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title