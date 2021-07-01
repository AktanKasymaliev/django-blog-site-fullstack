from django.urls import path
from .views import HomePage, DetailPage, RegisterView, LogInView, LogOutView

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path("read/<int:pk>/", DetailPage.as_view(), name='read'),
    path('signup/user/', RegisterView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout')
]