from django.forms import Textarea
from django.utils.safestring import mark_safe

def dijit_with_plugins(plugins=None):
    if plugins is None:
        plugins = ['copy', 'cut', 'paste', 'bold']

    class RichTextWidget(Textarea):
        def render(self, name, value, attrs=None):
            if attrs is None:
                attrs = {}

            our_plugins = mark_safe("['"+"','".join(plugins)+"']")
            attrs.update({
                'dojoType':'dijit.Editor',
                'plugins':our_plugins
            })
            return super(self.__class__, self).render(name, value, attrs)
    return RichTextWidget
