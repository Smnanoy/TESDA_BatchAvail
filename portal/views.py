from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from courses.models import Batch
from enrollments.models import Enrollment
from .models import Notification


def home(request):
    batches = (
        Batch.objects
        .select_related('course', 'training_center')
        .filter(status='open')[:8]
    )
    return render(request, 'portal/home.html', {'batches': batches})


@login_required
def dashboard_redirect(request):
    if request.user.role == 'admin' or request.user.is_superuser:
        return redirect('admin:index')
    return redirect('trainee_home')


@login_required
def trainee_home(request):
    my_enrollments = (
        Enrollment.objects
        .filter(trainee=request.user)
        .select_related('batch__course', 'batch__training_center')
    )
    applied_ids = my_enrollments.values_list('batch_id', flat=True)

    open_batches = (
        Batch.objects
        .filter(status='open')
        .exclude(pk__in=applied_ids)
        .select_related('course', 'training_center')
    )
    announcements = Notification.objects.filter(is_published=True)[:5]

    return render(request, 'portal/trainee_home.html', {
        'my_enrollments': my_enrollments,
        'open_batches': open_batches,
        'announcements': announcements,
    })