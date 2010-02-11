
from south.db import db
from django.db import models
from d51_django_blog.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
        for blog in orm.D51Blog.objects.all():
            blog.thumb_url = blog.photo_url = blog.link 
            blog.save()    
    
    def backwards(self, orm):
        "Write your backwards migration here"
        for blog in orm.D51Blog.objects.all():
            blog.link = blog.photo_url
            blog.save()
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'd51_django_blog.d51blog': {
            'Meta': {'ordering': "['-published',]"},
            'add_date': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'author': ('models.ForeignKey', ["orm['auth.User']"], {'null': 'True', 'blank': 'True'}),
            'content': ('RichTextField', [], {}),
            'display_title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'internal_title': ('models.CharField', [], {'max_length': '255'}),
            'link': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified_date': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'photo_url': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'published': ('models.DateTimeField', [], {}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'summary': ('RichTextField', [], {}),
            'thumb_url': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['d51_django_blog']
