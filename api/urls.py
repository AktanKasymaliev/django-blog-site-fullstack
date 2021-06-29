from django.urls import path
from .views import CommentsView

urlpatterns = [
    path('v1/comments/create/', CommentsView.as_view())
]