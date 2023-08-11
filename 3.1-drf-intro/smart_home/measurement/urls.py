from django.urls import path

from measurement.views import SensorView, SensorDetailView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
