from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class RichTextField(models.TextField):
    pass

class D51Blog(models.Model):
    internal_title = models.CharField(max_length=255)
    display_title = models.CharField(null=True, blank=True, max_length=255)

    summary = RichTextField()
    content = RichTextField()
    meta_keywords = models.CharField(null=True, blank=True, max_length=255)

    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, blank=True, null=True)
    published = models.DateTimeField()

    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    @property
    def title(self):
        return self.display_title or self.internal_title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-published',]
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'
        app_label = getattr(settings, "D51_DJANGO_BLOG_APP_LABEL", "blog")
