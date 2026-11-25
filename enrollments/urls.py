from django.urls import path
from . import views

urlpatterns = [
    path('enroll/<int:batch_id>/', views.enroll, name='enroll'),
]