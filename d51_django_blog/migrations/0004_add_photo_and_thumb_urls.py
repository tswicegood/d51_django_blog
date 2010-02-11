
from south.db import db
from django.db import models
from d51_django_blog.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'D51Blog.photo_url'
        db.add_column('d51_django_blog_d51blog', 'photo_url', models.CharField(max_length=200, null=True, blank=True))
        
        # Adding field 'D51Blog.thumb_url'
        db.add_column('d51_django_blog_d51blog', 'thumb_url', models.CharField(max_length=200, null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'D51Blog.photo_url'
        db.delete_column('d51_django_blog_d51blog', 'photo_url')
        
        # Deleting field 'D51Blog.thumb_url'
        db.delete_column('d51_django_blog_d51blog', 'thumb_url')
        
    
    
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
