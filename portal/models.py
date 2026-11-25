from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title