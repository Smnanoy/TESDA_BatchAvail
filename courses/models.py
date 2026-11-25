from django.db import models


class TrainingCenter(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    duration_hours = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Batch(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('full', 'Full'),
        ('closed', 'Closed'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='batches')
    training_center = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE, related_name='batches')
    batch_name = models.CharField(max_length=100)          # e.g. Batch 2026-01
    start_date = models.DateField()
    end_date = models.DateField()
    schedule = models.CharField(max_length=100, blank=True)  # e.g. Mon-Fri, 8AM-5PM
    total_slots = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')

    class Meta:
        ordering = ['start_date']

    @property
    def enrolled_count(self):
        return self.enrollments.filter(status='approved').count()

    @property
    def slots_left(self):
        return max(self.total_slots - self.enrolled_count, 0)

    def __str__(self):
        return f"{self.course.name} - {self.batch_name}"