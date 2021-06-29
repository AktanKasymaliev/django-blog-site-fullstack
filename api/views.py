from rest_framework import generics
from blogs.models import Comments
from .serializers import CommentsSerializer

class CommentsView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    
# TODO улучшить вид html, сделать unnit test'ы, возможно добавить docker, сделать систему профилей