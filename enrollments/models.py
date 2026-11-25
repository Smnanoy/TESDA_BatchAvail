from django.conf import settings
from django.db import models
from courses.models import Batch


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    trainee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('trainee', 'batch')   # a trainee can't apply twice to the same batch
        ordering = ['-date_applied']

    def __str__(self):
        return f"{self.trainee} -> {self.batch} ({self.status})"