from __future__ import unicode_literals
import json
import traceback
from django.db import models
from django.template import Template as DjangoTemplate, Context
from jinja2 import Template as JinjaTemplate


class TemplateSnippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets')
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    context = models.TextField()
    rendered = models.TextField()
    engine = models.CharField(
        max_length=50, 
        choices=(('django', 'Django'), ('jinja2', 'Jinja'))
    )
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        self.rendered = self.render(self.code, self.context)
        self.context = json.dumps(self.context)
        self.processed = True
        return super(self.__class__, self).save(*args, **kwargs)
    
    def render(self, code, context):
        try:
            if self.engine.lower() == 'django':
                return DjangoTemplate(code).render(Context(context))
            elif self.engine.lower() == 'jinja2':
                return JinjaTemplate(code).render(**context) 
            else:
                raise Exception('Invalid engine: {}'.format(self.engine))
        except Exception as e:
            return {
                'exception': unicode(e),
                'traceback': traceback.format_exc()
            }



