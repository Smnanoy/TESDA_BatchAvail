from django.contrib import admin
from .models import TrainingCenter, Course, Batch


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('course', 'batch_name', 'training_center', 'start_date', 'total_slots', 'slots_left', 'status')
    list_filter = ('status', 'course', 'training_center')
    search_fields = ('batch_name', 'course__name')


admin.site.register(TrainingCenter)
admin.site.register(Course)