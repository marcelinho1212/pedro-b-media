from django.db import models


class Lead(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    service = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.service}"