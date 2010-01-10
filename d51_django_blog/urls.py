from django.conf.urls.defaults import url, patterns, include, handler404, handler500

urlpatterns = patterns(
    'd51_django_blog.views',
    url('^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[a-zA-Z0-9\-_]+)/$', 'post_detail', name='post-detail'),
)
