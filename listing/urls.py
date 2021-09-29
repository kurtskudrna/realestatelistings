from django.urls import path
from . import views


urlpatterns = [
    path('homes', views.HomeListings.as_view()),
    path('homes/<int:pk>', views.SingleHome.as_view())
]
