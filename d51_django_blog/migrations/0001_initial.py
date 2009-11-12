
from south.db import db
from django.db import models
from d51_django_blog.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'D51Blog'
        db.create_table('d51_django_blog_d51blog', (
            ('id', models.AutoField(primary_key=True)),
            ('internal_title', models.CharField(max_length=255)),
            ('display_title', models.CharField(max_length=255, null=True, blank=True)),
            ('summary', RichTextField()),
            ('content', RichTextField()),
            ('meta_keywords', models.CharField(max_length=255, null=True, blank=True)),
            ('slug', models.SlugField(unique=True)),
            ('author', models.ForeignKey(orm['auth.User'], null=True, blank=True)),
            ('published', models.DateTimeField()),
            ('add_date', models.DateTimeField(auto_now_add=True)),
            ('modified_date', models.DateTimeField(auto_now=True)),
        ))
        db.send_create_signal('d51_django_blog', ['D51Blog'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'D51Blog'
        db.delete_table('d51_django_blog_d51blog')
        
    
    
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
            'meta_keywords': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified_date': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'published': ('models.DateTimeField', [], {}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'summary': ('RichTextField', [], {})
        }
    }
    
    complete_apps = ['d51_django_blog']
