from django.urls import path
from . import views

urlpatterns = [
    path('enroll/<int:batch_id>/', views.enroll, name='enroll'),
    path('enrollment/<int:pk>/cancel/', views.cancel_enrollment, name='cancel_enrollment'),
]