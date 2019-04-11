from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """ Meta class to map serializer's data fields with the model fields """
        model = Blog
        fields = ('id', 'slug', 'title', 'body', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('slug', 'date_created', 'date_modified')
