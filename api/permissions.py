from rest_framework.permissions import BasePermission
from blog.models import Blog

class IsBlogOwner(BasePermission):
    """ Custom permission class to allow only owner of blog to edit them """

    def has_object_permission(self, request, view, obj):
        """ Return true if permission is granted to the blog owner """
        if isinstance(obj, Blog):
            return obj.owner == request.user
        return obj.owner == request.user