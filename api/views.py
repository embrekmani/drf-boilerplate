from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsBlogOwner
from .serializers import BlogSerializer
from blog.models import Blog

class CreateBlogView(generics.ListCreateAPIView):
    """ This class defines the create behaviour of our REST api. """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticated, IsBlogOwner)
    
    def perform_create(self, serializer):
        """ Save the post data when creating a new bucketlist """
        serializer.save(owner=self.request.user)

class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ This class handles the http GET, PUT and DELETE requests. """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticated, IsBlogOwner)