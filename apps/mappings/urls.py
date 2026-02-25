from django.urls import path
from .views import (
    MappingListCreateView,
    MappingDetailDeleteView,
    PatientDoctorMappingListView,
)

urlpatterns = [
    path("", MappingListCreateView.as_view()),
    path("<int:patient_id>/", PatientDoctorMappingListView.as_view()),
    path("delete/<int:pk>/", MappingDetailDeleteView.as_view()),
]