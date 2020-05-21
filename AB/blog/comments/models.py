from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey # This is added in generic foriegnkey part-2
from django.contrib.contenttypes.models import ContentType

from django.db import models

from blog_app.models import Post



class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE) 

    # This is added in generic foriegnkey part-2
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


