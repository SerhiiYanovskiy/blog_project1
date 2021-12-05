from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(max_length=500)
    slug = models.SlugField(max_length=60,null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)+'-'+str(self.id)
            self.save()