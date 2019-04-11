from django.db import models
from django.utils.text import slugify
import itertools

class Blog(models.Model):
    """ This class represents the blog model. """
    title = models.CharField(max_length=140, blank=False)
    body = models.TextField(blank=False)
    slug = models.SlugField(unique=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return a human readable representation of the model instance. """
        return "{}".format(self.title)

    def _get_unique_slug(self):
        slug = orig = slugify(self.title)
        for x in itertools.count(1):
            if not Blog.objects.filter(slug=slug).exists():
                break
            slug = '%s-%d' % (orig, x)
        return slug
    
    def save(self, *args, **kwargs):
        self.slug = self._get_unique_slug()
        super(Blog, self).save(*args, **kwargs)