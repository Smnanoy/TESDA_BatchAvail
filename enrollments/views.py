from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from courses.models import Batch
from .models import Enrollment


@login_required
@require_POST
def enroll(request, batch_id):
    batch = get_object_or_404(Batch, pk=batch_id)

    if batch.status != 'open' or batch.slots_left <= 0:
        messages.error(request, 'This batch is no longer accepting enrollments.')
    elif Enrollment.objects.filter(trainee=request.user, batch=batch).exists():
        messages.warning(request, 'You already applied to this batch.')
    else:
        Enrollment.objects.create(trainee=request.user, batch=batch)
        messages.success(request, 'Your enrollment is now pending approval.')

    return redirect('trainee_home')


@login_required
@require_POST
def cancel_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk, trainee=request.user)
    if enrollment.status == 'pending':
        enrollment.delete()
        messages.success(request, 'Your application was cancelled.')
    else:
        messages.error(request, 'Only pending applications can be cancelled.')
    return redirect('trainee_home')