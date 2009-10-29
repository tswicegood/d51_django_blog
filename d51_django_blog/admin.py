from django.contrib import admin
from models import D51Blog, RichTextField
from widgets import dijit_with_plugins 
from django.conf import settings
import os

class D51BlogAdmin(admin.ModelAdmin):
    list_display = (
        'internal_title', 
        'display_title',
        'author',
        'published',
        'add_date',
        'modified_date',
    )

    list_filter = (
        'author',
        'modified_date',
        'published',
        'meta_keywords',
    )

    list_editable = (
        'display_title',
        'published',
    )

    exclude = ('author',)

    formfield_overrides = {
        RichTextField:{
            'widget':dijit_with_plugins([
                'copy', 'cut', 'paste', 'bold', 'italic',
            ])
        }
    }

    prepopulated_fields = {'slug':('display_title',)}
    def save_model(self, request, obj, form, change):
        if obj.author is None:
            obj.author = request.user
        return super(self.__class__, self).save_model(request, obj, form, change)

    class Media:
        js = (
            'http://www.google.com/jsapi',
            os.path.join(getattr(settings, "D51_DJANGO_BLOG_MEDIA", "d51blog"), 'js/admin.js'),
        )
        css = {
            'all':(
                'http://ajax.googleapis.com/ajax/libs/dojo/1.3.2/dojo/resources/dojo.css', 
                'http://ajax.googleapis.com/ajax/libs/dojo/1.3.2/dijit/themes/tundra/tundra.css',
            )
        }

admin.site.register(D51Blog, D51BlogAdmin)
