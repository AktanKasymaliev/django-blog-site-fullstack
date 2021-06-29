from django.urls import path
from .views import HomePage, DetailPage

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path("read/<int:pk>/", DetailPage.as_view(), name='read')
]