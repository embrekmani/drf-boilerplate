from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateBlogView, BlogDetailsView

urlpatterns = {
    path('blog/', CreateBlogView.as_view(), name='create'),
    re_path(r'^blog/(?P<pk>[0-9]+)/$', BlogDetailsView.as_view(), name='details'),
}

urlpatterns = format_suffix_patterns(urlpatterns)