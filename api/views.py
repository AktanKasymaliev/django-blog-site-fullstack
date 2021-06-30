from rest_framework import generics
from blogs.models import Comments
from .serializers import CommentsSerializer
from rest_framework.permissions import IsAuthenticated

class CommentsView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated]
    
